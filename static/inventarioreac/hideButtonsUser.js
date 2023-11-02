//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para ocultar los botones de agregar si es una ventana emergente
function hideAddButtonsIfPopup() {

    var addLabCont = document.getElementById("add_lab_btn");
    var addRolCont = document.getElementById("add_rol_btn");
    var labBlock = document.getElementById("lab-block");
    var rolBlock = document.getElementById("rol-block");
    

    if (isPopupWindow()) {

        addLabCont.style.display = "none";
        addRolCont.style.display = "none";
        labBlock.classList.remove('input-group');
        rolBlock.classList.remove('input-group');
        

    }
}
// Ejecutar la función al cargar la página
hideAddButtonsIfPopup();