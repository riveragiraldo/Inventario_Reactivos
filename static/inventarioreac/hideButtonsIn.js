//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para ocultar los botones de agregar si es una ventana emergente
function hideAddButtonsIfPopup() {

    var addReactCont = document.getElementById("add_reagent_btn");
    var addTradeCont = document.getElementById("add_trademark_btn");
    var addLocationCont = document.getElementById("add_location_btn");
    var addManagerCont = document.getElementById("add_manager_btn");
    var addWlocationCont = document.getElementById("add_wlocation_btn");
    var nameBlock = document.getElementById("name-block");
    var trademarkBlock = document.getElementById("trademark-block");
    var locationBlock = document.getElementById("location-block");
    var managerBlock = document.getElementById("manager-block");
    var wlocationBlock = document.getElementById("wlocation-block");

    if (isPopupWindow()) {

        addReactCont.style.display = "none";
        addTradeCont.style.display = "none";
        addLocationCont.style.display = "none";
        addManagerCont.style.display = "none";
        addWlocationCont.style.display = "none";
        nameBlock.classList.remove('input-group');
        trademarkBlock.classList.remove('input-group');
        locationBlock.classList.remove('input-group');
        managerBlock.classList.remove('input-group');
        wlocationBlock.classList.remove('input-group');        

    }
}
// Ejecutar la función al cargar la página
hideAddButtonsIfPopup();