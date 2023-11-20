const gi_api = base_api_url + "grup_instansi";
const indikator_api = base_api_url + "indikator";
const aspek_api = base_api_url + "aspek";
const isi_api = base_api_url + "isi";
const group_cb_filter = document.getElementById("group_cb_filter");
const domain1_cb_filter = document.getElementById("domain1_cb_filter");
const domain2_cb_filter = document.getElementById("domain2_cb_filter");
const tampil_perbandingan = document.getElementById("tampil_perbandingan");

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
        domain1_cb_filter.appendChild(option);
        let option_filter = option.cloneNode(true);
        domain2_cb_filter.appendChild(option_filter);
        load_img();
        // create_option_aspek();
      });
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};

const load_img = () => {
  tampil_perbandingan.innerHTML = "";
  tampil_perbandingan.appendChild(
    create_perbandingan(
      group_cb_filter.value,
      domain1_cb_filter.value,
      domain2_cb_filter.value
    )
  );
};
const create_link = (grup, domain1, domain2) => {
  return `${isi_api}/kmeans_domain/${domain1}/${domain2}/grup/${grup}`;
};
const create_perbandingan = (grup, domain1, domain2) => {
  const img_tampil = document.createElement("img");
  img_tampil.src = create_link(grup, domain1, domain2);
  return img_tampil;
};
group_cb_filter.onchange = load_img;
domain1_cb_filter.onchange = load_img;
domain2_cb_filter.onchange = load_img;

cek_gi();
