import { useEffect, useState, useContext } from "react";
import Layout from "../components/Layout";
import { AuthContext } from "../context/AuthContext";
import { getBarang, deleteBarang } from "../services/barangService";
import TabelBarang from "../components/TabelBarang";
import Alert from "../components/Alert";

export default function Dashboard() {
  const { user } = useContext(AuthContext);
  const [barang, setBarang] = useState([]);
  const [filterKategori, setFilterKategori] = useState("");
  const [minStok, setMinStok] = useState(0);
  const [alertMessage, setAlertMessage] = useState("");
 
  const fetchBarang = async () => {
    const data = await getBarang();
    setBarang(data);
    const stokTipis = data.filter((i) => i.stok <= 5); // threshold 5
    if (stokTipis.length)
        setAlertMessage("BEBERAPA ITEM KEKURANGAN STOK. SILAKAN PERIKSA DI INVENTARIS.");
  };

  useEffect(() => {
    fetchBarang();
  }, []);

  const handleDelete = async (id) => {
    if (!confirm("BARANG INI AKAN DIHAPUS. APAKAH ANDA YAKIN UNTUK MENGHAPUS BARANG INI?")) return;
    await deleteBarang(id);
    fetchBarang();
  };

  const filteredBarang = barang.filter((i) => 
    (!filterKategori || i.kategori.includes(filterKategori)) &&
    i.stok >= minStok
  );

  return (
    <Layout>
      <h2>DASHBOARD INVENTARIS</h2>
      <Alert message={alertMessage} />

      <div>
        <label>Filter Kategori:</label>
        <input value={filterKategori} onChange={(e) => setFilterKategori(e.target.value)} />
        <label>Stok Minimum:</label>
        <input type="number" value={minStok} onChange={(e) => setMinStok(Number(e.target.value))} />
      </div>

      {user.role === "gudang" && <a href="/barang/create">Add New Item</a>}

      <TabelBarang items={filteredBarang} onDelete={handleDelete} userRole={user.role} />
    </Layout>
  );
}
