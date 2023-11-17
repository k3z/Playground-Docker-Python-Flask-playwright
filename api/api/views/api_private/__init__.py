from flask import Blueprint
from flask import url_for
from flask import current_app as app
from flask_restx import Api

from api.config import API_SWAGGER_UI
from api.config import USE_TLS
from .ns_info import api as ns_info

api_private = Blueprint("api_private", __name__, url_prefix="/v1/private")


class APIHttps(Api):
    @property
    def specs_url(self):
        return url_for(
            self.endpoint("specs"),
            _external=True,
            _scheme="https" if USE_TLS is True else "http",
        )


api = APIHttps(
    api_private,
    version="1.0",
    title="API Private",
    description="",
    doc=API_SWAGGER_UI,
    authorizations={
        "JWT": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
    },
    default="General",
    default_label="General Operations",
)

api.add_namespace(ns_info)
