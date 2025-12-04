import api from "./api";

export const getBarang = async () => {
  const response = await api.get("/barang/");
  return response.data;
};

export const createBarang = async (barangData) => {
  const response = await api.post("/barang/", barangData);
  return response.data;
};

export const updateBarang = async (id, itemData) => {
  const response = await api.put(`/barang/${id}`, barangData);
  return response.data;
};

export const deleteBarang = async (id) => {
  const response = await api.delete(`/barang/${id}`);
  return response.data;
};
