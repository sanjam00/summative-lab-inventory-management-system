import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

@pytest.fixture
def client():
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client

# GET all items
def test_get_inventory(client):
  response = client.get("/inventory")
  assert response.status_code == 200

  data = response.get_json()
  assert isinstance(data, list)

# GET single item
def test_get_single_item(client):
  response = client.get("/inventory/1")
  
  assert response.status_code in [200, 404]

# POST add item
def test_add_item(client):
  new_item = {
    "name": "Test Item",
    "description": "Testing",
    "price": 5.99,
    "quantity": 2,
    "category": "test",
    "product": {}
  }

  response = client.post("/inventory", json=new_item)
  assert response.status_code == 201

  data = response.get_json()
  assert data["name"] == "Test Item"

# PUT update item
def test_update_item(client):
  updated_item = {
    "name": "Updated Item",
    "description": "Updated",
    "price": 10.0,
    "quantity": 5,
    "category": "updated",
    "product": {}
  }

  response = client.put("/inventory/1", json=updated_item)

  assert response.status_code in [200, 404]

# DELETE item
def test_delete_item(client):
  response = client.delete("/inventory/1")

  assert response.status_code in [200, 404]

