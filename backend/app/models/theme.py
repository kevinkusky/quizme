from app import db

themes = db.Table('themes',
    db.Column('theme_id', db.Integer, db.ForeignKey('theme.id')),
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'))
)


class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    quizzes = db.relationship('Quiz', secondary=themes, back_populates='themes')
