// Bloquear Enter
// Agregar un controlador de eventos al formulario
document.forms['form'].addEventListener('keypress', function (e) {
    // Verificar si la tecla presionada es "Enter"
    if (e.key === 'Enter') {
        // Cancelar la acción predeterminada del formulario
        e.preventDefault();
    }
});

// Quitar autocompletado de los campos de texto
var form = document.forms['form'];  // Obtener el formulario por nombre

if (form) {
    var textAndEmailInputs = form.querySelectorAll('input[type="text"], input[type="email"]');  // Obtener campos de texto y correo electrónico

    textAndEmailInputs.forEach(function (input) {
        input.setAttribute('autocomplete', 'off');  // Establecer el atributo autocomplete en "off"
    });
}


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
            if (response.status == 500) {
                respuesta = "Error en el servidor, consulte soporte técnico"
                return respuesta
            }
            
            else {


                if (response.ok) {
                    // La solicitud se realizó con éxito
                    console.log('Datos enviados correctamente');
                    //window.location.reload();


                }
                else {
                    // La solicitud falló
                    console.error('Error al enviar los datos');
                }
                respuesta = response.text()
                return respuesta
            }

        })


        .then(data => {
            // Se recibió una respuesta exitosa, procesar los datos y mostrar mensajes
            console.log('Respuesta del servidor:', data);

            setTimeout(() => {
                hideSpinner()
                var messageText = data;

                var alertType = 'info';  // Tipo de alerta predeterminado para mensajes habituales

                // Verificar el contenido del mensaje para asignar el tipo de alerta adecuado
                if (messageText.includes('Por favor seleccione') || messageText.includes('no se encuentra en la base de datos') || messageText.includes('fecha válida') || messageText.includes('Solo se permiten')|| messageText.includes('pero la cantidad en inventario')|| messageText.includes('pero esta a hecho que')) {
                    alertType = 'warning';
                } else if (messageText.includes('de manera exitosa')) {
                    alertType = 'success';
                } else if (messageText.includes('el inventario sea menor que 0') ) {
                    alertType = 'error';
                }

                // Mostrar la alerta SweetAlert
                Swal.fire({
                    icon: alertType,
                    title: 'Respuesta del servidor',
                    text: data+' Haga clic en Aceptar para continuar',
                    confirmButtonText: 'Aceptar'
                }).then((result) => {
                    if (result.isConfirmed) {
                        // Verificar si la ventana actual es una ventana emergente
                        if (window.opener) {
                            // Actualizar la ventana padre
                            window.opener.location.reload();

                            // Cerrar la ventana actual después de un retraso
                            setTimeout(() => {
                                window.close();
                            }, 200);
                        }else{
                            setTimeout(() => {
                                window.location.reload();
                            }, 100);
                        }
                    }
                });

            }, 700);
            // Verificar si la ventana actual es una ventana emergente



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
            campo.id === 'prefix' ||
            campo.id === 'password1' ||
            campo.id === 'password2' ||
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

// Obtiene el valor o el archivo del campo
function obtenerValorCampo(campo) {
    if (campo.tagName.toLowerCase() === "select") {
        var opcionSeleccionada = campo.options[campo.selectedIndex];
        return opcionSeleccionada.textContent;
    } else if (campo.type === "file") {
        // Manejar campos de archivo
        return campo.files[0];
    } else {
        // Manejar otros tipos de campos (por ejemplo, campos de entrada de texto)
        return campo.value;
    }
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


