# services/users/project/tests/test_users.py
from project.tests.conftest import add_user


def test_add_user(test_app):
    """Ensure a new user can be added to the database."""
    response = test_app.post(
        "/users", json={"username": "primerpy", "email": "info@primerpy.com"}
    )
    data = response.json()
    assert response.status_code == 201
    assert "info@primerpy.com was added!" in data["message"]
    assert data["status"] == "success"


def test_add_user_invalid_json(test_app):
    """Ensure error is thrown if the JSON object is empty."""
    response = test_app.post("/users", json={})
    assert response.status_code == 422


def test_add_user_invalid_json_keys(test_app):
    """Ensure error is thrown if the JSON object does not have a username key."""
    response = test_app.post("/users", json={"email": "info@primerpy.com"})
    assert response.status_code == 422


def test_add_user_duplicate_email(test_app):
    """Ensure error is thrown if the email already exists."""
    test_app.post("/users", json={"username": "primerpy", "email": "info@primerpy.com"})
    response = test_app.post(
        "/users", json={"username": "primerpy", "email": "info@primerpy.com"}
    )
    data = response.json()
    assert response.status_code == 400
    assert "Sorry. That email already exists." in data["message"]
    assert data["status"] == "fail"


def test_single_user(test_app):
    """Ensure get single user behaves correctly."""
    user = add_user("primerpy2", "primerpy2@primerpy.com")
    response = test_app.get(f"/users/{user.id}")
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["username"] == "primerpy2"
    assert data["data"]["email"] == "primerpy2@primerpy.com"
    assert data["status"] == "success"


def test_single_user_invalid_id(test_app):
    """Ensure error is thrown if an id is not valid."""
    response = test_app.get("/users/blah")
    assert response.status_code == 422


def test_single_user_incorrect_id(test_app):
    """Ensure error is thrown if the id does not exist."""
    response = test_app.get("/users/999")
    data = response.json()
    assert response.status_code == 404
    assert "User does not exist" in data["message"]
    assert data["status"] == "fail"


def test_all_users(test_app):
    """Ensure get all users behaves correctly."""
    add_user("harry", "harry@testdriven.io")
    add_user("ron", "ron@testdriven.io")
    response = test_app.get("/users")
    data = response.json()
    assert response.status_code == 200
    assert len(data["data"]["users"]) >= 2
    assert data["status"] == "success"
