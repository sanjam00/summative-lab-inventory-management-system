import os
import json
from models.stock import StockItem

class JsonInventoryDataProvider():
  def __init__(self, filename):
    self._filename = filename
    self._items = []

  def load(self):
    # reads data from the filepath
    if not os.path.exists(self._filename):
      self._items = []

    with open(self._filename, "r", encoding="utf-8") as f:
      data = json.load(f)

      self._items = [StockItem.from_dict(item) for item in data]

    print(self._items)

  def save(self):
    data = [item.to_dict() for item in self._items]
    with open(self._filename, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=2)

  def all_inventory(self):
    # filter data, transform, hydrate, augment
    return self._items
  
  def get_item(self, id):
    return next(item for item in self._items if item.id == id)