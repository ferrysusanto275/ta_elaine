const base_api_url = "http://127.0.0.1:5000/api/";

const li_menu = document.querySelectorAll("li");
li_menu.forEach((li) => {
  li.onclick = () => {
    li.firstElementChild.click();
  };
});
