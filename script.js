document.addEventListener("DOMContentLoaded", function () {
  const page = document.body.dataset.page;
  const savedTheme = localStorage.getItem("wms-theme");
  const prefersDark = savedTheme === "dark";
  const navMenu = document.querySelector(".nav-menu");
  const navScrollTop = sessionStorage.getItem("wms-nav-scroll-top");
  const navScrollLeft = sessionStorage.getItem("wms-nav-scroll-left");

  if (prefersDark) {
    document.body.classList.add("theme-dark");
  }

  if (navMenu) {
    window.requestAnimationFrame(function () {
      navMenu.scrollTop = Number(navScrollTop || 0);
      navMenu.scrollLeft = Number(navScrollLeft || 0);
    });

    navMenu.addEventListener("scroll", function () {
      sessionStorage.setItem("wms-nav-scroll-top", String(navMenu.scrollTop));
      sessionStorage.setItem("wms-nav-scroll-left", String(navMenu.scrollLeft));
    });
  }

  document.querySelectorAll("[data-nav]").forEach(function (link) {
    if (link.dataset.nav === page) {
      link.classList.add("active");
    }

    link.addEventListener("click", function () {
      if (!navMenu) {
        return;
      }

      sessionStorage.setItem("wms-nav-scroll-top", String(navMenu.scrollTop));
      sessionStorage.setItem("wms-nav-scroll-left", String(navMenu.scrollLeft));
    });
  });

  const toggle = document.querySelector("[data-theme-toggle]");
  if (toggle) {
    toggle.checked = document.body.classList.contains("theme-dark");
    toggle.addEventListener("change", function () {
      document.body.classList.toggle("theme-dark", toggle.checked);
      localStorage.setItem("wms-theme", toggle.checked ? "dark" : "light");
    });
  }
});
