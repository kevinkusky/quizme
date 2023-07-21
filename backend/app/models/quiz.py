from app import db
from theme import themes


class Quiz(db.Model):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(64, index=True, nullable=False))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    questions = db.relationship('Question', back_populates='quiz')
    quiz_attempts = db.relationship('QuizAttempt', back_populates='quiz')
    owner = db.relationship('User', back_populates='quizzes')
    themes = db.relationship('Theme', secondary=themes, back_populates='quizzes')
