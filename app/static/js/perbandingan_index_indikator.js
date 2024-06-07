// const gi_api = base_api_url + "grup_instansi";
const indikator_api = base_api_url + "indikator";
const aspek_api = base_api_url + "aspek";
const isi_api = base_api_url + "isi";
// const group_cb_filter = document.getElementById("group_cb_filter");
const domain_cb_filter = document.getElementById("domain_cb_filter");
const aspek_cb_filter = document.getElementById("aspek_cb_filter");
const indikator_cb_filter = document.getElementById("indikator_cb_filter");
const tampil_perbandingan = document.getElementById("tampil_perbandingan");

// const cek_gi = () => {
//     fetch(gi_api)
//         .then((response) => {
//             if (!response.ok) {
//                 throw new Error("Network response was not ok");
//             }
//             return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
//         })
//         .then((data) => {
//             if (data.length == 0) {
//                 location.href = "grup_instansi";
//             } else {
//                 data.forEach((element, i) => {
//                     let option = document.createElement("option");
//                     option.value = element.id;
//                     option.textContent = element.nama;

//                     group_cb_filter.appendChild(option);
//                 });
//                 cek_indikator();
//             }
//         })
//         .catch((error) => {
//             console.error("Ada kesalahan:", error);
//         });
// };
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
        domain_cb_filter.innerHTML = "";
        domain_cb.innerHTML = "";
        create_option_domain();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const handle_aspek = () => {
  fetch(indikator_api + "/aspek/" + aspek_cb_filter.value)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      indikator_cb_filter.innerHTML = "";
      data.forEach((element, i) => {
        let option = document.createElement("option");
        option.value = element.id;
        option.textContent = element.nama;
        indikator_cb_filter.appendChild(option);
      });
      load_img();
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const handle_domain = () => {
  fetch(indikator_api + "/domain/" + domain_cb_filter.value)
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
      });
      handle_aspek();
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
      });
      handle_domain();
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};

const load_img = () => {
  tampil_perbandingan.innerHTML = "";
  tampil_perbandingan.appendChild(
    create_perbandingan(
      // group_cb_filter.value,
      indikator_cb_filter.value
    )
  );
};
const create_link = (indikator) => {
  return `${isi_api}/index_indikator/${indikator}`;
};
const create_perbandingan = (indikator) => {
  const img_tampil = document.createElement("img");
  img_tampil.src = create_link(indikator);
  return img_tampil;
};
// group_cb_filter.onchange = load_img;
domain_cb_filter.onchange = handle_domain;
aspek_cb_filter.onchange = handle_aspek;
indikator_cb_filter.onchange = load_img;

cek_indikator();
