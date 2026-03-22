import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from providers.json_inventory_provider import JsonInventoryDataProvider
from models.inventory_item import InventoryItem
from services.product_api import fetch_product_details

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/inventory.json")

_provider = JsonInventoryDataProvider(DATA_PATH)

# GET /inventory - GET all available products
@app.route("/inventory")
def get_all():
  _provider.load()

  inventory = _provider.all_inventory()
  return jsonify([ item.to_dict() for item in inventory ]), 200

# GET /inventory/id - get that specific product
@app.route("/inventory/<int:id>")
def get_item(id):
  _provider.load()

  item = _provider.get_item(id)
  if not item:
    return jsonify({"error": "Item not found"}), 404
  
  return jsonify(item.to_dict()), 200  

# POST /inventory
@app.route("/inventory", methods=["POST"])
def add_item():
  _provider.load()

  data = request.json
  item = InventoryItem.from_dict(data)

  product_data = fetch_product_details(item.name)
  item.product = product_data

  _provider.add_item(item)

  return jsonify(item.to_dict()), 201

# PUT /inventory/<id>
@app.route("/inventory/<int:id>", methods=["PUT"])
def update_item(id):
  _provider.load()

  data = request.json
  item = _provider.get_item(id)

  if not item:
    return jsonify({"error": "Item not found"}), 404

  item.name = data.get("name", item.name)
  item.description = data.get("description", item.description)
  item.price = data.get("price", item.price)
  item.quantity = data.get("quantity", item.quantity)
  item.category = data.get("category", item.category)
  item.product = data.get("product", item.product)

  _provider.save()

  return jsonify(item.to_dict()), 200

# DELETE /inventory/<id>
@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):
  original_len = len(_provider._items)

  _provider._items = [i for i in _provider._items if i.id != id]

  if len(_provider._items) == original_len:
    return jsonify({"error": "Item not found"}), 404

# # Register Routes
# inventory_routes = InventoryRoutes(inventory_provider, detail_services)
# inventory_routes.register(app)

if __name__ == "__main__":
  app.run(debug=True, port=5000)