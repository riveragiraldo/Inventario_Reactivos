// Función para recargar el captcha
function recargarCaptcha() {
    // Obtén una referencia al contenedor del captcha y al botón de recarga
    var captchaContainer = document.getElementById('captcha-container');
    var recargarCaptchaButton = document.getElementById('recargar-captcha');

    // Obtén el valor del token CSRF del formulario
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Realiza una solicitud AJAX para obtener un nuevo captcha
    fetch('/UniClab/captcha_refresh/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
    })
        .then(response => response.json())
        .then(data => {
            if (data.captcha_key) {
                // Construye la URL del captcha usando la clave generada
                var captchaUrl = '/captchaimage/' + data.captcha_key + '/';
                // Construye el contenido del contenedor del captcha
                var newContent = `<img src="${captchaUrl}" alt="captcha" class="captcha">`;
                // Agrega el campo de texto y el botón de recarga al contenido
                newContent += `<input type="hidden" name="captcha_0" value="${data.captcha_key}" class="form-control" id="recaptcha_0" required="" autocomplete="off">`;
                newContent += '<input type="text" name="captcha_1" class="form-control" id="recaptcha_1" required="" autocapitalize="off" autocomplete="off" autocorrect="off" spellcheck="false">';
                newContent += '<button type="button" id="recargar-captcha" class="reload-button" title="Actualizar Recaptcha"></button>';
                // Actualiza el contenido del contenedor del captcha
                captchaContainer.innerHTML = newContent;

                // Vuelve a asignar el manejador de eventos al nuevo botón
                var nuevoRecargarCaptchaButton = document.getElementById('recargar-captcha');
                nuevoRecargarCaptchaButton.addEventListener('click', recargarCaptcha);
            } else {
                // Maneja el caso en que la recarga del captcha no sea exitosa
                console.error('Error al recargar el captcha:', data.error);
            }
        })
        .catch(error => {
            console.error('Error en la solicitud AJAX:', error);
        });
}

// Agrega un controlador de eventos al botón de recarga inicialmente
var recargarCaptchaButton = document.getElementById('recargar-captcha');
recargarCaptchaButton.addEventListener('click', recargarCaptcha);


// Agrega un controlador de eventos al botón de recarga inicialmente
var recargarCaptchaButton = document.getElementById('recargar-captcha');
recargarCaptchaButton.addEventListener('click', recargarCaptcha);