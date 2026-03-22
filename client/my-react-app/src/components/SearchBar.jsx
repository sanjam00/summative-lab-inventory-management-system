import { useState } from "react"

export default function SearchBar({ onSearch , props}) {
  const [query, setQuery] = useState("");

  function handleChange(e) {
    const value = e.target.value;
    setQuery(value);
    onSearch(value); // send value to parent
  }

  return (
    <div style={{ margin: "20px 0" }}>
      <input
        type="text"
        placeholder="Search inventory..."
        value={query}
        onChange={handleChange}
        style={{ padding: "8px", width: "300px" }}
      />
    </div>
    );
}