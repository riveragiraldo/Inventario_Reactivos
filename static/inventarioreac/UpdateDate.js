//Obtiene la fecha actual y la formatea para mejor entendimiento

function mostrarFechaActual() {
    var dateElement = document.getElementById("currentDate");
    var now = new Date();
    var formattedDate = formatDate(now);

    dateElement.textContent = formattedDate;
}

function formatDate(date) {
    var year = date.getFullYear();
    var month = padNumber(date.getMonth() + 1);
    var day = padNumber(date.getDate());
    var hours = padNumber(date.getHours());
    var minutes = padNumber(date.getMinutes());
    var seconds = padNumber(date.getSeconds());
    return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds;
}

function padNumber(num) {
    return num < 10 ? '0' + num : num;
}

function onPageLoad() {
    mostrarFechaActual();
}

// Llamar a la función onPageLoad cuando la página se carga
window.addEventListener('load', onPageLoad);
