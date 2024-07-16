import pytest
import os

from app import create_app, db
from app.models import QuestionAnswer

@pytest.fixture(scope='module')
def test_client():
    app = create_app()  
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URI')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_ask_question(test_client):
    # Sample question
    question_data = {'question': 'What is the capital of France?'}

    # Send a POST request
    response = test_client.post('/ask', json=question_data)

    # Assertions
    assert response.status_code == 200
    assert 'answer' in response.json
    assert response.json['answer'] == {"answer": "Paris"}

