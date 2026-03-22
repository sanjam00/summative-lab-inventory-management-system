import ItemCard from "./ItemCard";

export default function ItemList({items, props}) {
  return (
    <div className="item-container">
      {items.map(i => (
          items.length === 0 ? (<p>No items found</p>) : <ItemCard key={i.id} item={i} />
      ))}
    </div>
  )
}