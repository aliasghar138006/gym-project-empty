const menu = document.getElementById("menu");
const navbar = document.getElementById("navbar");
const btn = document.getElementById("btn");

addEventListener("resize", () => {
  let width = screen.width;
  if (width > 600) {
    menu.style.display = "none";
    navbar.style.display = "none";
  } else {
    menu.style.display = "block";
    navbar.style.display = "block";
  }
});

menu.addEventListener("click", () => {
  navbar.style.display = "block";
  menu.style.display = "none";
});

btn.addEventListener("click", () => {
  navbar.style.display = "none";
  menu.style.display = "block";
});
