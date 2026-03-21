
"""
Will not be using this file for this specific project, 
but I included it based off of the Professor's example as a way to configure routes in a manner that is cleaner and more scalable
"""

class InventoryRoutes():
  # Class to manage inventory routes and handle dependency injection

  def __init___(self, inventory_provider, detail_services):
    self.inventory_provider = inventory_provider
    self.detail_services = detail_services

  def register(self, app):
    # Registers the routes directly with the Flask instance.
    @app.get("/inventory")
    def get_all():
      return self.get_all()

    @app.get("/inventory/<int:id>")
    def get_by_id(path: InventoryItemIDPath):
      return self.get_by_id(path)
    
    @app.post("/inventory")
    def add(query: InventoryQuery, body: InventoryItemSchema):
      return self.add(query, body)

    @app.put("/inventory/<int:id>")
    def update(path: InventoryItemIDPath, query: InventoryQuery, body: InventoryItemSchema):
      return self.update(path, query, body)
    
    @app.delete("/inventory/<int:id>")
    def delete(path: InventoryItemIDPath):
      return self.delete(path)
    
  def get_all(self):
    pass

  def get_by_id(self, path: InventoryItemIDPath):
    pass