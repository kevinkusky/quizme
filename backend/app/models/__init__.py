from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User, followers
from .theme import Theme, themes
from .quiz import Quiz
from .question import Question
from .answer import Answer
