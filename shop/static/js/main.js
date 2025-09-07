document.addEventListener('DOMContentLoaded', function () {
    const sidebarCatalog = document.getElementById('sidebarCatalog');
    const sidebarHide = document.getElementById('sidebarHide');
    const sidebarShow = document.getElementById('sidebarShow');

    sidebarHide.addEventListener('click', function () {
        sidebarCatalog.classList.add('collapsed');
        sidebarShow.style.display = 'block';
    });

    sidebarShow.addEventListener('click', function () {
        sidebarCatalog.classList.remove('collapsed');
        sidebarShow.style.display = 'none';
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const consentBanner = document.getElementById("cookie-consent");
    const acceptBtn = document.getElementById("accept-cookies");

    if (localStorage.getItem("cookiesAccepted")) {
        consentBanner.style.display = "none";
    }

    acceptBtn.addEventListener("click", function () {
        localStorage.setItem("cookiesAccepted", "true");
        consentBanner.style.display = "none";
    });
});