//Valida que los campos required se hayan diligenciado, antes de sacar alerta informativa y enviarlos al servidor
function validarCampos() {
    var campos = document.querySelectorAll("form input[required], form select[required], form textarea[required]");
    for (var i = 0; i < campos.length; i++) {
        if (!campos[i].value) {
            alert("Por favor, complete todos los campos obligatorios.");
            return false;
        }
    }
    return true;
}

//Función principal que la orden desde el submit
function openPopupWindowConfirm() {
    if (validarCampos()) {
        var formData = obtenerDatosFormulario();
        var mensaje = "Los datos registrados son:\n\n" + formData;

        if (confirm(mensaje)) {
            var csrfToken = obtenerCSRFToken();  // Obtener el valor del token CSRF
            var formDataToSend = obtenerDatosFormularioEnviar();
            enviarInformacion(formDataToSend, csrfToken);
        }
    }
}

//Envía la información al servidor
function enviarInformacion(formData, csrfToken) {
    fetch('', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData
    })
        .then(response => {
            if (response.ok) {
                // La solicitud se realizó con éxito
                console.log('Datos enviados correctamente');
                //window.location.reload();
            }
            else {
                // La solicitud falló
                console.error('Error al enviar los datos');
            }
        })
        .then(data => {
            // Se recibió una respuesta exitosa, procesar los datos y mostrar mensajes
            console.log('Respuesta del servidor:', data);
            // Realiza cualquier acción adicional que desees después de recibir los datos

            // Recargar la página después de 500 ms
            setTimeout(() => {
                window.location.reload();
            }, 500);
        })
        .catch(error => {
            // Ocurrió un error al realizar la solicitud
            console.error('Error de red:', error);
        });
}


//Obtiene los datos del formulario y los organiza para sacar la alerta informativa
function obtenerDatosFormulario() {
    var campos = document.querySelectorAll("form input, form select, form textarea");
    var formData = "";

    for (var i = 0; i < campos.length; i++) {
        var campo = campos[i];
        var etiquetaAsociada = obtenerEtiquetaAsociada(campo);
        var valorCampo = obtenerValorCampo(campo);

        // Filtrar botones y token CSRF
        if (
            campo.tagName.toLowerCase() === 'button' ||
            (campo.tagName.toLowerCase() === 'input' && (campo.type === 'button' || campo.type === 'reset')) ||
            campo.name === 'csrfmiddlewaretoken' ||
            campo.id === 'wf' ||
            campo.id === 'lab' ||
            campo.id === 'stock'

        ) {
            continue;
        }


        formData += etiquetaAsociada + " " + valorCampo + "\n";
    }

    return formData;
}

//Obtiene los datos del formulario y los organiza para enviarlos al servidor
function obtenerDatosFormularioEnviar() {
    var campos = document.querySelectorAll("form input, form select, form textarea");
    var formData = new FormData();

    for (var i = 0; i < campos.length; i++) {
        var nombreCampo = campos[i].name;
        var valorCampo = campos[i].value;
        formData.append(nombreCampo, valorCampo);
    }
    console.log(formData)

    return formData;
}

//Obtiene las etiquetas asociadas de manera que la alerta no esté asociada al name de la input sino a la etiqueta de manera que se a 
//más fácil de entender
function obtenerEtiquetaAsociada(campo) {
    var etiqueta = campo.previousElementSibling;
    if (etiqueta) {
        return etiqueta.textContent.trim();
    }

    return campo.name;
}

//Obtiene los valores de los select
function obtenerValorCampo(campo) {
    if (campo.tagName.toLowerCase() === "select") {
        var opcionSeleccionada = campo.options[campo.selectedIndex];
        return opcionSeleccionada.textContent;
    }

    return campo.value;
}

//Obtiene el CSRFToken para ser enviado al servidor
function obtenerCSRFToken() {
    var csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (csrfInput) {
        return csrfInput.value;
    }
    return null;
}

//Obtiene el clic del submit para ejecutar las funciones
var addUnitBtn = document.getElementById("open_confirm_in");
addUnitBtn.addEventListener("click", openPopupWindowConfirm);


