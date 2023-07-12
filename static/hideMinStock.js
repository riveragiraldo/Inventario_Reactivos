

//Muestra el campo stock mínimo únicamente cuando se esté trabajando desde el LABORATORIO DE QUIMICA
document.addEventListener("DOMContentLoaded", function () {
    // Obtener los elementos correspondientes a los bloques a modificar
    var referenceBlock = document.getElementById("referenceBlock");
    var weightBlock = document.getElementById("weightBlock");
    var unitBlock = document.getElementById("unitBlock");
    var minStockBlock = document.getElementById("minStockBlock");
    var minStockInput = document.getElementById("minstock");

    // Obtener el elemento select del laboratorio
    var labSelect = document.getElementById("lab");

    // Función para ocultar los bloques y cambiar las clases correspondientes
    function ocultarBloques() {
        referenceBlock.classList.remove("col-md-3");
        referenceBlock.classList.add("col-md-4");

        weightBlock.classList.remove("col-md-4");
        weightBlock.classList.add("col-md-5");

        unitBlock.classList.remove("col-md-2");
        unitBlock.classList.add("col-md-3");

        minStockBlock.style.display = "none";
        minStockInput.removeAttribute("required"); // Remover el atributo required

    }

    // Función para mostrar los bloques y restaurar las clases originales
    function mostrarBloques() {
        referenceBlock.classList.remove("col-md-4");
        referenceBlock.classList.add("col-md-3");

        weightBlock.classList.remove("col-md-5");
        weightBlock.classList.add("col-md-4");

        unitBlock.classList.remove("col-md-3");
        unitBlock.classList.add("col-md-2");

        minStockBlock.style.display = "block";
        minStockInput.setAttribute("required", "required"); // Agregar el atributo required

    }

    // Verificar el valor seleccionado en el campo "Laboratorio" después de 1100 ms de cargar la página
    setTimeout(function () {
        if (labSelect.value !== "LABORATORIO DE QUIMICA") {
            ocultarBloques();
        } else {
            mostrarBloques();
        }
    }, 1030);

    // Agregar un evento para verificar el valor seleccionado en el campo "Laboratorio" al cambiar su valor
    labSelect.addEventListener("change", function () {
        if (this.value !== "LABORATORIO DE QUIMICA") {
            ocultarBloques();
        } else {
            mostrarBloques();
        }
    });
});
