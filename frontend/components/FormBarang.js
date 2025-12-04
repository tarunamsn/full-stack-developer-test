import { useState } from "react";

export default function FormBarang({ initialData = {}, onSubmit }) {
  const [name, setName] = useState(initialData.name || "");
  const [kategori, setKategori] = useState(initialData.kategori || "");
  const [stok, setStok] = useState(initialData.stok || 0);
  const [hargaBeli, setHargaBeli] = useState(initialData.harga_beli || 0);
  const [hargaJual, setHargaJual] = useState(initialData.harga_jual || 0);
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (stok < 0) return setError("STOK TIDAK BOLEH MINUS!");
    if (hargaJual < hargaBeli) return setError("HARGA JUAL HARUS LEBIH TINGGI DARI HARGA BELI");

    onSubmit({ name, kategori, stok, harga_beli: hargaBeli, harga_jual: hargaJual });
  };

  return (
    <form onSubmit={handleSubmit}>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <div>
        <label>Name:</label>
        <input value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div>
        <label>Ketegori:</label>
        <input value={kategori} onChange={(e) => setKategori(e.target.value)} required />
      </div>
      <div>
        <label>Stok:</label>
        <input type="number" value={stok} onChange={(e) => setStok(Number(e.target.value))} required />
      </div>
      <div>
        <label>Harga Beli:</label>
        <input type="number" value={hargaBeli} onChange={(e) => setHargaBeli(Number(e.target.value))} required />
      </div>
      <div>
        <label>Harga Jual:</label>
        <input type="number" value={hargaJual} onChange={(e) => setHargaJual(Number(e.target.value))} required />
      </div>
      <button type="submit">SIMPAN</button>
    </form>
  );
}
