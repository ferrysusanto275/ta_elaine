const year_api = base_api_url + "isi/year";
const year_cb_filter = document.getElementById('year_cb_filter')
const chk = document.getElementById('chk')
const head_data = document.getElementById('head_data')
const body_data = document.getElementById('body_data')
const indikator_api = base_api_url + "indikator";
const aspek_api = base_api_url + "aspek";
const res_kmeans_api = base_api_url + "isi/res_kmeans";
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
                // handle_year()
                cek_domain();
            }
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
};
const cek_domain = () => {
    fetch(indikator_api + "/domain")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            data.forEach(element => {
                //<input id=element.id type='checkbox'>
                let chk_box = document.createElement('input')
                chk_box.type = "checkbox"
                chk_box.classList.add('domain_chk')
                chk_box.id = element.id
                chk_box.setAttribute('data-name', element.nama)
                chk_box.onchange = load_data
                //<label></label>
                // chk_box.textContent = element.name
                let lbl_chk_box = document.createElement('label')
                lbl_chk_box.innerText = element.nama
                lbl_chk_box.setAttribute('for', element.id)
                chk.appendChild(chk_box)
                chk.appendChild(lbl_chk_box)


                chk.append(" ")
            });
            chk.appendChild(document.createElement("br"))
            cek_aspek();
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
};
const cek_aspek = () => {
    fetch(aspek_api)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            data.forEach(element => {
                let chk_box = document.createElement('input')
                chk_box.type = "checkbox"
                chk_box.id = element.id
                chk_box.classList.add('aspek_chk')
                chk_box.onchange = load_data

                chk_box.setAttribute('data-name', element.nama)
                // chk_box.textContent = element.name
                let lbl_chk_box = document.createElement('label')
                lbl_chk_box.innerText = element.nama

                lbl_chk_box.setAttribute('for', element.id)
                chk.appendChild(chk_box)
                chk.appendChild(lbl_chk_box)

                chk.append(" ")
            });
            chk.appendChild(document.createElement("br"))
            chkIndikator()

        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
};
const chkIndikator = () => {
    let chk_box = document.createElement('input')
    chk_box.type = "checkbox"
    chk_box.id = "indikator_chk"
    chk_box.onchange = load_data
    // chk_box.textContent = element.name
    let lbl_chk_box = document.createElement('label')
    lbl_chk_box.innerText = "Indikator"

    lbl_chk_box.setAttribute('for', "indikator_chk")
    chk.appendChild(chk_box)
    chk.appendChild(lbl_chk_box)
    chk.appendChild(document.createElement("br"))
    chkIndeks()
}
const chkIndeks = () => {
    let chk_box = document.createElement('input')
    chk_box.type = "checkbox"
    chk_box.id = "indeks_chk"
    chk_box.onchange = load_data
    // chk_box.textContent = element.name
    let lbl_chk_box = document.createElement('label')
    lbl_chk_box.innerText = "Indeks"
    lbl_chk_box.setAttribute('for', "indeks_chk")
    chk.appendChild(chk_box)
    chk.appendChild(lbl_chk_box)
    load_data();
}
const load_data = () => {
    console.log("Masuk");
    create_head()
    create_body()
}

const create_head = () => {
    head_data.innerHTML = "";
    const newRow = document.createElement("tr")
    const cell1 = document.createElement('td')
    cell1.textContent = "No"
    newRow.appendChild(cell1)
    const cell2 = document.createElement('td')
    cell2.textContent = "Nama Instansi"
    newRow.appendChild(cell2)
    const cell3 = document.createElement('td')
    cell3.textContent = "Grup Instansi"
    newRow.appendChild(cell3)
    const domains_chk = document.querySelectorAll(".domain_chk")
    domains_chk.forEach(domain_chk => {
        if (domain_chk.checked) {
            const cell4 = document.createElement('td')
            cell4.textContent = domain_chk.getAttribute('data-name')
            newRow.appendChild(cell4)

        }
    })
    const aspeks_chk = document.querySelectorAll(".aspek_chk")
    aspeks_chk.forEach(aspek_chk => {
        if (aspek_chk.checked) {
            const cell4 = document.createElement('td')
            cell4.textContent = aspek_chk.getAttribute('data-name')
            newRow.appendChild(cell4)

        }
    })
    const indikator_chk = document.getElementById('indikator_chk')
    if (indikator_chk.checked) {
        for (let i = 1; i <= 47; i++) {
            const cell4 = document.createElement('td')
            cell4.textContent = `I${i}`
            newRow.appendChild(cell4)

        }
    }
    const indeks_chk = document.getElementById('indeks_chk')
    if (indeks_chk.checked) {
        const cell4 = document.createElement('td')
        cell4.textContent = `Indeks`
        newRow.appendChild(cell4)

    }

    const cell5 = document.createElement('td')
    cell5.textContent = "Cluster"
    newRow.appendChild(cell5)
    head_data.appendChild(newRow)

}
const create_body = () => {
    fetch(`${res_kmeans_api}/${year_cb_filter.value}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            body_data.innerHTML = "";

            data.forEach((element, i) => {
                const newRow = document.createElement("tr")
                const cell1 = document.createElement('td')
                cell1.textContent = i + 1
                newRow.appendChild(cell1)
                const cell2 = document.createElement('td')
                cell2.textContent = element.Instansi
                newRow.appendChild(cell2)
                const cell3 = document.createElement('td')
                cell3.textContent = element.Group
                newRow.appendChild(cell3)
                const domains_chk = document.querySelectorAll(".domain_chk")
                domains_chk.forEach(domain_chk => {
                    if (domain_chk.checked) {
                        const cell4 = document.createElement('td')
                        cell4.textContent = element[domain_chk.getAttribute('data-name')]
                        newRow.appendChild(cell4)

                    }
                })
                const aspeks_chk = document.querySelectorAll(".aspek_chk")
                aspeks_chk.forEach(aspek_chk => {
                    if (aspek_chk.checked) {
                        const cell4 = document.createElement('td')
                        cell4.textContent = element[aspek_chk.getAttribute('data-name')]
                        newRow.appendChild(cell4)

                    }
                })
                const indikator_chk = document.getElementById('indikator_chk')
                if (indikator_chk.checked) {
                    for (let i = 1; i <= 47; i++) {
                        const cell4 = document.createElement('td')
                        cell4.textContent = element[`I${i}`]
                        newRow.appendChild(cell4)

                    }
                }
                const indeks_chk = document.getElementById('indeks_chk')
                if (indeks_chk.checked) {
                    const cell4 = document.createElement('td')
                    cell4.textContent = element[`Indeks`]
                    newRow.appendChild(cell4)

                }
                const cell5 = document.createElement('td')
                cell5.textContent = element.Cluster
                newRow.appendChild(cell5)
                body_data.appendChild(newRow)
            });
        })
        .catch((error) => {
            console.error("Ada kesalahan:", error);
        });
}
year_cb_filter.onchange = load_data

cek_year()