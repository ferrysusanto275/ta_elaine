const instansi_cb_filter = document.getElementById("instansi_cb_filter");
const domain_cb_filter = document.getElementById("domain_cb_filter");
const year_tf_filter = document.getElementById("year_tf_filter");
const group_cb_filter = document.getElementById("group_cb_filter");
const bobot_domain = document.getElementById("bobot_domain");
const url_api = base_api_url + "isi";
const indikator_api = base_api_url + "indikator";
const instansi_api = base_api_url + "instansi";
const domain_api = base_api_url + "domain";
const gi_api = base_api_url + "grup_instansi";
const tabel_body = document.getElementById("body_data");
let domain_data = {};
let selected_domain = "";
let selected_instansi = "";
let selected_year = "";
let selected_gi = "";
const cek_gi = () => {
  fetch(gi_api)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      if (data.length == 0) {
        location.href = "grup_instansi";
      } else {
        data.forEach((element, i) => {
          let option = document.createElement("option");
          option.value = element.id;
          option.textContent = element.nama;

          group_cb_filter.appendChild(option);
          if (i == 0) selected_gi = element.id;
        });
        cek_instansi();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const cek_instansi = () => {
  fetch(`${instansi_api}/grup/${group_cb_filter.value}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      instansi_cb_filter.innerHTML = "";
      if (data.length == 0) {
        location.href = "instansi";
      } else {
        data.forEach((element, i) => {
          let option = document.createElement("option");
          option.value = element.id;
          option.textContent = element.nama;
          instansi_cb_filter.appendChild(option);
          if (i == 0) selected_instansi = element.id;
        });
        cek_indikator();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const cek_indikator = () => {
  fetch(indikator_api)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      if (data.length == 0) {
        location.href = "indikator";
      } else {
        create_option_domain();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const create_option_domain = () => {
  fetch(indikator_api + "/domain")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      data.forEach((element, i) => {
        let option = document.createElement("option");
        option.value = element.id;
        option.textContent = element.nama;
        domain_cb_filter.appendChild(option);
        if (i == 0) {
          selected_domain = element.id;
        }
      });
      handle_change_filter();
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};

const load_data = async () => {
  try {
    let res_aspek = await fetch(
      `${indikator_api}/domain/${domain_cb_filter.value}`
    );
    if (!(await res_aspek.ok)) {
      throw new Error("Network response was not ok");
    }
    let list_aspek = await res_aspek.json();
    tabel_body.innerHTML = "";
    let jml = 0;
    for (const element of list_aspek) {
      const newRow = document.createElement("tr");
      const cell1 = document.createElement("td");
      cell1.textContent = element.nama;
      newRow.appendChild(cell1);
      const cell2 = document.createElement("td");
      let na = 0;
      let res_isi = await fetch(
        url_api +
          "/aspek/" +
          instansi_cb_filter.value +
          "/" +
          element.id +
          "/" +
          year_tf_filter.value
      );
      if (!(await res_isi.ok)) {
        throw new Error("Network response was not ok");
      }
      let list_isi = (await res_isi).json();
      let jml_indikator = 0;
      (await list_isi).forEach((element) => {
        jml_indikator +=
          parseFloat(element.indikator.bobot) * parseFloat(element.value);
      });
      na = jml_indikator / parseFloat(element.bobot);
      cell2.textContent = na.toFixed(2);
      newRow.appendChild(cell2);
      const cell3 = document.createElement("td");
      cell3.textContent = element.bobot;
      newRow.appendChild(cell3);
      const cell4 = document.createElement("td");
      let NB = parseFloat(element.bobot) * na;
      jml += NB;
      cell4.textContent = NB.toFixed(2);
      newRow.appendChild(cell4);

      tabel_body.appendChild(newRow);
    }
    let newRow = document.createElement("tr");
    let cell1 = document.createElement("td");
    cell1.setAttribute("colspan", 3);
    cell1.textContent = "Jumlah NA x BA";
    newRow.appendChild(cell1);
    let cell2 = document.createElement("td");
    cell2.textContent = jml.toFixed(2);
    newRow.appendChild(cell2);
    tabel_body.appendChild(newRow);

    let newRow1 = document.createElement("tr");
    let cell11 = document.createElement("td");
    cell11.setAttribute("colspan", 3);
    cell11.textContent = `Indeks ${domain_data.name}`;
    newRow1.appendChild(cell11);
    let cell21 = document.createElement("td");
    cell21.textContent = (jml / parseFloat(domain_data.bobot)).toFixed(2);
    newRow1.appendChild(cell21);
    tabel_body.appendChild(newRow1);
  } catch (error) {
    console.error("Ada kesalahan:", error);
  }
};
const handle_change_filter = () => {
  fetch(domain_api + "/" + domain_cb_filter.value)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      domain_data = data;
      bobot_domain.textContent = domain_data.bobot;
      load_data();
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
year_tf_filter.onchange = handle_change_filter;
domain_cb_filter.onchange = handle_change_filter;
instansi_cb_filter.onchange = handle_change_filter;
group_cb_filter.onchange = cek_instansi;
cek_gi();
