document.addEventListener("DOMContentLoaded", function () {

    // Obtén la referencia a la imagen, la input de texto y la input oculta por clase e ID
    var captchaImage = document.querySelector('.captcha');
    var captchaText = document.getElementById('id_captcha_1');
    var captchaHidden = document.getElementById('id_captcha_0');
    var captchaRefresh = document.getElementById('recargar-captcha');

    // Obtén el contenedor padre
    var captchaContainer = captchaImage.parentNode;

    // Cambia el orden de los elementos
    captchaContainer.appendChild(captchaImage);
    captchaContainer.appendChild(captchaRefresh);
    captchaContainer.appendChild(captchaText);
    captchaContainer.appendChild(captchaHidden);
    
    // Agrega las clases 'col-lg-4' y 'col-md-4' al elemento
    captchaText.classList.add('form-control');
});