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
    minStockControl.value='Inactivo'
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
    minStockControl.value='Activo'
}

// Obtener el checkbox "Control de Stock"
var controlStockCheckbox = document.getElementById("controlMinStock");
// Obtener los elementos correspondientes a los bloques a modificar
var referenceBlock = document.getElementById("referenceBlock");
var weightBlock = document.getElementById("weightBlock");
var unitBlock = document.getElementById("unitBlock");
var minStockBlock = document.getElementById("minStockBlock");
var minStockInput = document.getElementById("minstock");
var minStockControl = document.getElementById("minStockControl");

// Verificar el estado del checkbox después de 1100 ms de cargar la página
setTimeout(function () {
    if (controlStockCheckbox.checked) {
        mostrarBloques();
    } else {
        ocultarBloques();
    }
}, 1100);

// Agregar un evento para verificar el estado del checkbox al cambiar su valor
controlStockCheckbox.addEventListener("change", function () {
    
    if (this.checked) {
        mostrarBloques();
    } else {
        ocultarBloques();
    }
});
