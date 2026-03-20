import os
from flask import Flask, jsonify
from providers.json_inventory_provider import JsonInventoryDataProvider

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/inventory.json")

_provider = JsonInventoryDataProvider(DATA_PATH)

# GET /inventory - GET all available products
@app.route("/inventory")
def get_inventory():
  _provider.load()

  inventory = _provider.all_inventory()
  return jsonify([ item.to_dict() for item in inventory ]), 200

# GET /inventory/id - get that specific product
@app.route("/inventory/<int:id>")
def get_item(id):
  _provider.load()

  item = _provider.get_item(id)
  if not id:
    return jsonify({"error": "Item not found"}), 404
  return jsonify(item.to_dict()), 200  

if __name__ == "__main__":
  app.run(debug=True, port=5000)