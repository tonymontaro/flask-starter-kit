from flask_restful import Resource
from app.models import User


class Home(Resource):
    def get(self):
        # user = User.query.filter_by(email='t@g.com').first()
        return 'Welcome!'
