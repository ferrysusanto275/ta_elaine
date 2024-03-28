const year_api = base_api_url + "isi/year";
const analisis_api = base_api_url + "analisis_grup";
const keluaran_api = base_api_url + "analisis"
const analisis_indikator_api = base_api_url + "analisis_indikator"
const year_cb_filter = document.getElementById('year_cb_filter')
const bagian_cb_filter = document.getElementById('bagian_cb_filter')
const inisiatif_cb_filter = document.getElementById('inisiatif_cb_filter')
const keluaran_cb_filter = document.getElementById('keluaran_cb_filter')
const indikator_cb_filter = document.getElementById('indikator_cb_filter')
const pj = document.getElementById('pj')
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
                handle_year()

            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
};
const cek_bagian = () => {
    fetch(analisis_api + "/bagian")
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
                    option.value = i;
                    option.textContent = element;

                    bagian_cb_filter.appendChild(option);
                });
                handle_bagian()

            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
}
const cek_inisiatif = () => {
    // console.log(inisiatif_cb_filter.value);
    fetch(analisis_api + "/" + bagian_cb_filter.value)
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
                    option.value = element.id;
                    option.textContent = element.nama;

                    inisiatif_cb_filter.appendChild(option);
                });
                handle_inisiatif()

            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
}
const cek_keluaran = () => {
    // console.log(inisiatif_cb_filter.value);
    fetch(keluaran_api + "/" + inisiatif_cb_filter.value)
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
                    option.value = element.id;
                    option.textContent = element.nama;
                    option.setAttribute('pj', element.penanggung_jawab)

                    keluaran_cb_filter.appendChild(option);
                });
                handle_keluaran()

            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
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
                    option.setAttribute('pj', element.penanggung_jawab)

                    indikator_cb_filter.appendChild(option);
                });
                // handle_indikator()

            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
}

const handle_year = () => {
    cek_bagian()
}
const handle_bagian = () => {
    inisiatif_cb_filter.innerHTML = "";
    cek_inisiatif()
}
const handle_inisiatif = () => {
    keluaran_cb_filter.innerHTML = "";
    cek_keluaran()
}
const handle_keluaran = () => {
    let selectedIndex = keluaran_cb_filter.selectedIndex;

    // Mendapatkan opsi yang dipilih
    let selectedOption = keluaran_cb_filter.options[selectedIndex];
    pj.value = selectedOption.getAttribute('pj')
    indikator_cb_filter.innerHTML = ""
    cek_indikator()
}

year_cb_filter.onchange = handle_year
bagian_cb_filter.onchange = handle_bagian
inisiatif_cb_filter.onchange = handle_inisiatif
keluaran_cb_filter.onchange = handle_keluaran
cek_year();