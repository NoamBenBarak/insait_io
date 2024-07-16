from flask import Flask, request, jsonify
from openai import OpenAI
from config import OPENAI_API_KEY, hostname, database, username, pwd, port_id
from sqlalchemy import create_engine, Column, String 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
import uuid

openai_client = OpenAI(api_key=OPENAI_API_KEY)
DATABASE_URL = f"postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}"


Base = declarative_base()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db) 

class QuestionAnswer(Base):
    __tablename__ = "question_answer"

    id = Column(String, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.route('/')
def index():
    return "Hello world2"

@app.route('/ask', methods=['POST'])
def handle_question():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        question = data.get("question")
        if not question:
            return jsonify({"error": "Missing question in request body"}), 400
        try:
            # response = openai_client.chat.completions.create(
            # model="gpt-3.5-turbo-0125",
            # response_format={ "type": "json_object" },
            # messages=[
            #     {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            #     {"role": "user", "content": question}
            # ]
            # )
            # answer = response.choices[0].text.strip()
            answer = "Paris"
            db = next(get_db())
            new_entry = QuestionAnswer(id=str(uuid.uuid4()), question=question, answer=answer)
            db.add(new_entry)
            db.commit()
            return jsonify({"answer": answer})
        except Exception as e:
            print(f"Error getting answer: {e}")
            return jsonify({"error": "Failed to generate answer"}), 500

    else:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == "__main__":
    app.run(debug=True)