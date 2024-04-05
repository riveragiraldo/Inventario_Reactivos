// Función para configurar los selectores según los valores en la URL o valores por defecto
function configurarSelectoresDesdeURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const startDateValue = urlParams.get('start_date');
    const endDateValue = urlParams.get('end_date');
    const labValue = urlParams.get('lab');
    const keywordValue = urlParams.get('keyword');

    const startDateSelect = document.getElementById('start_date');
    const endDateSelect = document.getElementById('end_date');
    const labSelect = document.getElementById('lab');
    const keywordSelect = document.getElementById('keyword');


    if (startDateValue !== null) {
        startDateSelect.value = startDateValue;
    } else {
        startDateSelect.value = ''; // Valor por defecto del selector "start_date"
    }

    if (endDateValue !== null) {
        endDateSelect.value = endDateValue;
    } else {
        endDateSelect.value = ''; // Valor por defecto del selector "end_date"
    }

    if (labValue !== null) {
        labSelect.value = labValue;
    } else {
        labSelect.value = ''; // Valor por defecto del selector "lab"
    }

    if (keywordValue !== null) {
        keywordSelect.value = keywordValue;
    } else {
        keywordSelect.value = ''; // Valor por defecto del selector "keyword"
    }

}

// Esperar 200 ms después de la carga para configurar los selectores desde la URL
window.addEventListener('load', function () {
    setTimeout(configurarSelectoresDesdeURL, 50);
});
