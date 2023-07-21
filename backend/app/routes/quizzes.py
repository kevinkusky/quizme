from flask import Blueprint, render_template

bp = Blueprint('quizzes', __name__, url_prefix='/quiz')

@bp.route('/<id>')
def get_quiz(id):
    pass
