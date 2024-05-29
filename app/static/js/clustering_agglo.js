const year_api = base_api_url + "isi/year";
const mode_filter = document.getElementById("mode_filter");
const year_cb_filter = document.getElementById("year_cb_filter");
const linkage_cb_filter = document.getElementById("linkage_cb_filter");
const area_cb_filter = document.getElementById("area_cb_filter");
const domain_div = document.getElementById("domain_div");
const aspek_div = document.getElementById("aspek_div");
const indeks_div = document.getElementById("indeks_div");
const search = document.getElementById("search");
const chk = document.getElementById("chk");
const head_data = document.getElementById("head_data");
const body_data = document.getElementById("body_data");
const indikator_api = base_api_url + "indikator";
const aspek_api = base_api_url + "aspek";
const res_kmeans_api = base_api_url + "analisis/res_agglo";
const keluaran_indikator_api = base_api_url + "analisis/indikator";
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
        // handle_year()
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
        cek_domain();
        // load_data();
      } else {
        location.href = "area";
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const cek_domain = () => {
  if (area_cb_filter.value == 0) {
    domain_div.style.display = "block";
  } else {
    domain_div.style.display = "none";
  }
  cek_aspek();
};

area_cb_filter.onchange = cek_domain;
const cek_aspek = () => {
  if (area_cb_filter.value == 0) {
    aspek_div.style.display = "block";
  } else {
    aspek_div.style.display = "none";
  }

  chkIndeks();
};
const chkIndeks = () => {
  if (area_cb_filter.value == 0) {
    indeks_div.style.display = "block";
  } else {
    indeks_div.style.display = "none";
  }
  load_data();
};
const load_data = () => {
  create_head();
  create_body();
};
async function fetchDataIndikator() {
  try {
    const response = await fetch(
      `${keluaran_indikator_api}/${area_cb_filter.value}`
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data_indikator = await response.json();
    return data_indikator;
  } catch (error) {
    console.error("Error fetching data:", error);
    // Handle the error here if needed
    return null;
  }
}

const create_head = async () => {
  head_data.innerHTML = "";
  const newRow = document.createElement("tr");
  const cell1 = document.createElement("th");
  cell1.textContent = "No";
  newRow.appendChild(cell1);
  const cell2 = document.createElement("th");
  cell2.textContent = "Nama Instansi";
  newRow.appendChild(cell2);
  // const cell3 = document.createElement("td");
  // cell3.textContent = "Grup Instansi";
  // newRow.appendChild(cell3);
  if (area_cb_filter.value == 0) {
    const domains_chk = document.querySelectorAll(".domain_chk");
    domains_chk.forEach((domain_chk) => {
      if (domain_chk.checked) {
        const cell4 = document.createElement("th");
        cell4.textContent = domain_chk.getAttribute("data-name");
        newRow.appendChild(cell4);
      }
    });
    const aspeks_chk = document.querySelectorAll(".aspek_chk");
    aspeks_chk.forEach((aspek_chk) => {
      if (aspek_chk.checked) {
        const cell4 = document.createElement("th");
        cell4.textContent = aspek_chk.getAttribute("data-name");
        newRow.appendChild(cell4);
      }
    });
  }
  const indikator = document.getElementById("indikator");
  if (indikator.checked) {
    if (area_cb_filter.value != 0) {
      let data_indikator = await fetchDataIndikator();
      data_indikator.forEach((element_indikator) => {
        const cell4 = document.createElement("th");
        cell4.textContent = element_indikator.toUpperCase();
        newRow.appendChild(cell4);
      });
    } else {
      for (let i = 1; i <= 47; i++) {
        const cell4 = document.createElement("th");
        cell4.textContent = `I${i}`;
        newRow.appendChild(cell4);
      }
    }
  }
  if (area_cb_filter.value == 0) {
    const indeks = document.getElementById("indeks");
    if (indeks.checked) {
      const cell6 = document.createElement("th");
      cell6.textContent = "Indeks";
      newRow.appendChild(cell6);
    }
  }

  const cell5 = document.createElement("th");
  cell5.textContent = "Cluster";
  newRow.appendChild(cell5);
  head_data.appendChild(newRow);
};
const loadDataFrame = async () => {
  api_bobot=""
  if(mode_filter.value==1)api_bobot="_bobot"
  try {
    const response = await fetch(
      `${res_kmeans_api}${api_bobot}/${area_cb_filter.value}/${year_cb_filter.value}/${linkage_cb_filter.value}`
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching data:", error);
    // Handle the error here if needed
    return null;
  }
};
const create_body = async () => {
  data_indikator = await fetchDataIndikator();
  data = await loadDataFrame();
  body_data.innerHTML = "";
  data.forEach((element, i) => {
    const newRow = document.createElement("tr");
    const cell1 = document.createElement("td");
    cell1.textContent = i + 1;
    newRow.appendChild(cell1);
    const cell2 = document.createElement("td");
    cell2.textContent = element.nama;
    newRow.appendChild(cell2);
    if (area_cb_filter.value == 0) {
      const domains_chk = document.querySelectorAll(".domain_chk");
      domains_chk.forEach((domain_chk) => {
        if (domain_chk.checked) {
          const cell4 = document.createElement("td");
          cell4.textContent = element[domain_chk.id].toFixed(2);
          newRow.appendChild(cell4);
        }
      });
      const aspeks_chk = document.querySelectorAll(".aspek_chk");
      aspeks_chk.forEach((aspek_chk) => {
        if (aspek_chk.checked) {
          const cell4 = document.createElement("td");
          cell4.textContent = element[aspek_chk.id].toFixed(2);
          newRow.appendChild(cell4);
        }
      });
    }
    const indikator = document.getElementById("indikator");
    if (indikator.checked) {
      console.log(area_cb_filter.value);
      if (area_cb_filter.value != 0) {
        // let data_indikator = await fetchDataIndikator();
        data_indikator.forEach((element_indikator) => {
          const cell4 = document.createElement("td");
          cell4.textContent = element[element_indikator];
          newRow.appendChild(cell4);
        });
      } else {
        for (let i = 1; i <= 47; i++) {
          const cell4 = document.createElement("td");
          cell4.textContent = element[`i${i}`];
          newRow.appendChild(cell4);
        }
      }
    }
    if (area_cb_filter.value == 0) {
      const indeks = document.getElementById("indeks");
      if (indeks.checked) {
        const cell6 = document.createElement("td");
        cell6.textContent = element["indeks"].toFixed(2);
        newRow.appendChild(cell6);
      }
    }
    const cell5 = document.createElement("td");
    cell5.textContent = element.Cluster;
    newRow.appendChild(cell5);
    if (element.nama.toLowerCase().includes(search.value))
      body_data.appendChild(newRow);
  });
};
year_cb_filter.onchange = load_data;
linkage_cb_filter.onchange = load_data;
mode_filter.onchange=load_data
cek_year();
