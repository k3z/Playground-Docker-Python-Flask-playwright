import os


def env_var(key, default=None):
    val = os.environ.get(key, default)
    if val == "True":
        val = True
    elif val == "False":
        val = False
    return val


DEBUG = env_var("DEBUG", True)
SECRET_KEY = env_var(
    "SECRET_KEY",
    "b5a6ab31-dd0e-4ab3-a410-9c18a1992146",
)
USE_TLS = env_var("USE_TLS", False)

CORS_ORIGIN = env_var("CORS_ORIGIN", "*")
CORS_CREDENTIALS = env_var("CORS_CREDENTIALS", False)
CORS_MAX_AGE = env_var("CORS_MAX_AGE", 60 * 60 * 24)

API_SWAGGER_UI = env_var("API_SWAGGER_UI", "/api-documentation/")
