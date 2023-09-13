
document.addEventListener("DOMContentLoaded", function () {
    const password1Input = document.getElementById("password1");
    const password1ValidationMsg = document.getElementById("password1-validation-msg");
    const password2Input = document.getElementById("password2");
    const password2ValidationMsg = document.getElementById("password2-validation-msg");

    password1Input.addEventListener("blur", function () {
        const password1Value = password1Input.value;
        const password2Value = password2Input.value;
        const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

        if (!passwordPattern.test(password1Value)) {
            password1ValidationMsg.textContent = "*La contraseña debe tener mínimo 8 caracteres,  al menos una mayúscula, un número, y un caracter especial";
            password1Input.focus();
        } else if (!password2Value || !passwordPattern.test(password2Value)) {
            password2ValidationMsg.textContent = "Ingrese contraseña correctamente";
            password2Input.focus();
        } else if (password1Value !== password2Value) {
            password1ValidationMsg.textContent = "Contraseñas no coinciden";
            password2ValidationMsg.textContent = "Contraseñas no coinciden";
        } else {
            password1ValidationMsg.textContent = "";
            password2ValidationMsg.textContent = "";
        }
    });

    password2Input.addEventListener("blur", function () {
        const password2Value = password2Input.value;
        const password1Value = password1Input.value;
        const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

        if (!passwordPattern.test(password2Value)) {
            password2ValidationMsg.textContent = "*La contraseña debe tener mínimo 8 caracteres,  al menos una mayúscula, un número, y un caracter especial";
            password2Input.focus();
        } else if (!password1Value || !passwordPattern.test(password1Value)) {
            password1ValidationMsg.textContent = "Ingrese contraseña correctamente";
            password1Input.focus();
        } else if (password1Value !== password2Value) {
            password1ValidationMsg.textContent = "Contraseñas no coinciden";
            password2ValidationMsg.textContent = "Contraseñas no coinciden";
        } else {
            password1ValidationMsg.textContent = "";
            password2ValidationMsg.textContent = "";
        }
    });

    password2Input.addEventListener("input", function () {
        const password1Value = password1Input.value;
        const password2Value = password2Input.value;
        const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

        if (!password1Value || !passwordPattern.test(password1Value)) {
            password1ValidationMsg.textContent = "Ingrese Contraseña";
        } else if (password1Value !== password2Value) {
            password1ValidationMsg.textContent = "Contraseñas no coinciden";
            password2ValidationMsg.textContent = "Contraseñas no coinciden";
        } else {
            password1ValidationMsg.textContent = "";
            password2ValidationMsg.textContent = "";
        }
    });

    password1Input.addEventListener("input", function () {
        password1ValidationMsg.textContent = ""; // Borra el mensaje al empezar a escribir nuevamente
        password2ValidationMsg.textContent = ""; // Borra el mensaje al empezar a escribir nuevamente
    });

    password2Input.addEventListener("input", function () {
        password1ValidationMsg.textContent = ""; // Borra el mensaje al empezar a escribir nuevamente
        password2ValidationMsg.textContent = ""; // Borra el mensaje al empezar a escribir nuevamente
    });
});
