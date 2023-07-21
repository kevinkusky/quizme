from app import db


class Answer(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String(255, nullable=False))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)
    
    question = db.relationship('Question', back_populates='answers')
