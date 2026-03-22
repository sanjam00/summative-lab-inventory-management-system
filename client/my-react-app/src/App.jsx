import { useState, useEffect } from 'react'
import './App.css'
import SearchBar from './components/SearchBar'
import ItemCard from './components/ItemCard'
import Header from './components/Header'
import AddItemForm from './components/AddItemForm'

function App() {

  const [inventory, setInventory] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/inventory")
      .then(res => res.json())
      .then(data => setInventory(data))
      .catch(err => console.error(err));
  }, []);

  function handleNewItem(newItem) {
    setInventory(prev => [...prev, newItem])
  }

  return (
    <div>
      <AddItemForm onAddItem={handleNewItem} inventory={inventory} setInventory={setInventory} />
      <h1>Inventory</h1>

      {/* place holder item mapping, will implement component later */}
      {inventory.length === 0 ? (
        <p>No items found</p>
      ) : (
        inventory.map(item => (
          <div key={item.id} style={{ border: "1px solid gray", margin: "10px", padding: "10px" }}>
            <h2>{item.name}</h2>
            <p>{item.description}</p>
            <p><strong>Price:</strong> ${item.price}</p>
            <p><strong>Quantity:</strong> {item.quantity}</p>
            <p><strong>Category:</strong> {item.category}</p>

            {item.product && (
              <div>
                <p><strong>Brand:</strong> {item.product.brands}</p>
                <p><strong>Ingredients:</strong> {item.product.ingredients_text}</p>
              </div>
            )}
          </div>
        ))
      )}
    </div>
  )
}

export default App
