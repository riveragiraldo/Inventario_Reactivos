function iniciarAutenticacion() {
     // Obtener la URL actual
     var currentUrl = window.location.href;
     // Remmpleza la url relativa actual por la url de redirección
     var fullRedirectUrl = currentUrl.replace(actualRelativeUrl, redirectRelativeUrl);
    // Redirecciona al servicio de autenticación de Google
    window.location.href = 'https://accounts.google.com/o/oauth2/auth?' +
        'client_id=395543985223-19rni6f5f9ufhr9lpddr3qhh2u9gm7ov.apps.googleusercontent.com' +
        '&redirect_uri='+fullRedirectUrl+
        '&response_type=token' + 
        '&scope=email profile' ;  // Puedes ajustar los alcances según tus necesidades
}


const secretKey = 'HelloWorld2011*2024#';

// Función para decodificar mensajes
const decodeMessage = (encodedMessage) => {
    const ciphertext = decodeURIComponent(encodedMessage);
    const bytes = CryptoJS.AES.decrypt(ciphertext, secretKey);
    return bytes.toString(CryptoJS.enc.Utf8);
};




// Obtener parámetros de la URL
const urlParams = new URLSearchParams(window.location.search);
const encodedSuccessMessage = urlParams.get('success');
const encodedMessage = urlParams.get('error');

// Decodificar el mensaje
const decodedMessage = decodeMessage(encodedMessage);


// Obtener el div donde se mostrará el mensaje
const mensajeDiv = document.getElementById('mensaje');

// Mostrar el mensaje correspondiente
if (decodedMessage) {
    mensajeDiv.innerText = decodedMessage;
}