// Opciones del Spinner
const opts = {
    lines: 16, // número de líneas
    length: 80, // longitud de cada línea
    width: 20, // grosor de cada línea
    radius: 80, // radio del círculo interno
    scale: 1, // escala general del spinner
    corners: 1, // redondeado de las esquinas (0..1)
    color: '#fff', // color de las líneas
    fadeColor: 'transparent', // color de fondo
    speed: 0.6, // velocidad de rotación (revoluciones por segundo)
    rotate: 0, // rotación adicional por frame
    animation: 'spinner-line-fade-quick', // estilo de animación
    direction: 1, // dirección de la animación (1: horario, -1: antihorario)
    zIndex: 2e9, // z-index del spinner
    className: 'spinner', // clase CSS para el spinner
    top: '70%', // posición desde arriba
    left: '50%', // posición desde la izquierda
    shadow: '0 0 1px transparent', // sombra del spinner
    position: 'absolute' // posición del spinner (absolute o fixed)
};

// Variable para almacenar la instancia del spinner
let spinnerInstance = null;


// Función para mostrar el spinner
function showSpinner() {
    var target = document.getElementById("spinner");

    // Mostrar mensaje de espera
    target.innerHTML = '<div class="message">Espere por favor...</div>';
    spinnerInstance = new Spinner(opts).spin(target);

    // Ocultar elementos del formulario y sus etiquetas
    var formElements = document.querySelectorAll("form input, form select, form textarea, form button, form label, form img, .iti, form span");
    formElements.forEach((element) => {
        element.style.display = "none";
    });


}

// Función para ocultar el spinner
function hideSpinner() {
    if (spinnerInstance) {
        spinnerInstance.stop();
    }
    // Ocultar mensaje de espera
    var target = document.getElementById("spinner");
    target.innerHTML = '';

    // Mostrar elementos del formulario y sus etiquetas
    var formElements = document.querySelectorAll("form input, form select, form textarea, form button, form label, form img, .iti, form span");
    formElements.forEach((element) => {
        element.style.display = "block";
    });


}


// Función para validar los campos del formulario
function validarCampos() {
    var campos = document.querySelectorAll("form input[required], form select[required], form textarea[required]");
    for (var i = 0; i < campos.length; i++) {
        var campo = campos[i];
        if (!campo.value) {
            var etiquetaAsociada = obtenerEtiquetaAsociada(campo);
            // Mostrar la notificación con SweetAlert2
            Swal.fire({
                icon: 'warning',
                title: 'Campos no diligenciados',
                text: "No se ha diligenciado el campo " + etiquetaAsociada,
                confirmButtonText: 'Aceptar',
                didClose: () => {
                    // Colocar el foco en la entrada del campo que corresponde al mensaje
                    campo.focus();
                }
            });
            return false;
        }
        if (campo.pattern && !new RegExp("^" + campo.pattern + "$").test(campo.value)) {
            var etiquetaAsociada = obtenerEtiquetaAsociada(campo);
            var tituloCampo = campo.title || etiquetaAsociada;
            // Mostrar la notificación con SweetAlert2
            Swal.fire({
                icon: 'warning',
                title: 'Información Incorrecta',
                text: "Verificar información en " + etiquetaAsociada + " " + tituloCampo,
                confirmButtonText: 'Aceptar',
                didClose: () => {
                    // Colocar el foco en la entrada del campo que corresponde al mensaje
                    campo.focus();
                }
            });
            return false;
        }
    }
    return true;
}

// Agregar un controlador de eventos al evento submit del formulario
form.addEventListener('submit', validarCampos);



//Función principal que la orden desde el submit
function openPopupWindowConfirm() {
    if (validarCampos()) {
        var formData = obtenerDatosFormulario();
        var mensaje = formData;


        // Mostrar la notificación con SweetAlert2
        Swal.fire({
            icon: 'info',
            title: 'Datos del formulario',
            html: '<div style="text-align: left;">Los datos registrados son:<br>' + mensaje + '</div>',

            showCancelButton: true,
            confirmButtonText: 'Aceptar',
            cancelButtonText: 'Cancelar',
        }).then((result) => {
            if (result.isConfirmed) {
                var csrfToken = obtenerCSRFToken(); // Obtener el valor del token CSRF
                var formDataToSend = obtenerDatosFormularioEnviar();
                enviarInformacion(formDataToSend, csrfToken);
            }
        });
    }
}

//Envía la información al servidor
function enviarInformacion(formData, csrfToken) {
    //Oculta formulario y muestra spinner
    showSpinner();
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
            // Ocultar el spinner después de recibir la respuesta del servidor
            


            // Recargar la página después de 700 ms
            setTimeout(() => {
                window.location.reload();
            }, 700);

        })
        .catch(error => {
            // Ocurrió un error al realizar la solicitud
            console.error('Error de red:', error);
        });
}


// Obtiene los datos del formulario y los organiza para sacar la alerta informativa
function obtenerDatosFormulario() {
    var campos = document.querySelectorAll("form input, form select, form textarea");
    var formData = "";

    for (var i = 0; i < campos.length; i++) {
        var campo = campos[i];
        var etiquetaAsociada = obtenerEtiquetaAsociada(campo);
        var valorCampo = obtenerValorCampo(campo);



        //Filtrar botones y token CSRF
        if (
            campo.tagName.toLowerCase() === 'button' ||
            (campo.tagName.toLowerCase() === 'input' && (campo.type === 'button' || campo.type === 'reset')) ||
            campo.name === 'csrfmiddlewaretoken' ||
            campo.id === 'wf' ||
            campo.id === 'stock' ||
            campo.id === 'prefix'||
            campo.id === 'password1' ||
            campo.id === 'password2'||
            campo.id === 'controlMinStock'

        ) {

            continue;
        }

        // Agregar una coma y espacio si no es el último registro
        formData += "<br>" + etiquetaAsociada + " " + valorCampo;
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


    return formData;
}

//Obtiene las etiquetas asociadas de manera que la alerta no esté asociada al name de la input sino a la etiqueta de manera que se a 
//más fácil de entender
function obtenerEtiquetaAsociada(campo) {
    // Verificar si el campo tiene un atributo 'id'
    if (campo.id) {
        // Buscar la etiqueta asociada con el mismo valor en el atributo 'for'
        var etiqueta = document.querySelector('label[for="' + campo.id + '"]');
        if (etiqueta) {
            return etiqueta.getAttribute('name');
        }
    }

    // Si no se encuentra una etiqueta asociada, devolver el 'name' del campo
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


