import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import Layout from "../../../components/Layout";
import FormBarang from "../../../components/FormBarang";
import { getBarang, updateBarang } from "../../../services/barangService";

export default function EditItem() {
  const router = useRouter();
  const { id } = router.query;
  const [barangData, setBarangData] = useState(null);

  useEffect(() => {
    if (!id) return;
    const fetchBarang = async () => {
      const barang = await getBarang();
      const item = barang.find((i) => i.id === parseInt(id));
      setBarangData(item);
    };
    fetchBarang();
  }, [id]);

  const handleSubmit = async (data) => {
    await updateBarang(id, data);
    router.push("/dashboard");
  };

  if (!barangData) return <Layout>Harap Tunggu...</Layout>;

  return (
    <Layout>
      <h2>Edit Barang</h2>
      <FormBarang initialData={barangData} onSubmit={handleSubmit} />
    </Layout>
  );
}
