from flask import Blueprint, request, jsonify, session
from app.forms.signin import SigninForm

bp = Blueprint('', __name__)


@bp.route('/')
def index():
    return render_template('page.html')

@bp.route('/signin')
def signin():
    return render_template('signin.html')

@bp.route('/signup')
def signup():
    return render_template('signup.html')

@bp.route('/me')
def home():
    return '<h1>Home Page</h1>'