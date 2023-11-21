//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para ocultar los botones de agregar si es una ventana emergente
function hideAddButtonsIfPopup() {

    
    var addManagerCont = document.getElementById("add_manager_btn");
    var addLocationCont = document.getElementById("add_location_btn");
    var locationBlock = document.getElementById("location-block");
    var managerBlock = document.getElementById("manager-block");

    if (isPopupWindow()) {
       
        addManagerCont.style.display = "none";
        addLocationCont.style.display = "none";
        locationBlock.classList.remove('input-group');
        managerBlock.classList.remove('input-group');

    }
}
// Ejecutar la función al cargar la página
hideAddButtonsIfPopup();