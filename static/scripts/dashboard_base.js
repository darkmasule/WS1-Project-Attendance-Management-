const dashboard = document.getElementById("dashboard")
const toggle_sidebar = document.getElementById("sidebar_toggle")

toggle_sidebar.addEventListener("click", () => {
    dashboard.classList.toggle("expanded");
});