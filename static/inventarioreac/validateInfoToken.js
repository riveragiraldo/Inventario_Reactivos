// Obtener el valor del parámetro 'token' de la URL
const urlParams = new URLSearchParams(window.location.search);
const token = urlParams.get('token');

const secretKey = 'HelloWorld2011*2024#';

// Función para codificar mensajes
const encodeMessage = (message) => {
    const ciphertext = CryptoJS.AES.encrypt(message, secretKey).toString();
    return encodeURIComponent(ciphertext);
};



// Mensaje de ejemplo
const errorMessage = 'Error: primero debe estar autenticado con un correo válido de la Universidad Nacional de Colombia (micorreo@unal.edu.co).';

// Codificar el mensaje
const encodedMessage = encodeMessage(errorMessage);

// Obtener la URL actual
var currentUrl = window.location.href;


// Verificar si la URL contiene el parámetro access_token
if (currentUrl.includes('access_token')) {
    // JavaScript para obtener el token del fragmento de la URL
    const fragment = window.location.hash.substring(1);
    const token = new URLSearchParams(fragment).get('access_token');



    // Hacer una solicitud a la API de Google para obtener información del usuario
    const user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo';  // Cambio a v2
    const headers = { 'Authorization': `Bearer ${token}` };

    fetch(user_info_url, { headers })
        .then(response => {
            if (!response.ok) {
                throw new Error('La solicitud a la API de Google no fue exitosa');
                pag_anterior += `?error=${encodedMessage}`
                window.location.href = pag_anterior;
            }
            return response.json();
        })
        .then(user_info => {
            // Imprimir nombres, apellidos y correo electrónico en la consola

            const email = user_info.email || 'N/A';
            const nombre = user_info.given_name || 'N/A';
            const apellido = user_info.family_name || 'N/A';
            names = nombre + ' ' + apellido

            // Establecer el valor del campo de correo electrónico y nombres
            document.getElementsByName('email')[0].value = email;
            document.getElementsByName('name')[0].value = names;

            // Obtener el token del fragmento de la URL
            const fragment = window.location.hash.substring(1);
            const token = new URLSearchParams(fragment).get('access_token');

            // Asignar el token al campo oculto
            document.getElementById('access_token').value = token;

            // Verificar si el correo electrónico tiene el dominio correcto
            if (email.endsWith('@unal.edu.co')) {
                console.log('Email válido de la Universidad Nacional de Colombia');
            } else {
                console.log('El email no pertenece a la Universidad Nacional de Colombia');
                pag_anterior += `?error=${encodedMessage}`
                window.location.href = pag_anterior;
            }
        })
        .catch(error => {
            console.error('Error al obtener información del usuario:', error);

            pag_anterior += `?error=${encodedMessage}`
            window.location.href = pag_anterior;
        });
} else {
    console.log('Token no encontrado en la URL');
    pag_anterior += `?error=${encodedMessage}`
    window.location.href = pag_anterior;
}

