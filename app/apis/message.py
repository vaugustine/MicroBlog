from flask import jsonify, Blueprint, request

from app.models.models import db, Message

messages = Blueprint('messages',__name__)

@messages