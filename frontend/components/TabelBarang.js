import Link from "next/link";

export default function TabelBarang({ items, onDelete, userRole }) {
  return (
    <table border="1" cellPadding="5" style={{ width: "100%", marginTop: "20px" }}>
      <thead>
        <tr>
          <th>Nama</th>
          <th>Kategori</th>
          <th>Stok</th>
          <th>Harga Beli</th>
          <th>Harga Jual</th>
          <th>Total Nilai</th>
          {userRole === "gudang" && <th>Actions</th>}
        </tr>
      </thead>
      <tbody>
        {items.map((item) => (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.category}</td>
            <td>{item.stock}</td>
            <td>{item.purchase_price}</td>
            <td>{item.selling_price}</td>
            <td>{item.stock * item.purchase_price}</td>
            {userRole === "gudang" && (
              <td>
                <Link href={`/barang/${item.id}/edit`}>EDIT</Link>{" "}
                <button onClick={() => onDelete(item.id)}>HAPUS</button>
              </td>
            )}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
