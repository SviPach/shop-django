document.addEventListener('DOMContentLoaded', function() {
    const sidebarCatalog = document.getElementById('sidebarCatalog');
    const sidebarHide = document.getElementById('sidebarHide');
    const sidebarShow = document.getElementById('sidebarShow');

    sidebarHide.addEventListener('click', function() {
        sidebarCatalog.classList.add('collapsed');
        sidebarShow.style.display = 'block';
    });

    sidebarShow.addEventListener('click', function() {
        sidebarCatalog.classList.remove('collapsed');
        sidebarShow.style.display = 'none';
    });
});