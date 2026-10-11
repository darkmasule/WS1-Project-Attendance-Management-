const register_cta = document.getElementById("register_cta");
const registration_form = document.getElementById("registration_form");

register_cta.addEventListener("click", function () {
    registration_form.showModal();
});

registration_form.addEventListener("click", function (event) {
    if (event.target === registration_form) {
        registration_form.close();
    }
});