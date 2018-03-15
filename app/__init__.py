import os
from flask import Flask

from app.models.models import db
from app.apis.user import users

def create_app():

	app = Flask(__name__)
	app.config.from_object(os.environ.get('FLASK_CONFIG') or 'config')
	db.init_app(app)
	with app.app_context():
		db.create_all()

	app.register_blueprint(users)

	@app.route('/')
	def index():
		return 'Welcome to Microblog by vaugusti !!!'

	return app