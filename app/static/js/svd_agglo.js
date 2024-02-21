const year_api = base_api_url + "isi/year";
const pca_api = base_api_url + "isi/svd_agglo";
const year_cb_filter = document.getElementById("year_cb_filter");
const cari_cb_filter = document.getElementById("cari_cb_filter");
const linkage_cb_filter = document.getElementById("linkage_cb_filter");
const cek_year = () => {
  fetch(year_api)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      if (data.length == 0) {
        location.href = "isi";
      } else {
        data.forEach((element, i) => {
          let option = document.createElement("option");
          option.value = element;
          option.textContent = element;

          year_cb_filter.appendChild(option);
        });
        load_img();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const load_img = () => {
  tampil_perbandingan.innerHTML = "";
  tampil_perbandingan.appendChild(create_pca(year_cb_filter.value, cari_cb_filter.value));
};
const create_link = (year, cari, linkage) => {
  return `${pca_api}/${year}/${cari}/${linkage}`;
};
const create_pca = (year, cari, linkage) => {
  const img_tampil = document.createElement("img");
  img_tampil.src = create_link(year, cari, linkage);
  return img_tampil;
};
year_cb_filter.onchange = load_img;
cari_cb_filter.onchange = load_img;
linkage_cb_filter.onchange = load_img;
cek_year();
