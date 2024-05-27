const year_api = base_api_url + "isi/year";
const kmeans_api = base_api_url + "isi/plot_kmeans";
const bar_kmeans_api = base_api_url + "isi/bar_kmeans";
const top10_api = base_api_url + "isi/top10_kmeans";
// const score_api = base_api_url + "isi/kmeans_score";
const year_cb_filter = document.getElementById("year_cb_filter");
const area_cb_filter = document.getElementById("area_cb_filter");
const search_filter = document.getElementById("search");
const data_top10 = document.getElementById("data_top10");

const area_api = base_api_url + "area";
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
const handle_year = () => {
  load_img();
};
const isi_data = () => {
  data_top10.innerHTML = "";
  fetch(`${top10_api}/${year_cb_filter.value}/${area_cb_filter.value}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      const sortedKeys = Object.keys(data).sort((a, b) => data[b] - data[a]);
      sortedKeys.forEach((key) => {
        const row = document.createElement("tr");
        data_top10.appendChild(row);

        let cell = document.createElement("td");
        cell.textContent = key;
        row.appendChild(cell);

        cell = document.createElement("td");
        cell.textContent = data[key].toFixed(3);
        row.appendChild(cell);
      });
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
          area_cb_filter.appendChild(option_filter);
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
  isi_data();
  tampil_perbandingan.innerHTML = "";
  tampil_perbandingan.appendChild(
    create_bar(year_cb_filter.value, area_cb_filter.value)
  );
  tampil_perbandingan.appendChild(
    create_elbow(
      year_cb_filter.value,
      area_cb_filter.value,
      search_filter.value
    )
  );
};
const create_link = (year, area, search) => {
  if (search == "") search = "x";
  return `${kmeans_api}/${year}/${area}/${search}`;
};
const create_link_bar = (year, area) => {
  return `${bar_kmeans_api}/${year}/${area}`;
};
const create_bar = (year, area) => {
  const img_tampil = document.createElement("img");

  img_tampil.style.width = "100%";
  img_tampil.src = create_link_bar(year, area);
  return img_tampil;
};
const create_elbow = (year, area, search) => {
  const img_tampil = document.createElement("img");

  img_tampil.style.width = "100%";
  img_tampil.src = create_link(year, area, search);
  return img_tampil;
};
year_cb_filter.onchange = load_img;
area_cb_filter.onchange = load_img;
search_filter.onchange = load_img;
cek_year();
