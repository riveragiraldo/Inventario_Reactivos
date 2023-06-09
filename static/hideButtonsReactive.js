//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para ocultar los botones de agregar si es una ventana emergente
function hideAddButtonsIfPopup() {

    var addUnitCont = document.getElementById("add_unit_btn");
    
    var addSgaCont = document.getElementById("add_sga_btn");
    var addRespelCont = document.getElementById("add_respel_btn");

    if (isPopupWindow()) {

        addUnitCont.style.display = "none";
        addSgaCont.style.display = "none";
        addRespelCont.style.display = "none";
        

    }
}
// Ejecutar la función al cargar la página
hideAddButtonsIfPopup();