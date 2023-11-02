//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para ocultar los botones de agregar si es una ventana emergente
function hideAddButtonsIfPopup() {

    var addUnitCont = document.getElementById("add_unit_btn");
    var addclase_almacenamientoCont = document.getElementById("add_clase_almacenamiento_btn");
    var addalmacenamiento_internoCont = document.getElementById("add_almacenamiento_interno_btn");
    var unitBlock = document.getElementById("unit-block");
    var claseAlmacenamientokBlock = document.getElementById("clase-block");
    var almacenamientoInternoBlock = document.getElementById("almacenamiento-block");

    if (isPopupWindow()) {

        addUnitCont.style.display = "none";
        addclase_almacenamientoCont.style.display = "none";
        addalmacenamiento_internoCont.style.display = "none";
        unitBlock.classList.remove('input-group');
        claseAlmacenamientokBlock.classList.remove('input-group');
        almacenamientoInternoBlock.classList.remove('input-group');
        

    }
}
// Ejecutar la función al cargar la página
hideAddButtonsIfPopup();