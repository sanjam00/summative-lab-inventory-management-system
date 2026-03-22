import os
import json
# from models.stock import StockItem
from models.inventory_item import InventoryItem

class JsonInventoryDataProvider():
  def __init__(self, filename):
    self._filename = filename
    self._items = []

  def _initialize_empty_file(self):
    # DO I NEED THIS METHOD???
    # Initializes the json file with an empty list
    with open(self.file_path, "w") as f:
      json.dump({}, f)

  def load(self):
    # reads data from the filepath
    if not os.path.exists(self._filename):
      self._items = []
      return

    with open(self._filename, "r", encoding="utf-8") as f:
      data = json.load(f)
      self._items = [InventoryItem.from_dict(item) for item in data]

  def save(self):
    data = [item.to_dict() for item in self._items]
    with open(self._filename, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=2)

  def all_inventory(self):
    # filter data, transform, hydrate, augment
    return self._items
  
  def get_item(self, id):
    return next((item for item in self._items if item.id == id), None)

  def add_item(self, item):
    # generate id
    max_id = max([i.id for i in self._items], default=0)
    item.id = max_id + 1

    self._items.append(item)
    self.save()

  def delete_item(self, id):
    self._items = [item for item in self._items if item.id != id]
    self.save()

def update_item(self, id, data):
  item = self.get_item(id)

  if not item:
    return None

  item.name = data.get("name", item.name)
  item.description = data.get("description", item.description)
  item.price = data.get("price", item.price)
  item.quantity = data.get("quantity", item.quantity)
  item.category = data.get("category", item.category)
  item.product = data.get("product", item.product)

  self.save()

  return item