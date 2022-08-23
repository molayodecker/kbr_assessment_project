import json

import pytest

from app.v1.api.users import user_crud


def test_create_users(test_app, monkeypatch):
    test_request_payload = {"firstname": "Jules", "lastname": "Kroll", "phone_number": 2127020707, "email": "string",
                            "street": "805 3rd Ave 29th floor", "city": "New York", "state": "NY", "zipcode": 10022}
    test_response_payload = {'message': 'successful'}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(user_crud, "post", mock_post)

    response = test_app.post("/user", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_user_invalid_json(test_app):
    response = test_app.post("/user", data=json.dumps({"firstname": "Jules"}))
    assert response.status_code == 422


def test_get_all_users(test_app, monkeypatch):
    test_data = [{"firstname": "Jules", "lastname": "Kroll", "phone_number": 2127020707, "email": "string",
                            "street": "805 3rd Ave 29th floor", "city": "New York", "state": "NY", "zipcode": 10022}]

    async def mock_get():
        return test_data

    monkeypatch.setattr(user_crud, "get_all", mock_get)

    response = test_app.get("/users")

    assert response.status_code == 200
    assert response.json() == test_data