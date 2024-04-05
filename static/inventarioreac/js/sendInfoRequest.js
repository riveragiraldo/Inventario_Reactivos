$(document).ready(function () {
    $('#solicitudes_externas_form').submit(function (event) {
        // Evitar que el formulario se envíe de forma convencional
        event.preventDefault();

        // Mostrar el mensaje de carga con una barra de progreso
        Swal.fire({
            title: 'Por favor espere...',
            html: 'Enviando datos al servidor',
            timerProgressBar: true,
            didOpen: () => {
                Swal.showLoading();
                // Crear un objeto FormData para enviar archivos
                var formData = new FormData(this);

                // Realizar la solicitud AJAX
                $.ajax({
                    type: 'POST',
                    url: $(this).attr('action'),
                    data: formData,
                    // Necesitas configurar estas opciones para enviar archivos correctamente
                    contentType: false,
                    processData: false,
                    success: function (response) {
                        // Ocultar el mensaje de carga
                        Swal.close();

                        // Manejar la respuesta del servidor
                        if (response.success) {
                            // Mostrar la notificación con SweetAlert2
                            Swal.fire({
                                icon: 'success',
                                title: 'Envío Exitoso',
                                text: response.message,
                                confirmButtonText: 'Aceptar'
                            }).then((result) => {
                                // Redirigir a la página anterior al hacer clic en "Aceptar"
                                if (result.isConfirmed) {
                                    window.location.href = pag_anterior;
                                }
                            });

                            // Puedes realizar acciones adicionales aquí según la respuesta del servidor
                        } else {
                            // Imprimir la respuesta en la consola
                            console.log('Respuesta:', response.errors);
                            // Formatear mensajes de error para mostrarlos en la alerta
                            respuesta = response.errors

                            let formattedErrors = '';



                            if (respuesta === 'La sesión no es válida o ha caducado, debe autenticarse nuevamente para realizar la solicitud') {
                                // Mostrar alerta de errores de validación
                                Swal.fire({
                                    icon: 'warning',
                                    title: 'Mensaje del servidor',
                                    text: respuesta,
                                    confirmButtonText: 'Aceptar'
                                }).then((result) => {
                                    // Redirigir a la página anterior al hacer clic en "Aceptar"

                                    const secretKey = 'HelloWorld2011*2024#';

                                    // Función para codificar mensajes
                                    const encodeMessage = (message) => {
                                        const ciphertext = CryptoJS.AES.encrypt(message, secretKey).toString();
                                        return encodeURIComponent(ciphertext);
                                    };



                                    // Mensaje de ejemplo
                                    const errorMessage = respuesta;

                                    // Codificar el mensaje
                                    const encodedMessage = encodeMessage(errorMessage);
                                    pag_anterior += `?error=${encodedMessage}`

                                    window.location.href = pag_anterior;

                                });
                            } else {
                                for (const field in response.errors) {
                                    if (response.errors.hasOwnProperty(field)) {
                                        formattedErrors += `${response.errors[field][0]}\n`;
                                    }
                                }
                                // Mostrar alerta de errores de validación
                                Swal.fire({
                                    icon: 'warning',
                                    title: 'Mensaje del servidor',
                                    text: 'Error de validación:\n' + formattedErrors,
                                    confirmButtonText: 'Aceptar'
                                });
                            }
                        }
                    },
                    error: function (error) {
                        // Ocultar el mensaje de carga y manejar errores
                        Swal.close();
                        console.error('Error al enviar el formulario:', error);
                    },
                });
            }
        });
    });
});