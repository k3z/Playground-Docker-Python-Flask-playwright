import pytest
from api.app import create_app


@pytest.fixture
def app():
    flask_app = create_app()

    ctx = flask_app.app_context()
    ctx.push()

    yield flask_app

    ctx.pop()


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


@pytest.fixture
def data(app):
    return {
        "FOO": "BAR",
    }
