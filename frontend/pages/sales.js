import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import { getBarang } from "../services/barangService";
import { createSale, getSales } from "../services/salesService";

export default function SalesPage() {
  const [barang, setBarang] = useState([]);
  const [sales, setSales] = useState([]);
  const [selectedBarang, setSelectedBarang] = useState("");
  const [quantity, setQuantity] = useState(0);

  const fetchData = async () => {
    setBarang(await getBarang());
    setSales(await getSales());
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSale = async () => {
    if (!selectedBarang || quantity <= 0) return alert("PILIH BARANG DAN JUMLAH TERLEBIH DAHULU!");
    await createSale({ barang_id: parseInt(selectedBarang), quantity: parseInt(quantity) });
    setQuantity(0);
    fetchData();
  };

  return (
    <Layout>
      <h2>Rekor Penjualan</h2>
      <div>
        <select value={selectedBarang} onChange={(e) => setSelectedBarang(e.target.value)}>
          <option value="">Pilih Barang</option>
          {barang.map((i) => (
            <option key={i.id} value={i.id}>{i.name} (Stock: {i.stok})</option>
          ))}
        </select>
        <input type="number" value={quantity} onChange={(e) => setQuantity(Number(e.target.value))} placeholder="Quantity" />
        <button onClick={handleSale}>Rekor Penjualan</button>
      </div>

      <h3>Histori Penjualan</h3>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Barang</th>
            <th>Jumlah</th>
          </tr>
        </thead>
        <tbody>
          {sales.map((s) => (
            <tr key={s.id}>
              <td>{barang.find((i) => i.id === s.barang_id)?.name}</td>
              <td>{s.quantity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </Layout>
  );
}
