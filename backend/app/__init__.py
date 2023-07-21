import os
from flask import Flask
from flask_bcrypt import Bcrypt
from .models import db
from app.config import configuration

bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])
    db.init_app(app)
    bcrypt.init_app(app)
    

    from .routes import quizzes, main

    app.register_blueprint(quizzes.bp)
    app.register_blueprint(main.bp)

    return app
