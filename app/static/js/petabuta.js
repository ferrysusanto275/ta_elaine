const year_api = base_api_url + "isi/year";
const titik_peta_api = base_api_url + "titik_peta";
const year_cb_filter = document.getElementById("year_cb_filter");
const tipe_cb_filter = document.getElementById("tipe_cb_filter");
const tampil_peta = document.getElementById("tampil_peta");
const domain_cb_filter = document.getElementById("domain_cb_filter");
const data_name = document.getElementById("data_name");
const head_name = document.getElementById("head_name");
const indikator_layanan = [
  "i14",
  "i15",
  "i28",
  "i30",
  "i33",
  "i32",
  "i34",
  "i35",
  "i36",
  "i37",
  "i38",
  "i39",
  "i40",
  "i41",
  "i42",
  "i43",
  "i44",
  "i45",
  "i46",
  "i47",
  "domain4",
];
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
  tampil_peta.style.position = "relative";
  tampil_peta.innerHTML = "";
  head_name.innerHTML = "";
  data_name.innerHTML = "";
  tampil_peta.appendChild(create_img());
  fetch(
    titik_peta_api +
      "/" +
      tipe_cb_filter.value +
      "/" +
      year_cb_filter.value +
      "/" +
      domain_cb_filter.value
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Ganti dengan response.text() jika Anda mengharapkan data dalam bentuk teks
    })
    .then((data) => {
      if (data.length == 0) {
        tampil_peta.innerHTML = "<h1>Data Not Found</h1>";
      } else {
        const newRow_head = document.createElement("tr");
        const cell_head1 = document.createElement("td");
        cell_head1.textContent = "No";
        newRow_head.appendChild(cell_head1);
        const cell_head2 = document.createElement("td");
        cell_head2.textContent = "Nama";
        newRow_head.appendChild(cell_head2);
        const cell_head3 = document.createElement("td");
        cell_head3.textContent =
          "Rerata " +
          domain_cb_filter.options[domain_cb_filter.selectedIndex].text;
        newRow_head.appendChild(cell_head3);
        head_name.appendChild(newRow_head);
        for (let key in data["nama_titik"]) {
          let avg = parseFloat(data[domain_cb_filter.value][key]).toFixed(2);
          const newRow = document.createElement("tr");
          const cell1 = document.createElement("td");
          cell1.textContent = parseInt(key) + 1;
          newRow.appendChild(cell1);
          const cell2 = document.createElement("td");
          cell2.textContent = data["nama_titik"][key];
          newRow.appendChild(cell2);
          const cell3 = document.createElement("td");
          cell3.textContent = avg;
          newRow.appendChild(cell3);
          data_name.appendChild(newRow);
          let fc = "black";
          let color = "green";
          let angkaLayanan = 3;
          if (indikator_layanan.indexOf(domain_cb_filter.value) !== -1)
            angkaLayanan = 4;
          if (avg < angkaLayanan) {
            color = "red";
          }
          tampil_peta.appendChild(
            create_dot(
              color,
              fc,
              data["x"][key],
              data["y"][key],
              parseInt(key) + 1
            )
          );
        }
      }
    })
    .catch((error) => {
      console.error("Ada kesalahan:", error);
    });
};
const create_img = () => {
  const img_tampil = document.createElement("img");
  img_tampil.src = "/assets/img/petabuta.png";
  img_tampil.width = 600;
  return img_tampil;
};

const create_dot = (color, fontColor, x, y, nama) => {
  // Create a new div element
  const dot = document.createElement("div");
  dot.innerText = nama;
  dot.style.fontSize = "0.7rem";
  dot.style.color = fontColor;

  // Set styles to make it look like a dot
  dot.style.width = "7px"; // Set the width of the dot
  dot.style.height = "7px"; // Set the height of the dot
  dot.style.borderRadius = "50%"; // Set border-radius to make it a circle
  dot.style.backgroundColor = color; // Set the background color of the dot

  dot.style.position = "absolute";
  dot.style.left = `${x}px`; // Replace '50px' with the desired x-coordinate
  dot.style.top = `${y}px`; // Replace '30px' with the desired y-coordinate

  // Append the dot to the body or another container
  return dot;
};
cek_year();
year_cb_filter.onchange = load_img;
tipe_cb_filter.onchange = load_img;
domain_cb_filter.onchange = load_img;
