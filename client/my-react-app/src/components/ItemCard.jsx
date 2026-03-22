import { useState } from "react";

export default function ItemCard({item, onDelete, onUpdate, props}) {
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState(item);
  
  function handleChange(e) {
    const { name, value } = e.target;

    setEditData(prev => ({
      ...prev,
      [name]: value
    }));
  }

  function handleSubmit(e) {
    e.preventDefault();

    onUpdate({
      ...editData,
      price: parseFloat(editData.price),
      quantity: parseInt(editData.quantity)
    });

    setIsEditing(false);
  }

  return (
    <div>
      {isEditing 
      ? (<form onSubmit={handleSubmit}>

          <label htmlFor="edit-name">Name:</label>
          <input id="edit-name" name="name" value={editData.name} onChange={handleChange} />

          <label htmlFor="edit-description">Description:</label>
          <input id="edit-description" name="description" value={editData.description} onChange={handleChange} />

          <label htmlFor="edit-price">Price:</label>
          <input id="edit-price" name="price" value={editData.price} onChange={handleChange} />

          <label htmlFor="edit-quantity">Quantity:</label>
          <input id="edit-quantity" name="quantity" value={editData.quantity} onChange={handleChange} />

          <label htmlFor="edit-category">Category:</label>
          <input id="edit-category" name="category" value={editData.category} onChange={handleChange} />

          <button type="submit">Save</button>
          <button type="button" onClick={() => setIsEditing(false)}>Cancel</button>
      </form>
      ) : (
    <div className="item-card" data-testid="item-card">
      <h3>{item.name}</h3>
      <p>Description: {item.description}</p>
      <p>Price: ${item.price}</p>
      <p>Quantity: {item.quantity}</p>
      <p>Category: {item.category}</p>
      <p>Brand: {item.product.brands ? item.product.brands : "Not Available"}</p>
      <p>Ingredients: {item.product.ingredients_text ? item.product.ingredients_text : "Not Available"}</p>

      <button onClick={() => setIsEditing(true)}>Edit</button>
      <button onClick={() => onDelete(item.id)}>Delete</button>
    </div>
      )}
    </div>
  );
}