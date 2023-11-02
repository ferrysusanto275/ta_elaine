const url_api = base_api_url + "aspek"
const domain_api = base_api_url + "domain"
//dapetin element html
const add_btn = document.getElementById("add_btn");
const cancel_btn = document.getElementById("cancel_btn");
const submit_btn = document.getElementById("submit_btn");
const modal_form = document.getElementById("modal_form");
const id_tf = document.getElementById("id_tf");
const nama_tf = document.getElementById("nama_tf");
const bobot_tf = document.getElementById("bobot_tf");
const domain_cb = document.getElementById("domain_cb");
const domain_cb_filter = document.getElementById("domain_cb_filter");
let selected_domain = "";
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
    let url_tuju = `${url_api}/domain/${selected_domain}`;
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
                        bobot_tf.value = element.bobot
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
    nama_tf.value = "";
    bobot_tf.value = "";
}
const handle_submit = () => {
    let url_tuju = url_api;
    let data = {
        nama: nama_tf.value,
        domain: selected_domain,
        bobot: parseFloat(bobot_tf.value)
    }
    let option = {
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }
    if (id_tf.value === "") {
        //add
        option.method = 'POST'
    } else {
        //update
        option.method = 'PUT'
        url_tuju += `/${id_tf.value}`;
    }
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

}
const cek_domain = () => {
    fetch(domain_api)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
        })
        .then(data => {
            if (data.length > 0) {
                data.forEach((element, i) => {
                    let option = document.createElement('option');
                    option.value = element.id;
                    option.textContent = element.nama;
                    let option_filter = option.cloneNode(true);
                    domain_cb.appendChild(option);
                    domain_cb_filter.appendChild(option_filter);
                    if (i == 0) selected_domain = element.id;
                });
                load_data();
            } else {
                location.href = "domain"
            }
        })
        .catch(error => {
            console.error('Ada kesalahan:', error);
        });
}
const handle_filter = () => {
    if (domain_cb.value == selected_domain) {
        selected_domain = domain_cb_filter.value;
        domain_cb.value = domain_cb_filter.value;
    } else {
        selected_domain = domain_cb.value;
        domain_cb_filter.value = domain_cb.value;
    }
    load_data();
}
domain_cb.onchange = handle_filter;
domain_cb_filter.onchange = handle_filter;
submit_btn.onclick = handle_submit;
cancel_btn.onclick = handle_cancel_btn;
add_btn.onclick = handle_add_btn;
cek_domain();
// load_data();