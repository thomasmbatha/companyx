const header = document.querySelector("header");
const navigatorBar = document.querySelector("#hamburger-btn");
const closeMenuBtn = document.querySelector("#close-menu-btn");

navigatorBar.addEventListener("click", () => header.classList.toggle("show-mobile-menu"));
closeMenuBtn.addEventListener("click", () => navigatorBar.click());