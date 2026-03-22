export default function Notification({ message, type }) {
  if (!message) return null;

  const colors = {
    info: "#333",
    success: "green",
    error: "red"
  };

  return (
    <div style={{
      position: "fixed",
      top: "20px",
      left: "50%",
      transform: "translateX(-50%)",
      background: colors[type],
      color: "white",
      padding: "10px 20px",
      borderRadius: "8px",
      zIndex: 1000
    }}>
      {message}
    </div>
  );
}