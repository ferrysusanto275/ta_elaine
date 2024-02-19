const year_api = base_api_url + "isi/year";
const kmeans_api = base_api_url + "isi/plot_kmeans";
const year_cb_filter = document.getElementById('year_cb_filter')
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
const handle_year = () => {
    load_img();
    isi_data();
}
const isi_data = () => {
    data_score.innerHTML = ""
    fetch(score_api + '/' + year_cb_filter.value).then((response) => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
        .then((data) => {

            data.forEach((element, i) => {
                const newRow = document.createElement('tr')
                const cell1 = document.createElement('td')
                cell1.textContent = i + 2
                newRow.appendChild(cell1)
                const cell2 = document.createElement('td')
                cell2.textContent = element
                newRow.appendChild(cell2)
                data_score.appendChild(newRow)
            });

        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
}
const load_img = () => {
    tampil_perbandingan.innerHTML = "";
    tampil_perbandingan.appendChild(
        create_elbow(
            year_cb_filter.value
        )
    );
};
const create_link = (year) => {
    return `${kmeans_api}/${year}`;
};
const create_elbow = (year) => {
    const img_tampil = document.createElement("img");
    img_tampil.src = create_link(year);
    return img_tampil;
};
year_cb_filter.onchange = handle_year
cek_year()