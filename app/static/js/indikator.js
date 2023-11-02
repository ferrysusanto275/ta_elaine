const url_api = base_api_url + "indikator"
const aspek_api = base_api_url + "aspek"
//dapetin element html
const add_btn = document.getElementById("add_btn");
const cancel_btn = document.getElementById("cancel_btn");
const submit_btn = document.getElementById("submit_btn");
const modal_form = document.getElementById("modal_form");
const id_tf = document.getElementById("id_tf");
const nama_tf = document.getElementById("nama_tf");
const bobot_tf = document.getElementById("bobot_tf");
const aspek_cb = document.getElementById("aspek_cb");
const aspek_cb_filter = document.getElementById("aspek_cb_filter");
let selected_aspek = "";
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
    let url_tuju = `${url_api}/aspek/${selected_aspek}`;
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
        aspek: selected_aspek,
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
const cek_aspek = () => {
    fetch(aspek_api)
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
                    aspek_cb.appendChild(option);
                    aspek_cb_filter.appendChild(option_filter);
                    if (i == 0) selected_aspek = element.id;
                });
                load_data();
            } else {
                location.href = "aspek"
            }
        })
        .catch(error => {
            console.error('Ada kesalahan:', error);
        });
}
const handle_filter = () => {
    if (aspek_cb.value == selected_aspek) {
        selected_aspek = aspek_cb_filter.value;
        aspek_cb.value = aspek_cb_filter.value;
    } else {
        selected_aspek = aspek_cb.value;
        aspek_cb_filter.value = aspek_cb.value;
    }
    load_data();
}
aspek_cb.onchange = handle_filter;
aspek_cb_filter.onchange = handle_filter;
submit_btn.onclick = handle_submit;
cancel_btn.onclick = handle_cancel_btn;
add_btn.onclick = handle_add_btn;
cek_aspek();
// load_data();