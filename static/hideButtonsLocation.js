//Ocultar los enlaces "+" Add si es ventana emergente
// Función para verificar si la ventana actual es una ventana emergente
function isPopupWindow() {
    return window.opener != null;
  }

  // Función para ocultar los botones de agregar si es una ventana emergente
  function hideAddButtonsIfPopup() {
    var addFacultadCont = document.getElementById("addFacultadCont");

    if (isPopupWindow()) {
      addFacultadCont.style.display = "none";
    }
  }

  // Ejecutar la función al cargar la página
  hideAddButtonsIfPopup();