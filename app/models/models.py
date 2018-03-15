from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	user_id = db.Column('user_id', db.Integer, primary_key=True)
	username = db.Column('username', db.String(64), unique=True, index=True, nullable=False)
	password = db.Column('password', db.String(64), nullable=False)

	def to_json(self):
		return {'username':self.username, 'password':self.password}

class Message(db.Model):
	__tablename__ = 'messages'
	message_id = db.Column('message_id', db.Integer, primary_key=True)
	message = db.Column('message', db.String, nullable=False)
	user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))

