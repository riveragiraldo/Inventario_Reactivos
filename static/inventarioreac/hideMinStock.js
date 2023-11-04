// Función para ocultar los bloques y cambiar las clases correspondientes
function ocultarBloques() {
    

    minStockBlock.style.display = "none";
    minStockInput.removeAttribute("required"); // Remover el atributo required
    minStockControl.value='Inactivo'
    locationBlock.classList.remove("col-md-6");
    locationBlock.classList.add("col-md-12");
}

// Función para mostrar los bloques y restaurar las clases originales
function mostrarBloques() {
    minStockBlock.style.display = "block";
    minStockInput.setAttribute("required", "required"); // Agregar el atributo required
    minStockControl.value='Activo'
    locationBlock.classList.remove("col-md-6");
    locationBlock.classList.remove("col-md-12");
    locationBlock.classList.add("col-md-6");
}

// Obtener el checkbox "Control de Stock"
var controlStockCheckbox = document.getElementById("controlMinStock");
// Obtener los elementos correspondientes a los bloques a modificar

var minStockBlock = document.getElementById("minStockBlock");
var minStockInput = document.getElementById("minstock");
var minStockControl = document.getElementById("minStockControl");
var locationBlock = document.getElementById("locationBlock");
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
