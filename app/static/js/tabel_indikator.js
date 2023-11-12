const instansi_cb_filter = document.getElementById("instansi_cb_filter");
const domain_cb_filter = document.getElementById("domain_cb_filter");
const aspek_cb_filter = document.getElementById("aspek_cb_filter");
const year_tf_filter = document.getElementById("year_tf_filter");
const group_cb_filter = document.getElementById("group_cb_filter");
const bobot_aspek = document.getElementById("bobot_aspek");
const url_api = base_api_url + "isi";
const indikator_api = base_api_url + "indikator";
const instansi_api = base_api_url + "instansi";
const aspek_api = base_api_url + "aspek";
const gi_api = base_api_url + "grup_instansi";
let selected_gi = "";
let selected_aspek = "";
let selected_domain = "";
let selected_instansi = "";
let selected_year = "";
let aspek_data = {};
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
        if (i == 0) selected_domain = element.id;
        create_option_aspek();
      });
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const create_option_aspek = () => {
  fetch(indikator_api + "/domain/" + selected_domain)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      aspek_cb_filter.innerHTML = "";
      data.forEach((element, i) => {
        let option = document.createElement("option");
        option.value = element.id;
        option.textContent = element.nama;
        aspek_cb_filter.appendChild(option);
        if (i == 0) selected_aspek = element.id;
        handle_filter_aspek();
      });
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const load_data = () => {
  fetch(
    url_api +
      "/aspek/" +
      instansi_cb_filter.value +
      "/" +
      aspek_cb_filter.value +
      "/" +
      year_tf_filter.value
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      let tabel_body = document.getElementById("body_data");
      tabel_body.innerHTML = "";
      if (data.length > 0) {
        let jumlah = 0;
        data.forEach((element) => {
          let newRow = document.createElement("tr");
          let cell1 = document.createElement("td");
          cell1.textContent = element.indikator.name;
          // console.log(element.indikator);
          newRow.appendChild(cell1);
          let cell2 = document.createElement("td");
          cell2.textContent = element.value;
          newRow.appendChild(cell2);
          let cell3 = document.createElement("td");
          cell3.textContent = element.indikator.bobot;
          newRow.appendChild(cell3);
          jumlah +=
            parseFloat(element.indikator.bobot) * parseFloat(element.value);
          let cell4 = document.createElement("td");
          cell4.textContent = (
            parseFloat(element.indikator.bobot) * parseFloat(element.value)
          ).toFixed(2);
          newRow.appendChild(cell4);
          tabel_body.appendChild(newRow);
        });
        let newRow = document.createElement("tr");
        let cell1 = document.createElement("td");
        cell1.setAttribute("colspan", 3);
        cell1.textContent = "Jumlah NI x BI";
        newRow.appendChild(cell1);
        let cell2 = document.createElement("td");
        cell2.textContent = jumlah.toFixed(2);
        newRow.appendChild(cell2);
        tabel_body.appendChild(newRow);

        let newRow1 = document.createElement("tr");
        let cell11 = document.createElement("td");
        cell11.setAttribute("colspan", 3);
        cell11.textContent = `Indeks ${aspek_data.name}`;
        console.log(aspek_data);
        newRow1.appendChild(cell11);
        let cell21 = document.createElement("td");
        cell21.textContent = (jumlah / parseFloat(aspek_data.bobot)).toFixed(2);
        newRow1.appendChild(cell21);
        tabel_body.appendChild(newRow1);
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const handle_filter_domain = () => {
  selected_domain = domain_cb_filter.value;
  create_option_aspek();
};
const handle_filter_aspek = () => {
  fetch(aspek_api + "/" + aspek_cb_filter.value)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      aspek_data = data;
      bobot_aspek.innerHTML = aspek_data.bobot;
      load_data();
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};

year_tf_filter.onchange = handle_filter_aspek;
aspek_cb_filter.onchange = handle_filter_aspek;
domain_cb_filter.onchange = handle_filter_domain;
instansi_cb_filter.onchange = handle_filter_aspek;
group_cb_filter.onchange = cek_instansi;
cek_gi();
