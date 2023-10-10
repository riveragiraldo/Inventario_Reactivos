// Espera 500 milisegundos después de que la página haya cargado completamente
window.onload = function () {
    wf = document.getElementById('wf').value
    console.log(wf)
    
    if (wf == 'entrada'){
        
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
            

            // Actualiza Select destination
            var destination_new = document.querySelector("#destination");
            destination_new.value = destino;
            destination_new.setAttribute("selected", true);

        }, 100);

        setTimeout(function () {

            // Actualiza Select wlocation
            var ubicacion_almacen_new = document.querySelector("#wlocation");
            ubicacion_almacen_new.value = ubicacion_almacen;
            ubicacion_almacen_new.setAttribute("selected", true);
        }, 500);
    }else if (wf == 'salida'){
        
        
        setTimeout(function () {
            // Actualiza Select lab
            var lab_new = document.querySelector("#lab");
            lab_new.value = laboratorio;
            lab_new.setAttribute("selected", true);

            updateTrademarkSelect() 
            
            // Actualiza Select destination
            var destination_new = document.querySelector("#destination");
            destination_new.value = destino;
            destination_new.setAttribute("selected", true);

        }, 100);

        setTimeout(function () {

            // Actualiza Select trademark
            var trademark_new = document.querySelector("#trademark");
            trademark_new.value = marca;
            trademark_new.setAttribute("selected", true);
            updateReferenceSelect()
        }, 400);
        setTimeout(function () {
            // Actualiza Select reference
            var reference_new = document.querySelector("#reference");
            reference_new.value = referencia;
            reference_new.setAttribute("selected", true);
            }, 700);
    }
    else if (wf == 'crear'){
        
        
        setTimeout(function () {
            // Actualiza Select almacenamiento_interno
            var almacenamiento_interno_new = document.querySelector("#almacenamiento_interno");
            almacenamiento_interno_new.value = almacenamiento_interno;
            almacenamiento_interno_new.setAttribute("selected", true);
            
            // Actualiza Select clase_almacenamiento
            var clase_almacenamiento_new = document.querySelector("#clase_almacenamiento");
            clase_almacenamiento_new.value = clase_almacenamiento;
            clase_almacenamiento_new.setAttribute("selected", true);

            // Actualiza Select Estado
            var state_new = document.querySelector("#selectState");
            state_new.value = estado;
            state_new.setAttribute("selected", true);

            // Actualiza Select Unidades
            var unit_new = document.querySelector("#selectUnidades");
            unit_new.value = unidad;
            unit_new.setAttribute("selected", true);

        }, 100);
        
    }
    else if (wf == 'usuarios'){
        
        
        setTimeout(function () {
            // Actualiza Select Lab
            var lab_new = document.querySelector("#id_lab");
            lab_new.value = lab;
            lab_new.setAttribute("selected", true);
            
            // Actualiza Select rol
            var rol_new = document.querySelector("#id_rol");
            rol_new.value = rol;
            rol_new.setAttribute("selected", true);
        }, 100);
        
    }

};