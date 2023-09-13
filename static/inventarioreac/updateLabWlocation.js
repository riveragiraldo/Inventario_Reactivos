//Obtener el laboratorio desde la ventana padre
//OJO este código es provisional mientras se define como lo va a tomar desde los datos de sesión de usuario
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
}

// Función para actualizar el campo lab con el de la ventana padre
function updateLabIfPopup() {

    if (isPopupWindow()) {

        var lab = window.opener.document.getElementById("lab").value;

        setTimeout(function () {
            //Actualiza Select lab
            var lab_new = document.getElementById('lab');
            lab_new.value = lab;
            var selectedOption = lab_new.options[lab_new.selectedIndex];
            lab_new.setAttribute("selected", true);
        }, 50);
    }
}

// Ejecutar la función al cargar la página

setTimeout(function () {

    updateLabIfPopup();
}, 100)