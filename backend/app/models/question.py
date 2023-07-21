from app import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    question_text = db.Column(db.String(255, nullable=False))
    
    answers = db.relationship('Answer', back_populates='question')
    quiz = db.relationship('Quiz', back_populates='questions')
