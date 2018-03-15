from flask import jsonify, Blueprint, request

from app.models.models import db, User

users = Blueprint('users',__name__)

@users.route('/users', methods=['POST'])
def create_user():
	user = request.get_json()
	user = User(username=user['username'], password=user['password'])
	db.session.add(user)
	db.session.commit()
	return jsonify(user.to_json()), 201

@users.route('/users', methods=['GET'])
def get_users():
	users = db.session.query(User)
	users = [user.to_json() for user in users]
	return jsonify({'users': users})