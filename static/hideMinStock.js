//Muestra el campo stock mínimo unicamente cuando se este trabajando desde el laboratoriod de química
document.addEventListener("DOMContentLoaded", function () {
    // Obtener los elementos correspondientes a los bloques a modificar
    var referenceBlock = document.getElementById("referenceBlock");
    var weightBlock = document.getElementById("weightBlock");
    var unitBlock = document.getElementById("unitBlock");
    var minStockBlock = document.getElementById("minStockBlock");

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
    }

    // Verificar el valor seleccionado en el campo "Laboratorio" al cargar la página
    if (labSelect.value !== "Laboratorio de química") {
        ocultarBloques();
    }

    // Agregar un evento para verificar el valor seleccionado en el campo "Laboratorio" al cambiar su valor
    labSelect.addEventListener("change", function () {
        if (this.value !== "Laboratorio de química") {
            ocultarBloques();
        } else {
            mostrarBloques();
        }
    });
});