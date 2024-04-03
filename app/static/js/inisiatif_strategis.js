const url_api = base_api_url + "analisis_grup"
const area_api = base_api_url + "area"
//dapetin element html
const add_btn = document.getElementById("add_btn");
const cancel_btn = document.getElementById("cancel_btn");
const submit_btn = document.getElementById("submit_btn");
const modal_form = document.getElementById("modal_form");
const id_tf = document.getElementById("id_tf");
const nama_tf = document.getElementById("nama_tf");
const area_cb = document.getElementById("area_cb");
const area_cb_filter = document.getElementById("area_cb_filter");
let selected_area = "";
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
    let url_tuju = `${url_api}/area/${selected_area}`;
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
                    cell1.textContent = element.id;
                    newRow.appendChild(cell1);
                    let cell2 = document.createElement("td");
                    cell2.textContent = element.nama;
                    newRow.appendChild(cell2)
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
}
const handle_submit = () => {
    let url_tuju = url_api;
    let data = {
        nama: nama_tf.value,
        grup: selected_area,
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
const cek_area = () => {
    fetch(area_api)
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
                    area_cb.appendChild(option);
                    area_cb_filter.appendChild(option_filter);
                    if (i == 0) selected_area = element.id;
                });
                load_data();
            } else {
                location.href = "area"
            }
        })
        .catch(error => {
            console.error('Ada kesalahan:', error);
        });
}
const handle_filter = () => {
    if (area_cb.value == selected_area) {
        selected_area = area_cb_filter.value;
        area_cb.value = area_cb_filter.value;
    } else {
        selected_area = area_cb.value;
        area_cb_filter.value = area_cb.value;
    }
    load_data();
}
area_cb.onchange = handle_filter;
area_cb_filter.onchange = handle_filter;
submit_btn.onclick = handle_submit;
cancel_btn.onclick = handle_cancel_btn;
add_btn.onclick = handle_add_btn;
cek_area();
// load_data();