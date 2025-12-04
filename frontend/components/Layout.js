import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import Link from "next/link";

export default function Layout({ children }) {
  const { user, logout } = useContext(AuthContext);

  return (
    <div>
      <header style={{ display: "flex", justifyContent: "space-between", padding: "10px", background: "#eee" }}>
        <h1>MANAJEMEN INVENTARIS BARANG</h1>
        {user && (
          <div>
            <span>{user.role}</span>
            <button onClick={logout}>LOGOUT</button>
          </div>
        )}
      </header>
      <nav style={{ margin: "10px" }}>
        <Link href="/dashboard">Dashboard</Link> |{" "}
        <Link href="/sales">Penjualan</Link>
      </nav>
      <main>{children}</main>
    </div>
  );
}
