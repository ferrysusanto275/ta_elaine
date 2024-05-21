const year_api = base_api_url + "isi/year";
const pca_api = base_api_url + "isi/pca";
const area_api = base_api_url + "area";
const year_cb_filter = document.getElementById("year_cb_filter");
const cari_cb_filter = document.getElementById("cari_cb_filter");
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
        cek_area();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const cek_area = () => {
  fetch(area_api)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      if (data.length > 0) {
        data.forEach((element, i) => {
          let option = document.createElement("option");
          option.value = element.id;
          option.textContent = element.nama;
          let option_filter = option.cloneNode(true);
          // area_cb.appendChild(option);
          cari_cb_filter.appendChild(option_filter);
        });
        load_img();
        // load_data();
      } else {
        location.href = "area";
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const load_img = () => {
  tampil_perbandingan.innerHTML = "";
  tampil_perbandingan.appendChild(
    create_pca(year_cb_filter.value, cari_cb_filter.value)
  );
};
const create_link = (year, cari) => {
  return `${pca_api}/${year}/${cari}`;
};
const create_pca = (year, cari) => {
  const img_tampil = document.createElement("img");
  img_tampil.src = create_link(year, cari);
  return img_tampil;
};
year_cb_filter.onchange = load_img;
cari_cb_filter.onchange = load_img;
cek_year();
