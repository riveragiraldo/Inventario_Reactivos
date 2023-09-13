document.addEventListener("DOMContentLoaded", function () {
    const password1Input = document.getElementById("password1");
    const password2Input = document.getElementById("password2");
    const passwordToggleIcons = document.querySelectorAll(".password-toggle");

    passwordToggleIcons.forEach(function (icon) {
      icon.addEventListener("click", function () {
        const inputField = this.closest(".input-group").querySelector("input");
        if (inputField.type === "password") {
          inputField.type = "text";
          this.innerHTML = '<i class="fas fa-eye-slash" title="Ocultar contraseña" style="cursor: pointer;"></i>';
        } else {
          inputField.type = "password";
          this.innerHTML = '<i class="fas fa-eye" title="Ver contraseña" style="cursor: pointer;"></i>';
        }
      });
    });
  });