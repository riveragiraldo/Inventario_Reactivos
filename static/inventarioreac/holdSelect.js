// Función para configurar los selectores según los valores en la URL o valores por defecto
function configurarSelectoresDesdeURL() {
    const urlParams = new URLSearchParams(window.location.search);

    const labValue = urlParams.get('lab');
    const nameValue = urlParams.get('name');
    const trademarkValue = urlParams.get('trademark');

    const labSelect = document.getElementById('lab');
    const nameSelect = document.getElementById('name');
    const trademarkSelect = document.getElementById('trademark');

    // Verificar si hay valores en la URL, si no, asignar valores por defecto
    if (labValue !== null) {
        labSelect.value = labValue;
    } else {
        labSelect.value = labDefault; // Valor por defecto del selector "lab"
    }

    if (nameValue !== null) {
        nameSelect.value = nameValue;
    } else {
        nameSelect.value = ''; // Valor por defecto del selector "name"
    }

    if (trademarkValue !== null) {
        trademarkSelect.value = trademarkValue;
    } else {
        trademarkSelect.value = ''; // Valor por defecto del selector "trademark"
    }
    updateNameTrademarkAndReferenceByLab();
}

// Esperar 200 ms después de la carga para configurar los selectores desde la URL
window.addEventListener('load', function () {
    setTimeout(configurarSelectoresDesdeURL, 200);
});
