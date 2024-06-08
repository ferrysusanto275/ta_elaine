const instansi_api= base_api_url + "instansi/value"
const prediksi_api= base_api_url + "prediksi"
const instansi_cb_filter = document.getElementById("instansi_cb_filter");
const cek_instansi = () => {
    fetch(instansi_api )
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        if (data.length == 0) {
          location.href = "isi";
        } else {
          data.forEach((element, i) => {
            // console.log(element);
            let option = document.createElement("option");
            option.value = element.id;
            option.textContent = element.nama;
  
            instansi_cb_filter.appendChild(option);
          });
          $("#instansi_cb_filter").select2();
  
          load_data();
        }
      })
      .catch((error) => {
        console.error("Ada kesalahan:", error);
      });
  };
  const load_data = () => {
    tampil_prediksi.innerHTML = "";
    load_img();
    load_tabel();
  };
  const load_tabel = () => {
    fetch(
      `api/prediksi/df_linear_reg/${instansi_cb_filter.value}/indeks`
    )
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        tabel.innerHTML = "";
        if (data.length > 0) {
          data.forEach((element, i) => {
            console.log(element);
            let td = document.createElement("td");
            td.innerText = element.value;
            // td.textContent = element.nama_instansi;
  
            tabel.appendChild(td);
          });
  
          // load_data()
        }
      });
  };
  const load_img = () => {
    tampil_prediksi.appendChild(
      create_png_prediksi(instansi_cb_filter.value, 'indeks')
    );
  };
  const create_link = (instansi, indikator) => {
    return `api/prediksi/png_linear_reg/${instansi}/${indikator}`;
  };
  const create_png_prediksi = (instansi, indikator) => {
    const img_tampil = document.createElement("img");
    img_tampil.src = create_link(instansi, indikator);
    return img_tampil;
  };
  cek_instansi()
  instansi_cb_filter.onchange = load_data