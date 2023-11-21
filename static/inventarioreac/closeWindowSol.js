document.addEventListener("DOMContentLoaded", function () {
    const closeLink = document.getElementById("close-link");

    closeLink.addEventListener("click", function (event) {
       
            window.close()
        
        
    });


    //Código para establcer el contador de caracteres

    const textarea = document.getElementById("observations");
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
