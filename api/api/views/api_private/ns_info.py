from flask_restx import Namespace
from flask_restx import Resource

api = Namespace("Info", path="/info")


@api.route("/")
class version(Resource):
    def get(self):
        """Version"""
        return {"version": 1}
