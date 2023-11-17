from flask import Blueprint


bp_public = Blueprint(
    "public_views",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
    url_prefix="/",
)


@bp_public.route("/")
def index():
    return "Hello World"
