document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const sidebarHide = document.getElementById('sidebarHide');
    const sidebarShow = document.getElementById('sidebarShow');

    sidebarHide.addEventListener('click', function() {
        sidebar.classList.add('collapsed');
        sidebarShow.style.display = 'block';
    });

    sidebarShow.addEventListener('click', function() {
        sidebar.classList.remove('collapsed');
        sidebarShow.style.display = 'none';
    });
});