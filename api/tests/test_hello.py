import pytest  # noqa

# from .fixtures import reset_fixtures


# @pytest.fixture(autouse=True)
# def run_around_tests(app):
#     # before test
#     reset_fixtures()

#     yield

#     # after test
#     reset_fixtures()


def test_hello_world(client, app):
    r = client.get(
        "/",
    )
    assert r.text == "Hello World"


def test_private_api_version(client, app):
    r = client.get(
        "/v1/private/info/",
    )
    assert r.json.get("version") == 1
