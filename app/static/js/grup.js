const url_api = base_api_url + "grup_instansi"
fetch(url_api)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then(data => {
        // console.log(data); // Lakukan sesuatu dengan data yang diambil
        let tabel_body = document.getElementById('body_data');
        if (data.length > 0) {

            tabel_body.innerHTML = "";
            data.forEach((element, i) => {
                let res = "<tr>";
                res += `<td>${i + 1}</td>`;
                res += `<td>${element.nama}</td>`;
                let btn_delete = "";
                let btn_edit = "";
                res += `<td>${btn_edit} ${btn_delete}</td>`;
                res += "</tr>";
                tabel_body.innerHTML += res;
            });
        }
    })
    .catch(error => {
        console.error('Ada kesalahan:', error);
    });
