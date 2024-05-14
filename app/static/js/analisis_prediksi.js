const year_api = base_api_url + "isi/year";
const df23_api = base_api_url + "isi/get_df23";
const analisis_api = base_api_url + "analisis_prediksi/area";
const instansi_api = base_api_url + "analisis_instansi";
const keluaran_api = base_api_url + "analisis"
const area_api = base_api_url + "area"
const inisiatif_api = base_api_url + "analisis_grup"

const analisis_indikator_api = base_api_url + "analisis_indikator"
const area_cb_filter = document.getElementById('area_cb_filter')
const bagian_cb_filter = document.getElementById('bagian_cb_filter')
const inisiatif_cb_filter = document.getElementById('inisiatif_cb_filter')
const keluaran_cb_filter = document.getElementById('keluaran_cb_filter')
const indikator_cb_filter = document.getElementById('indikator_cb_filter')
const instansi_cb_filter = document.getElementById('instansi_cb_filter')
const baik_cb_filter = document.getElementById('baik_cb_filter')
const body_data = document.getElementById('body_data')
const tampil_prediksi=document.getElementById('tampil_prediksi')
const pj = document.getElementById('pj')
const tt = document.getElementById('tt')
const tabel = document.getElementById('tabel')
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
        //   inisiatif_cb.innerHTML=""
          inisiatif_cb_filter.innerHTML=""
          data.forEach((element, i) => {
            let option = document.createElement("option");
            option.value = element.id;
            option.textContent = element.id + ". " + element.nama;
            let option_filter = option.cloneNode(true);
            // inisiatif_cb.appendChild(option);
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
    
    keluaran_cb_filter.innerHTML=""
    fetch(`${keluaran_api}/inisiatif/${inisiatif_cb_filter.value}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
      })
      .then((data) => {
        if (data.length > 0) {
          data.forEach((element, i) => {
            console.log(element);
            let option = document.createElement("option");
            option.value = element.id;
            option.textContent = element.nama;
            
            option.setAttribute('pj', element.penanggung_jawab)
            option.setAttribute('tt', element.target_tahun)
            let option_filter = option.cloneNode(true);
            // keluaran_cb.appendChild(option);
            keluaran_cb_filter.appendChild(option_filter);
            if (i == 0) selected_keluaran = element.id;
          });
          handle_keluaran()
        } else {
          location.href = "area";
        }
      })
      .catch((error) => {
        console.error("Ada kesalahan:", error);
      });
  };
  const handle_keluaran = () => {
    let selectedIndex = keluaran_cb_filter.selectedIndex;
    // Mendapatkan opsi yang dipilih
    let selectedOption = keluaran_cb_filter.options[selectedIndex];
    pj.value = selectedOption.getAttribute('pj')
    console.log(selectedOption.getAttribute('pj'))
    tt.value = selectedOption.getAttribute('tt')
    indikator_cb_filter.innerHTML = ""
    instansi_cb_filter.innerHTML = ""
    cek_indikator()
}
const cek_indikator = () => {
    // console.log(inisiatif_cb_filter.value);
    fetch(analisis_indikator_api + "/" + keluaran_cb_filter.value)
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
                    option.value = element.indikator;
                    option.textContent = element.nama_indikator;

                    indikator_cb_filter.appendChild(option);
                });
                
                cek_instansi()
                // load_data()

            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
}
const cek_instansi=()=>{
    fetch(instansi_api + "/" + keluaran_cb_filter.value)
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
                    // console.log(element);
                    let option = document.createElement("option");
                    option.value = element.instansi;
                    option.textContent = element.nama_instansi;

                    instansi_cb_filter.appendChild(option);
                });
                $('#instansi_cb_filter').select2();
                
                load_data()

            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
}
const load_data=()=>{
    tampil_prediksi.innerHTML = "";
    load_img()
    load_tabel()
}
const load_tabel=()=>{
    fetch(`api/prediksi/df_linear_reg/${instansi_cb_filter.value}/${indikator_cb_filter.value}`)
    .then((response) => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
        tabel.innerHTML=""
        if (data.length > 0) {
        
            data.forEach((element, i) => {
                // console.log(element);
                let td = document.createElement("td");
                td.innerText = element.value;
                // td.textContent = element.nama_instansi;

                tabel.appendChild(td);
            });
            
            load_data()

        }
    })

}
const load_img = () => {
    
    tampil_prediksi.appendChild(
        create_png_prediksi(
            instansi_cb_filter.value,indikator_cb_filter.value
        )
    );
};
const create_link = (instansi,indikator) => {
    return `api/prediksi/png_linear_reg/${instansi}/${indikator}`;
};
const create_png_prediksi = (instansi,indikator) => {
    const img_tampil = document.createElement("img");
    img_tampil.src = create_link(instansi,indikator);
    return img_tampil;
};
area_cb_filter.onchange=cek_inisiatif
inisiatif_cb_filter.onchange=cek_keluaran
keluaran_cb_filter.onchange=handle_keluaran
indikator_cb_filter.onchange=load_data
instansi_cb_filter.onchange=load_data
cek_area()
