const year_api = base_api_url + "isi/year";
const titik_peta_api = base_api_url + "titik_peta";
const year_cb_filter = document.getElementById("year_cb_filter");
const tampil_peta = document.getElementById("tampil_peta")
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
                load_img();
            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
};
const load_img = () => {
    tampil_peta.style.position = "relative"
    tampil_peta.innerHTML = "";
    tampil_peta.appendChild(create_img());
    fetch(titik_peta_api)
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
                    console.log(element);
                    tampil_peta.appendChild(create_dot('green', 'aqua', element.x, element.y, element.nama))
                });
            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
};
const create_img = () => {
    const img_tampil = document.createElement("img");
    img_tampil.src = "/assets/img/petabuta.png";
    img_tampil.width = 600
    return img_tampil;
}
const create_dot = (color, fontColor, x, y, nama) => {
    // Create a new div element
    const dot = document.createElement('div');
    dot.innerText = nama
    dot.style.fontSize = '0.7rem'
    dot.style.color = fontColor;

    // Set styles to make it look like a dot
    dot.style.width = '7px'; // Set the width of the dot
    dot.style.height = '7px'; // Set the height of the dot
    dot.style.borderRadius = '50%'; // Set border-radius to make it a circle
    dot.style.backgroundColor = color; // Set the background color of the dot

    dot.style.position = 'absolute';
    dot.style.left = `${x}px`; // Replace '50px' with the desired x-coordinate
    dot.style.top = `${y}px`; // Replace '30px' with the desired y-coordinate

    // Append the dot to the body or another container
    return dot;
}
cek_year()
