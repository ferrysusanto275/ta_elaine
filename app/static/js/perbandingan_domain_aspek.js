// const gi_api = base_api_url + "grup_instansi";
const indikator_api = base_api_url + "indikator";
const aspek_api = base_api_url + "aspek";
const isi_api = base_api_url + "isi";
// const group_cb_filter = document.getElementById("group_cb_filter");
const domain1_cb_filter = document.getElementById("domain1_cb_filter");
const domain2_cb_filter = document.getElementById("domain2_cb_filter");
const aspek2_cb_filter = document.getElementById("aspek2_cb_filter");
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
                create_option_domain();
            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
};

const handle_domain2 = () => {
    fetch(indikator_api + "/domain/" + domain2_cb_filter.value)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            aspek2_cb_filter.innerHTML = "";
            data.forEach((element, i) => {
                let option = document.createElement("option");
                option.value = element.id;
                option.textContent = element.nama;
                aspek2_cb_filter.appendChild(option);
                load_img();
            });
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
                handle_domain2();
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
            // group_cb_filter.value,
            domain1_cb_filter.value,
            aspek2_cb_filter.value
        )
    );
};
const create_link = (domain, aspek) => {
    return `${isi_api}/domain_aspek/${domain}/${aspek}`;
};
const create_perbandingan = (domain, aspek) => {
    const img_tampil = document.createElement("img");
    img_tampil.src = create_link(domain, aspek);
    return img_tampil;
};
// group_cb_filter.onchange = load_img;
domain1_cb_filter.onchange = load_img;
domain2_cb_filter.onchange = handle_domain2;
aspek2_cb_filter.onchange = load_img;

cek_indikator();
