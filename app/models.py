from app import db

class QuestionAnswer(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)