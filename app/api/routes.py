"""Sample API routes."""
from flask_restful import Resource
from flask_login import login_required


class Home(Resource):
    """Sample home resource."""

    def get(self):
        """Welcome page/message."""
        return {'message': 'Hello World!'}


class Protected(Resource):
    """Sample protected resource."""

    @login_required
    def get(self):
        """Login to access this protected route."""
        return {'message': 'You must be logged in to view this message.'}
