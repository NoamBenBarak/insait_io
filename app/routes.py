from flask import Blueprint, request, jsonify
from . import db
from .models import QuestionAnswer
import uuid
from app.utils import get_openai_response


bp = Blueprint('routes', __name__)


@bp.route('/', methods=['GET'])
def index():
    return ("hello"),200
    

@bp.route('/ask', methods=['POST', 'GET'])
def handle_question():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        question = data.get("question")
        if not question:
            return jsonify({"error": "Missing question in request body"}), 400
        try:
            response = get_openai_response(question)
            new_entry = QuestionAnswer(id=str(uuid.uuid4()),question=question, answer=response)
            db.session.add(new_entry)
            db.session.commit()
            return jsonify({"answer": response}), 200
        except Exception as e:
            print(f"Error getting answer: {e}")
            return jsonify({"error": "Failed to generate answer"}), 500

    else:
        return jsonify({"error": "Invalid request"}), 400
