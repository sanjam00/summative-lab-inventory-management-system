import { useState, useEffect } from 'react'
import './App.css'
import SearchBar from './components/SearchBar'
import ItemCard from './components/ItemCard'
import Header from './components/Header'
import AddItemForm from './components/AddItemForm'
import ItemList from './components/ItemList'

function App() {

  const [inventory, setInventory] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/inventory")
      .then(res => res.json())
      .then(data => setInventory(data))
      .catch(err => console.error(err));
  }, []);

  function handleNewItem(newItem) {
    setInventory(prev => [...prev, newItem])
  }

  function handleSearch(term) {
    setSearchTerm(term);
  }

  const filteredItems = inventory.filter(item =>
    item.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  function handleDelete(id) {
    fetch(`http://localhost:5000/inventory/${id}`, {
      method: "DELETE"
    }).then(() => {
      setInventory(prev => prev.filter(item => item.id !== id));
    });
  }

  function handleUpdate(updatedItem) {
    fetch(`http://localhost:5000/inventory/${updatedItem.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(updatedItem)
    })
      .then(res => res.json())
      .then(data => {
        setInventory(prev =>
          prev.map(item => item.id === data.id ? data : item)
        );
      });
  }

  return (
    <div>
      <Header />

      <SearchBar onSearch={handleSearch} />

      <AddItemForm onAddItem={handleNewItem} inventory={inventory} setInventory={setInventory} />
      <h1>Inventory</h1>

      <ItemList items={filteredItems} onDelete={handleDelete} onUpdate={handleUpdate} />
    </div>
  )
}

export default App