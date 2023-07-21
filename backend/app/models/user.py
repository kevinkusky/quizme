from app import db, bcrypt

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))
)

saved_quizzes = db.Table('saved_quizzes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('quiz_id', db.Integer, db.ForeignKey('quizzes.id'))
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64, index=True, unique=True, nullable=False))
    email = db.Column(db.String(120, index=True, unique=True, nullable=False))
    password_hash = db.Column(db.String(128))

    quizzes =  db.relationship('Quiz', back_populates='owner')
    quiz_attempts = db.relationship('QuizAttempt', back_populates='user')
    followers = db.relationship('User',
                                secondary=followers,
                                primaryjoin=(followers.c.followed_id == id),
                                secondaryjoin=(followers.c.follower_id == id),
                                backref=db.backref('followed', lazy='dynamic'),
                                lazy='dynamic')
    saved_quizzes = db.relationship('Quiz',
                                    secondary=saved_quizzes,
                                    backref=db.backref('saved_by_users', lazy='dynamic'),
                                    lazy='dynamic')

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
