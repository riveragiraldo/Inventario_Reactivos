$(document).ready(function() {
    // Función para ocultar o mostrar los elementos siguientes
    function alternarSiguientes(elemento) {
        if (elemento.nextAll('li[id^="li_"]').is(':visible')) {
            elemento.nextAll('li[id^="li_"]').hide();
        } else {
            elemento.nextAll('li[id^="li_"]').show();
        }
    }

    // Reactivos
    $("#reactivos_button").click(function() {
        alternarSiguientes($("#li_reactivos"));
    });

    // Inventarios
    $("#inventarios_button").click(function() {
        alternarSiguientes($("#li_inventarios"));
    });

    // Solicitudes
    $("#solicitudes_button").click(function() {
        alternarSiguientes($("#li_solicitudes"));
    });

    // Usuarios
    $("#usuarios_button").click(function() {
        alternarSiguientes($("#li_usuarios"));
    });

    // Administrar
    $("#administrar_button").click(function() {
        alternarSiguientes($("#li_administrar"));
    });
});

// Obtener el valor del campo HTML 'title'
var pageTitle = document.title;

// Asignar el valor al elemento de breadcrumb
document.getElementById("breadcrumb-title").textContent = pageTitle;
document.getElementById("breadcrumb_title").setAttribute("title", "Inicio: " + "{{ laboratorio|title}}");


// $(document).ready(function () {
//     $('#datosusuario').popover();
// });

// Evento click para mostrar SweetAlert con la información del reactivo
document.querySelectorAll('.datos-usuario').forEach(element => {
    element.addEventListener('click', function () {
        const userNombre = this.getAttribute('data-name');        
        const userMensaje = this.getAttribute('data-message');

        const datausuario = obtenerInformacionDatosUsuario(userNombre, userMensaje,);
        // Mostrar la alerta después de 500 ms
        setTimeout(function() {
            mostrarSweetAlertUser(datausuario);
        }, 200);
    });
});

// Función para obtener la información del reactivo basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionDatosUsuario(nombre, mensaje,) {

    const datausuario = {
        nombre: nombre,
        mensaje: mensaje,

    };
    return datausuario;
}

// Función para mostrar la SweetAlert con la información del reactivo
function mostrarSweetAlertUser(datausuario) {
    Swal.fire({
        icon: 'info',
        title: `${datausuario.nombre}`,
        html: `
            <div class="card" style="text-align: left;">
                <div class="card-header">
                    A continuación relacionamos el detalle de sus datos
                </div>
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        ${datausuario.mensaje}
                    </ul>
                    </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Cerrar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
