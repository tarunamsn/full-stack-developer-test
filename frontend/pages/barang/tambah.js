import Layout from "../../components/Layout";
import FormBarang from "../../components/FormBarang";
import { createBarang } from "../../services/barangService";
import { useRouter } from "next/router";

export default function TambahBarang() {
  const router = useRouter();

  const handleSubmit = async (data) => {
    await createBarang(data);
    router.push("/dashboard");
  };

  return (
    <Layout>
      <h2>Tambah Barang</h2>
      <FormBarang onSubmit={handleSubmit} />
    </Layout>
  );
}
