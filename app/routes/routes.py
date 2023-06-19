"""
The routes of my flask app
"""
from flask import Blueprint
from app.controller.mainController import  index,downloadPresentation
blueprint = Blueprint('blueprint',__name__)

blueprint.route('/',methods=['GET'])(index)
blueprint.route('/download',methods=['GET'])(downloadPresentation)
