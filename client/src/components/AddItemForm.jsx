import { useState } from "react"

export default function AddItemForm({ onAddItem, inventory, setInventory, showNotification, props}) {
  const [isOpen, setIsOpen] = useState(false);
  const [formData, setFormData] = useState({
    name: "",
    description: "",
    price: "",
    quantity: "",
    category: "",
  })

  function handleChange(e) {
    const { name, type, value, checked } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }))
  }

  function handleSubmit(e) {
    e.preventDefault();

    fetch("http://localhost:5000/inventory", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    })
      .then(r => {
        if (!r.ok) { throw new Error("Post request failed") }
        return r.json()
      })
      .then(newItem => {
        console.log(newItem)
        onAddItem(newItem)
        showNotification("Item added successfully!", "success");
        setInventory([...inventory, newItem]);
        setFormData({
          name: "",
          description: "",
          price: "",
          quantity: "",
          category: ""
        });
      })
      .catch(() => {
        showNotification("Failed to add item", "error");
      });
  };
  
  return(
    <div className="add-item-container">
      <h3>Add Item</h3>

      <button className="add-item-btn" onClick={() => setIsOpen(prev => !prev)} style={{ marginBottom: "8px" }}>
        {isOpen ? "Close Form" : "Open Form"}
      </button>

      {isOpen && (
      <form onSubmit={handleSubmit} >

        <label htmlFor="name-input">Name:</label>
        <input id="name-input" type="textbox" name="name" value={formData.name} onChange={handleChange}/>

        <label htmlFor="description-input">Description:</label>
        <input id="description-input" type="textbox" name="description" value={formData.description} onChange={handleChange} />

        <label htmlFor="price-input">Price:</label>
        <input id="price-input" type="textbox" name="price" value={formData.price} onChange={handleChange} />

        <label htmlFor="quantity-input">Quantity:</label>
        <input id="quantity-input" type="textbox" name="quantity" value={formData.quantity} onChange={handleChange} />

        <label htmlFor="category-input">Category:</label>
        <input id="category-input" type="textbox" name="category" value={formData.category} onChange={handleChange} />

        <button type="submit" id="addItemSubmit">Add Item</button>
      </form>

      )}
    </div>
  )
}
