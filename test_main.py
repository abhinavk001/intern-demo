"""
Testing endpoints
"""
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

sample_data = {
    "id": 16,
    "first_name": "James",
    "last_name": "Butt",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutttt@gmail.comm",
    "web": "http://www.bentonjohnbjr.com",
    "age": 70
}

def test_post():
    """
    Test post on /api/users endpoint.
    """
    response = client.post('/api/users', json=sample_data)
    assert response.status_code == 201
    assert response.json() == {"message":"User created successfully"}

def test_get_all_users():
    """
    Test fetching all users
    """
    response = client.get('/api/users/')
    assert response.status_code == 200

def test_get_user_by_id():
    """
    Test fetch user by id
    """
    response = client.get(f'/api/users/{sample_data["id"]}')
    assert response.status_code == 200
    assert response.json() == sample_data

def test_patch():
    """
    Test updating user information
    """
    response = client.patch(f'/api/users/{sample_data["id"]}', json={
        "first_name": "John",
        "last_name": "Smith",
        "age": 60
    })
    assert response.status_code == 200
    assert response.json() == {"message":"User updated successfully"}

def test_delete():
    """
    Testing deleting users
    """
    response = client.delete(f'/api/users/{sample_data["id"]}')
    assert response.status_code == 200
    assert response.json() == {"message":"User deleted successfully"}