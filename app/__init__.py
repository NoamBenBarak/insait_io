from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


db = SQLAlchemy()
migrate = Migrate()


Base = declarative_base()  

# Create the SQLAlchemy engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# Create a SessionLocal class bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Update this for testing
    if app.config['TESTING']:
        app.config.from_object('config.TestConfig')

    db.init_app(app)
    migrate.init_app(app, db)

    from . import routes, models
    app.register_blueprint(routes.bp)

    # Ensure that the database tables are created (for development only)
    with app.app_context():
        db.create_all()  # Ensure tables are created (use with caution in production)

    return app
