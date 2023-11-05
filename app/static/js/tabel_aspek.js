const instansi_cb_filter = document.getElementById("instansi_cb_filter");
const domain_cb_filter = document.getElementById("domain_cb_filter");
const year_tf_filter = document.getElementById("year_tf_filter");
const bobot_domain = document.getElementById("bobot_domain");
const url_api = base_api_url + "isi";
const indikator_api = base_api_url + "indikator";
const instansi_api = base_api_url + "instansi";
const domain_api = base_api_url + "domain";
let domain_data = {};
let selected_domain = "";
let selected_instansi = "";
let selected_year = "";
const cek_instansi = () => {
  fetch(instansi_api)
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
cek_instansi();
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
        handle_change_filter();
      });
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};

const load_data = async () => {};
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
