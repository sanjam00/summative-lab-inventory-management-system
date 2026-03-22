
export default function ItemCard({item, props}) {
  return (
    <div className="item-card" data-testid="item-card">
      <h3>{item.name}</h3>
      <p>Description: {item.description}</p>
      <p>Price: ${item.price}</p>
      <p>Quantity: {item.quantity}</p>
      <p>Category: {item.category}</p>
      <p>Brand: {item.product.brands}</p>
      <p>Ingredients: {item.product.ingredients_text}</p>
    </div>  )
}