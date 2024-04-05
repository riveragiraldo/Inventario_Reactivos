document.addEventListener("DOMContentLoaded", function () {
    //Código para ocultar el otro asunto
    const destinoSelect = document.getElementById("id_destino");
    const userContainer = document.getElementById("user-container");
    const labContainer = document.getElementById("lab-container");
    const userInput = document.getElementById("id_usuario")

    // Función para verificar y mostrar/ocultar el campo "asunto"
    function verificarDestino() {
        const selectedOption = destinoSelect.options[destinoSelect.selectedIndex];
        if (selectedOption.value === "USUARIO_ESPECIFICO") {
            userContainer.style.display = "block";  // Mostrar el campo "usuario"
            labContainer.style.display = "none";   // Ocultar el campo "Laboratorio"
            userInput.required = true;  // Agregar el atributo "required"
            userInput.value=''
        } else {
            userContainer.style.display = "none";   // Ocultar el campo "asunto"
            labContainer.style.display = "block";   // Mostrar el campo "Laboratorio"
            userInput.required = false;  // Quitar el atributo "required"
            userInput.value='' 
        }
    }

    // Llama a la función al cargar la página
    verificarDestino();

    // Agrega un evento de cambio al selector
    destinoSelect.addEventListener("change", verificarDestino);


    //Código para estabelcer el contador de caracteres

    const textarea = document.getElementById("id_mensaje");
    const contador = document.getElementById("contador");

    // Establece el número máximo de caracteres permitidos.
    const maxLength = 1000;

    // Agrega un evento de escucha para el evento "input".
    textarea.addEventListener("input", function () {
        const conteoCaracteres = textarea.value.length;

        // Muestra el contador y muestra la cantidad de caracteres utilizados.
        contador.textContent = conteoCaracteres + "/" + maxLength + " caracteres";

        // Si el usuario supera el límite, puedes aplicar estilos para indicar que se ha excedido.
        if (conteoCaracteres > maxLength) {
            contador.classList.add("excedido"); // Puedes definir estilos CSS para "excedido".
        } else {
            contador.classList.remove("excedido");
        }

        // Si el usuario comienza a escribir, muestra el contador.
        if (conteoCaracteres > 0) {
            contador.style.display = "inline"; // Muestra el contador.
        }
    });
});