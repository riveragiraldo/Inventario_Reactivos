document.addEventListener("DOMContentLoaded", function () {
    //Código para ocultar el otro asunto
    const tipoSolicitudSelect = document.getElementById("tipo_solicitud");
    const asuntoContainer = document.getElementById("asunto-container");

    // Función para verificar y mostrar/ocultar el campo "asunto"
    function verificarTipoSolicitud() {
        const selectedOption = tipoSolicitudSelect.options[tipoSolicitudSelect.selectedIndex];
        if (selectedOption.text === "OTRA") {
            asuntoContainer.style.display = "block";  // Mostrar el campo "asunto"
        } else {
            asuntoContainer.style.display = "none";   // Ocultar el campo "asunto"
        }
    }

    // Llama a la función al cargar la página
    verificarTipoSolicitud();

    // Agrega un evento de cambio al selector
    tipoSolicitudSelect.addEventListener("change", verificarTipoSolicitud);


    //Código para establcer el contador de caracteres

    const textarea = document.getElementById("mensaje");
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