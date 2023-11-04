//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para ocultar los botones de agregar si es una ventana emergente
function hideAddButtonsIfPopup() {

    var addLabCont = document.getElementById("add_lab_btn");
    var addRolCont = document.getElementById("add_rol_btn");
    

    if (isPopupWindow()) {

        addLabCont.style.display = "none";
        addRolCont.style.display = "none";
        

    }
}
// Ejecutar la función al cargar la página
hideAddButtonsIfPopup();