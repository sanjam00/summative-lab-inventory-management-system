import ItemCard from "./ItemCard";

export default function ItemList({items, onDelete, onUpdate, props}) {
  return (
    <div className="item-container">
      {items.map(i => (
        items.length === 0 ? (<p>No items found</p>) : <ItemCard key={i.id} item={i} onDelete={onDelete} onUpdate={onUpdate} />
      ))}
    </div>
  )
}