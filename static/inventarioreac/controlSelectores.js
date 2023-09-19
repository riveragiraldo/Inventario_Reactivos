// Espera 500 milisegundos después de que la página haya cargado completamente
window.onload = function () {
    setTimeout(function () {
    // Actualiza Select lab
    var lab_new = document.querySelector("#lab");
    lab_new.value = laboratorio;
    lab_new.setAttribute("selected", true);

    updateWlocationOptions()

     // Actualiza Select trademark
     var trademark_new = document.querySelector("#trademark");
     trademark_new.value = marca;
     trademark_new.setAttribute("selected", true);

    }, 50);
    
    setTimeout(function () {
        
        // Actualiza Select wlocation
        var ubicacion_almacen_new = document.querySelector("#wlocation");
        ubicacion_almacen_new.value = ubicacion_almacen;
        ubicacion_almacen_new.setAttribute("selected", true);
    }, 500);
};