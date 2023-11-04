const url_api = base_api_url + "isi"
const indikator_api = base_api_url + "indikator"
const instansi_api = base_api_url + "instansi"
//dapetin element html
const add_btn = document.getElementById("add_btn");
const cancel_btn = document.getElementById("cancel_btn");
const submit_btn = document.getElementById("submit_btn");
const modal_form = document.getElementById("modal_form");
const year_tf = document.getElementById("year_tf");
const year_tf_filter = document.getElementById("year_tf_filter");
const value_tf = document.getElementById("value_tf");
const instansi_cb = document.getElementById("instansi_cb");
const instansi_cb_filter = document.getElementById("instansi_cb_filter");
const domain_cb = document.getElementById("domain_cb");
const domain_cb_filter = document.getElementById("domain_cb_filter");
const aspek_cb = document.getElementById("aspek_cb");
const aspek_cb_filter = document.getElementById("aspek_cb_filter");
const indikator_cb = document.getElementById("indikator_cb");
let selected_aspek = "";
let selected_domain = "";
let selected_instansi = "";
let selected_year = "";
const handle_delete = (id) => {
    fetch(`${url_api}/${id}`, {
        method: 'DELETE'
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
        .then(data => {
            console.log(data);
            load_data();
        });
}
const load_data = () => {
    let url_tuju = `${url_api}/aspek/${selected_instansi}/${selected_aspek}/${selected_year}`;
    fetch(url_tuju)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
        })
        .then(data => {
            // console.log(data); // Lakukan sesuatu dengan data yang diambil
            let tabel_body = document.getElementById('body_data');
            tabel_body.innerHTML = "";
            if (data.length > 0) {
                data.forEach((element, i) => {
                    let newRow = document.createElement("tr");
                    let cell1 = document.createElement("td");
                    cell1.textContent = i + 1;
                    newRow.appendChild(cell1);
                    let cell2 = document.createElement("td");
                    cell2.textContent = element.nama;
                    newRow.appendChild(cell2)
                    let cell3 = document.createElement("td");
                    cell3.textContent = element.bobot;
                    newRow.appendChild(cell3)
                    let cell4 = document.createElement("td");
                    let btn_delete = document.createElement("button");
                    btn_delete.textContent = "Delete";
                    btn_delete.classList.add("delete_btn");
                    btn_delete.onclick = function () {
                        handle_delete(element.id);
                    }
                    let btn_edit = document.createElement("button");
                    btn_edit.textContent = "Edit";
                    btn_edit.classList.add("edit_btn");
                    btn_edit.onclick = function () {
                        // console.log(element.id)
                        id_tf.value = element.id;
                        nama_tf.value = element.nama;
                        value_tf.value = element.bobot
                        handle_add_btn();
                    }
                    cell4.appendChild(btn_edit)
                    cell4.appendChild(btn_delete)
                    newRow.appendChild(cell4)

                    tabel_body.appendChild(newRow)
                });
            } else {
                let newRow = document.createElement("tr");
                let cell1 = document.createElement("td")
                cell1.setAttribute('colspan', 3)
                cell1.textContent = "No Data"
                cell1.classList.add("text_center");
                newRow.appendChild(cell1);
                tabel_body.appendChild(cell1)
            }
        })
        .catch(error => {
            console.error('Ada kesalahan:', error);
        });
}
const handle_add_btn = () => {
    modal_form.style.display = "flex";
}
const handle_cancel_btn = () => {
    modal_form.style.display = "none";
    clear_modal_form();
}
const clear_modal_form = () => {
    id_tf.value = "";
    value_tf.value = "";
}
const handle_submit = async () => {
    try {
        let url_id = `${url_api}/${selected_instansi}/${indikator_cb.value}/${year_tf.value}`
        let url_tuju = url_api;
        let data = {
            value: parseFloat(value_tf.value)
        }
        let option = {
            headers: {
                'Content-Type': 'application/json',
            }
        }
        let response = await fetch(url_id);
        if (!response.ok) {
            //add
            data.instansi = selected_instansi;
            data.indikator = indikator_cb.value;
            data.year = parseFloat(year_tf.value);
            option.method = 'POST'
        } else {
            //update
            option.method = 'PUT'
            url_tuju = url_id;
        }
        option.body = JSON.stringify(data)
        fetch(url_tuju, option).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
        })
            .then(data => {
                console.log(data);
                load_data();
                handle_cancel_btn();
            });
        if (listdata.length > 0) {

        }
    } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
    }



}
const cek_indikator = () => {
    fetch(indikator_api)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
        })
        .then(data => {
            if (data.length == 0) {
                location.href = "indikator"
            } else {
                create_option_domain();
            }
        })
        .catch(error => {
            console.error('Ada kesalahan:', error);
        });
}
const cek_instansi = () => {
    fetch(instansi_api)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
        })
        .then(data => {
            if (data.length == 0) {
                location.href = "indikator"
            } else {
                data.forEach((element, i) => {
                    let option = document.createElement('option');
                    option.value = element.id;
                    option.textContent = element.nama;
                    let option_filter = option.cloneNode(true);
                    instansi_cb.appendChild(option);
                    instansi_cb_filter.appendChild(option_filter);
                    if (i == 0) selected_instansi = element.id;
                });
                cek_indikator();
            }
        })
        .catch(error => {
            console.error('Ada kesalahan:', error);
        });
}
const create_option_indikator = () => {
    fetch(indikator_api + "/aspek/" + selected_aspek).then((response) => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then((data) => {
        indikator_cb.innerHTML = "";
        data.forEach((element, i) => {
            let option = document.createElement('option');
            option.value = element.id;
            option.textContent = element.nama;
            indikator_cb.appendChild(option);
        });
    }).catch(error => {
        console.error('Ada kesalahan:', error);
    });
}
const create_option_aspek = () => {
    fetch(indikator_api + "/domain/" + selected_domain).then((response) => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then((data) => {
        aspek_cb.innerHTML = "";
        aspek_cb_filter.innerHTML = "";
        data.forEach((element, i) => {
            let option = document.createElement('option');
            option.value = element.id;
            option.textContent = element.nama;
            let option_filter = option.cloneNode(true);
            aspek_cb.appendChild(option);
            aspek_cb_filter.appendChild(option_filter);
            if (i == 0) selected_aspek = element.id;
            create_option_indikator()
        });
    }).catch(error => {
        console.error('Ada kesalahan:', error);
    });
}
const create_option_domain = () => {
    fetch(indikator_api + "/domain").then((response) => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then((data) => {
        data.forEach((element, i) => {
            let option = document.createElement('option');
            option.value = element.id;
            option.textContent = element.nama;
            let option_filter = option.cloneNode(true);
            domain_cb.appendChild(option);
            domain_cb_filter.appendChild(option_filter);
            if (i == 0) selected_domain = element.id;
            create_option_aspek()
        });
    }).catch(error => {
        console.error('Ada kesalahan:', error);
    });
}
const handle_filter_domain = () => {
    if (domain_cb.value == selected_domain) {
        selected_domain = domain_cb_filter.value;
        domain_cb.value = domain_cb_filter.value;
    } else {
        selected_domain = domain_cb.value;
        domain_cb_filter.value = domain_cb.value;
    }
    create_option_aspek();
}
const handle_filter_aspek = () => {
    if (aspek_cb.value == selected_aspek) {
        selected_aspek = aspek_cb_filter.value;
        aspek_cb.value = aspek_cb_filter.value;
    } else {
        selected_aspek = aspek_cb.value;
        aspek_cb_filter.value = aspek_cb.value;
    }
    create_option_indikator();
    load_data();
}
const handle_filter_instansi = () => {
    if (instansi_cb.value == selected_instansi) {
        selected_instansi = instansi_cb_filter.value;
        instansi_cb.value = instansi_cb_filter.value;
    } else {
        selected_instansi = instansi_cb.value;
        instansi_cb_filter.value = instansi_cb.value;
    }
    load_data();
}
const handle_filter_year = () => {
    if (year_cb.value == selected_year) {
        selected_year = year_cb_filter.value;
        year_cb.value = year_cb_filter.value;
    } else {
        selected_year = year_cb.value;
        year_cb_filter.value = year_cb.value;
    }
    load_data();
}
domain_cb.onchange = handle_filter_domain;
domain_cb_filter.onchange = handle_filter_domain;
aspek_cb.onchange = handle_filter_aspek;
aspek_cb_filter.onchange = handle_filter_aspek;
instansi_cb.onchange = handle_filter_instansi;
instansi_cb_filter.onchange = handle_filter_instansi;
year_tf.onchange = handle_filter_year;
year_tf_filter.onchange = handle_filter_year;
submit_btn.onclick = handle_submit;
cancel_btn.onclick = handle_cancel_btn;
add_btn.onclick = handle_add_btn;
cek_instansi();

// load_data();