
class InventoryItem:
  def __init__(self, id=None, name="", description="", price=0.0, quantity=0, category=None):
    self.id = id
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity
    self.category = category
    self.product = {}

  def __str__(self):
    return f"InventoryItem(id={self.id}, name='{self.name}', quantity={self.quantity}, price=${self.price}, description='{self.description}', category={self.category}, product={self.product})"

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "price": self.price,
      "quantity": self.quantity,
      "category": self.category,
      "product": self.product
    }
  
  @classmethod
  def from_dict(cls, data):
    item = cls(
      id=data.get("id"),
      name=data.get("name", ""),
      description=data.get("description", ""),
      price=data.get("price", 0.0),
      quantity=data.get("quantity", 0),
      category=data.get("category", None)
    )
    item.product = data.get("product") or {}
    return item