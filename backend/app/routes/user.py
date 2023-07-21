from flask import Blueprint, request, jsonify
from app.models import User
from app import db

bp = Blueprint('user', __name__, url_prefix='/users')

@bp.route('/<id>', methods=['GET'])
def get_user(id):
    """Queries db and returns user data"""
    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

@bp.route('/', methods=['POST'])
def create_user():
    """Creates a user and adds it to the db, returning user data"""
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'Missing Fields'}), 400
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    try:
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as error:
        return jsonify({'error': str(error)}), 400

 