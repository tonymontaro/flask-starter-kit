from flask_restful import Resource
from flask_login import login_required


class Home(Resource):
    def get(self):
        return {'message': 'Hello World!'}


class Protected(Resource):
    @login_required
    def get(self):
        return {'message': 'You must be logged in to view this message.'}
