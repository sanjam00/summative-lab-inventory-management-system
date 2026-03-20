
from models.product import ProductInfo
from dataclasses import dataclass, asdict

@dataclass
class StockItem():
  quantity: int
  id: int
  product: ProductInfo

  @classmethod
  def from_dict(cls, data):
    return cls(
      quantity = data.get('quantity', 0),
      id = data.get('id', 0),
      product=ProductInfo.from_dict(data.get('product', {}))
      # product = data.get(ProductInfo.from_dict(p) for p in data.get('product', {}))
    )
  
  def to_dict(self) -> dict:
    return asdict(self)