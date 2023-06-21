//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para ocultar los botones de agregar si es una ventana emergente
function hideAddButtonsIfPopup() {

    var addUnitCont = document.getElementById("addUnitCont");
    var addStateCont = document.getElementById("addStateCont");
    var addSgaCont = document.getElementById("addSgaCont");
    var addRespelCont = document.getElementById("addRespelCont");

    if (isPopupWindow()) {

        addUnitCont.style.display = "none";
        addStateCont.style.display = "none";
        addSgaCont.style.display = "none";
        addRespelCont.style.display = "none";

    }
}
// Ejecutar la función al cargar la página
hideAddButtonsIfPopup();