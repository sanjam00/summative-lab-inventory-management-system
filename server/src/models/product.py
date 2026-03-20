
"""
Do I even need this class since the "products" key has a value of another dictionary?
Prof's example needs another class becuase it's an array of dictionaries.
"""
from dataclasses import dataclass, asdict

@dataclass
class ProductInfo():
  product_name: str
  brands: str
  ingredients_text: str

  @classmethod
  def from_dict(cls, data):
    if not data:
      return None

    return cls(
        product_name=data.get("product_name", ''),
        brands=data.get("brands", ''),
        ingredients_text=data.get("ingredients_text", '')
      )
  
  def to_dict(self):
    return asdict(self)