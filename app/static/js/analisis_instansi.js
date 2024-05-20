const url_api = base_api_url + "analisis_instansi";
const instansi_api = base_api_url + "instansi";
const area_api = base_api_url + "area";
const inisiatif_api = base_api_url + "analisis_grup";
const keluaran_api = base_api_url + "analisis";
const indikator_api = base_api_url + "indikator";
const gi_api = base_api_url + "grup_instansi";
//dapetin element html
const add_btn = document.getElementById("add_btn");
const cancel_btn = document.getElementById("cancel_btn");
const submit_btn = document.getElementById("submit_btn");
const modal_form = document.getElementById("modal_form");
const area_cb = document.getElementById("area_cb");
const keluaran_cb = document.getElementById("keluaran_cb");
const indikator_cb = document.getElementById("indikator_cb");
const inisiatif_cb = document.getElementById("inisiatif_cb");
const inisiatif_cb_filter = document.getElementById("inisiatif_cb_filter");
const area_cb_filter = document.getElementById("area_cb_filter");
const keluaran_cb_filter = document.getElementById("keluaran_cb_filter");
const grup_instansi_cb = document.getElementById("grup_instansi_cb");

let selected_area = "";
let selected_inisiatif = "";
let selected_keluaran = "";
const handle_delete = (analisis, instansi) => {
  fetch(`${url_api}/${analisis}/${instansi}`, {
    method: "DELETE",
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      console.log(data);
      load_data();
    });
};
const load_data = () => {
  let url_tuju = `${url_api}/${selected_keluaran}`;
  fetch(url_tuju)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      // console.log(data); // Lakukan sesuatu dengan data yang diambil
      let tabel_body = document.getElementById("body_data");
      tabel_body.innerHTML = "";
      if (data.length > 0) {
        data.forEach((element, i) => {
          let newRow = document.createElement("tr");
          let cell1 = document.createElement("td");
          cell1.textContent = i + 1;
          newRow.appendChild(cell1);
          let cell2 = document.createElement("td");
          cell2.textContent = element.nama_instansi;
          newRow.appendChild(cell2);
          let cell4 = document.createElement("td");
          let btn_delete = document.createElement("button");
          btn_delete.textContent = "Delete";
          btn_delete.classList.add("delete_btn");
          btn_delete.onclick = function () {
            handle_delete(element.analisis, element.instansi);
          };
          cell4.appendChild(btn_delete);
          newRow.appendChild(cell4);

          tabel_body.appendChild(newRow);
        });
      } else {
        let newRow = document.createElement("tr");
        let cell1 = document.createElement("td");
        cell1.setAttribute("colspan", 3);
        cell1.textContent = "No Data";
        cell1.classList.add("text_center");
        newRow.appendChild(cell1);
        tabel_body.appendChild(cell1);
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const handle_add_btn = () => {
  modal_form.style.display = "flex";
  create_option_gi();
};
const create_option_gi = () => {
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
          // let option_filter = option.cloneNode(true);

          grup_instansi_cb.appendChild(option);
        });
        create_option_instansi();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};

const create_option_instansi = () => {
  fetch(instansi_api + "/grup/" + grup_instansi_cb.value)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      instansi_cb.innerHTML = "";
      data.forEach((element, i) => {
        let option = document.createElement("option");
        option.value = element.id;
        option.textContent = element.nama;
        instansi_cb.appendChild(option);
      });
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};

const handle_cancel_btn = () => {
  modal_form.style.display = "none";
  clear_modal_form();
};
const clear_modal_form = () => {
  instansi_cb.value = "in2023110400001";
};
const handle_submit = () => {
  let url_tuju = url_api;
  let data = {
    analisis: keluaran_cb.value,
    instansi: instansi_cb.value,
  };
  let option = {
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
    method: "POST",
  };
  // if (id_tf.value === "") {
  //     //add
  //     option.method = 'POST'
  // } else {
  //     //update
  //     option.method = 'PUT'
  //     url_tuju += `/${id_tf.value}`;
  // }
  fetch(url_tuju, option)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      console.log(data);
      load_data();
      handle_cancel_btn();
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
          area_cb.appendChild(option);
          area_cb_filter.appendChild(option_filter);
          if (i == 0) selected_area = element.id;
        });
        cek_inisiatif();
        // load_data();
      } else {
        location.href = "area";
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const cek_inisiatif = () => {
  fetch(`${inisiatif_api}/area/${selected_area}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      if (data.length > 0) {
        inisiatif_cb.innerHTML = "";
        inisiatif_cb_filter.innerHTML = "";
        data.forEach((element, i) => {
          let option = document.createElement("option");
          option.value = element.id;
          option.textContent = element.id + ". " + element.nama;
          let option_filter = option.cloneNode(true);
          inisiatif_cb.appendChild(option);
          inisiatif_cb_filter.appendChild(option_filter);
          if (i == 0) selected_inisiatif = element.id;
        });
        cek_keluaran();
      } else {
        location.href = "area";
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const cek_keluaran = () => {
  keluaran_cb_filter.innerHTML = "";
  keluaran_cb_filter.innerHTML = "";
  // console.log("masuk");
  fetch(`${keluaran_api}/inisiatif/${selected_inisiatif}`)
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
          option.textContent = `${i + 1}. ${element.nama}`;
          let option_filter = option.cloneNode(true);
          keluaran_cb.appendChild(option);
          keluaran_cb_filter.appendChild(option_filter);
          if (i == 0) selected_keluaran = element.id;
        });
        load_data();
      } else {
        location.href = "area";
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const handle_filter = () => {
  if (area_cb.value == selected_area) {
    selected_area = area_cb_filter.value;
    area_cb.value = area_cb_filter.value;
  } else {
    selected_area = area_cb.value;
    area_cb_filter.value = area_cb.value;
  }
  inisiatif_cb_filter.innerHTML = "";
  inisiatif_cb.innerHTML = "";
  cek_inisiatif();
};
const handle_filter_inisiatif = () => {
  if (inisiatif_cb.value == selected_inisiatif) {
    selected_inisiatif = inisiatif_cb_filter.value;
    inisiatif_cb.value = inisiatif_cb_filter.value;
  } else {
    selected_inisiatif = inisiatif_cb.value;
    inisiatif_cb_filter.value = inisiatif_cb.value;
  }
  keluaran_cb_filter.innerHTML = "";
  keluaran_cb.innerHTML = "";
  cek_keluaran();
  // load_data();
};
const handle_filter_keluaran = () => {
  if (keluaran_cb.value == selected_keluaran) {
    selected_keluaran = keluaran_cb_filter.value;
    keluaran_cb.value = keluaran_cb_filter.value;
  } else {
    selected_keluaran = keluaran_cb.value;
    keluaran_cb_filter.value = keluaran_cb.value;
  }
  load_data();
};

grup_instansi_cb.onchange = create_option_instansi;
area_cb.onchange = handle_filter;
area_cb_filter.onchange = handle_filter;
inisiatif_cb.onchange = handle_filter_inisiatif;
inisiatif_cb_filter.onchange = handle_filter_inisiatif;
submit_btn.onclick = handle_submit;
cancel_btn.onclick = handle_cancel_btn;
add_btn.onclick = handle_add_btn;
keluaran_cb_filter.onchange = handle_filter_keluaran;
keluaran_cb.onchange = handle_filter_keluaran;
cek_area();
// load_data();
