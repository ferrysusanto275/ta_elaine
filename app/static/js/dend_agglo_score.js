const score_api = base_api_url + "isi/agglo_score";
const mode_filter = document.getElementById("mode_filter");
const year_api = base_api_url + "isi/year";
const agglo_api = base_api_url + "isi/plot_dend";
const area_api = base_api_url + "area";
const data_score = document.getElementById("data_score");
const year_cb_filter = document.getElementById("year_cb_filter");
const linkage_cb_filter = document.getElementById("linkage_cb_filter");
const area_cb_filter = document.getElementById("area_cb_filter");
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
          area_cb_filter.appendChild(option_filter);
        });
        handle_year();
        // load_data();
      } else {
        location.href = "area";
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const handle_year = () => {
  load_img();
  isi_data();
};
const isi_data = () => {
  data_score.innerHTML = "";
  fetch(
    score_api +
      "/" +
      year_cb_filter.value +
      "/" +
      linkage_cb_filter.value +
      "/" +
      area_cb_filter.value
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      data.forEach((element, i) => {
        const newRow = document.createElement("tr");
        const cell1 = document.createElement("td");
        cell1.textContent = i + 2;
        newRow.appendChild(cell1);
        const cell2 = document.createElement("td");
        cell2.textContent = element;
        newRow.appendChild(cell2);
        data_score.appendChild(newRow);
      });
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const load_img = () => {
  tampil_perbandingan.innerHTML = "";
  tampil_perbandingan.appendChild(
    create_elbow(
      year_cb_filter.value,
      linkage_cb_filter.value,
      area_cb_filter.value
    )
  );
};
const create_link = (year, linkage, area) => {
 
  return `${agglo_api}/${year}/${linkage}/${area}/${mode_filter.value}`;
};
const create_elbow = (year, linkage, area) => {
  const img_tampil = document.createElement("img");
  img_tampil.src = create_link(year, linkage, area);
  return img_tampil;
};
year_cb_filter.onchange = handle_year;
linkage_cb_filter.onchange = handle_year;
area_cb_filter.onchange = handle_year;
mode_filter.onchange=handle_year
cek_year();
