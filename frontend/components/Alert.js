export default function Alert({ message }) {
  if (!message) return null;
  return (
    <div style={{ color: "red", fontWeight: "bold", margin: "10px 0" }}>
      {message}
    </div>
  );
}
