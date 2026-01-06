def test_users_ping(test_app):
    """
    Ensure the /users/ping route behaves correctly.
    """
    response = test_app.get("/users/ping")
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "message": "pong!",
        "environment": "test",
        "testing": True,
    }
