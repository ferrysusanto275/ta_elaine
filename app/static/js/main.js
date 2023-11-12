const base_api_url = "http://127.0.0.1:5000/api/";
const drop_down_menu = document.querySelectorAll(".drop-down");
drop_down_menu.forEach((dd) => {
  dd.onclick = () => {
    if (dd.classList.contains("active")) dd.classList.remove("active");
    else dd.classList.add("active");
  };
});

const li_menu = document.querySelectorAll("li");
li_menu.forEach((li) => {
  li.onclick = () => {
    li.firstElementChild.click();
  };
});
