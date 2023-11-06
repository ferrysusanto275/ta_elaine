const instansi_cb_filter = document.getElementById("instansi_cb_filter");
const year_tf_filter = document.getElementById("year_tf_filter");
const tabel_body = document.getElementById("body_data");
const url_api = base_api_url + "isi";
const indikator_api = base_api_url + "indikator";
const instansi_api = base_api_url + "instansi";
const predikat_api = base_api_url + "predikat/nilai/";
const cek_instansi = () => {
  fetch(instansi_api)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      if (data.length == 0) {
        location.href = "instansi";
      } else {
        data.forEach((element, i) => {
          let option = document.createElement("option");
          option.value = element.id;
          option.textContent = element.nama;
          instansi_cb_filter.appendChild(option);
          if (i == 0) selected_instansi = element.id;
        });
        cek_indikator();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
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
        load_data();
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const load_data = async () => {
  try {
    let res_domain = await fetch(indikator_api + "/domain");
    if (!(await res_domain.ok)) {
      throw new Error("Network response was not ok");
    }
    let list_domain = await res_domain.json();
    tabel_body.innerHTML = "";
    let jml_akhir = 0;
    for (const domain of list_domain) {
      const newRow = document.createElement("tr");
      const cell1 = document.createElement("td");
      cell1.textContent = domain.nama;
      newRow.appendChild(cell1);
      let nd = 0;
      let res_aspek = await fetch(`${indikator_api}/domain/${domain.id}`);
      if (!(await res_aspek.ok)) {
        throw new Error("Network response was not ok");
      }
      let list_aspek = await res_aspek.json();
      let jml = 0;
      for (const aspek of list_aspek) {
        let na = 0;
        let res_isi = await fetch(
          url_api +
            "/aspek/" +
            instansi_cb_filter.value +
            "/" +
            aspek.id +
            "/" +
            year_tf_filter.value
        );
        if (!(await res_isi.ok)) {
          throw new Error("Network response was not ok");
        }
        let list_isi = (await res_isi).json();
        let jml_indikator = 0;
        (await list_isi).forEach((element) => {
          jml_indikator +=
            parseFloat(element.indikator.bobot) * parseFloat(element.value);
        });
        na = jml_indikator / parseFloat(aspek.bobot);
        let NB = parseFloat(aspek.bobot) * na;
        jml += NB;
      }
      nd = jml / parseFloat(domain.bobot);
      const cell2 = document.createElement("td");
      cell2.textContent = nd.toFixed(2);
      newRow.appendChild(cell2);
      const cell3 = document.createElement("td");
      cell3.textContent = domain.bobot;
      newRow.appendChild(cell3);
      let res = nd * parseFloat(domain.bobot);
      jml_akhir += res;
      const cell4 = document.createElement("td");
      cell4.textContent = res.toFixed(2);
      newRow.appendChild(cell4);
      tabel_body.appendChild(newRow);
    }
    let newRow = document.createElement("tr");
    let cell1 = document.createElement("td");
    cell1.setAttribute("colspan", 3);
    cell1.textContent = "Jumlah ND x BD";
    newRow.appendChild(cell1);
    let cell2 = document.createElement("td");
    cell2.textContent = jml_akhir.toFixed(2);
    newRow.appendChild(cell2);
    tabel_body.appendChild(newRow);

    let rowIndex = document.createElement("tr");
    let cell11 = document.createElement("td");
    cell11.setAttribute("colspan", 3);
    cell11.textContent = `Indeks SPEBE = 1/100 x ${jml_akhir}`;
    rowIndex.appendChild(cell11);
    let cell21 = document.createElement("td");
    cell21.textContent = (jml_akhir / 100).toFixed(2);
    rowIndex.appendChild(cell21);
    tabel_body.appendChild(rowIndex);

    let res_predikat = await fetch(`${predikat_api}${jml_akhir / 100}`);
    if (!(await res_predikat.ok)) {
      throw new Error("Network response was not ok");
    }
    let predikat = await res_predikat.json();
    let rowPredikat = document.createElement("tr");
    let cell1_predikat = document.createElement("td");
    cell1_predikat.setAttribute("colspan", 3);
    cell1_predikat.textContent = `Predikat`;
    rowPredikat.appendChild(cell1_predikat);
    let cell2_predikat = document.createElement("td");
    cell2_predikat.textContent = predikat.name;

    rowPredikat.appendChild(cell2_predikat);
    tabel_body.appendChild(rowPredikat);
  } catch (error) {
    console.error("Ada kesalahan:", error);
  }
};
year_tf_filter.onchange = load_data;
instansi_cb_filter.onchange = load_data;
cek_instansi();
