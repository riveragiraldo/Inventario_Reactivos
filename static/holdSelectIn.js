// Función para configurar los selectores según los valores en la URL o valores por defecto
function configurarSelectoresDesdeURL() {
    const urlParams = new URLSearchParams(window.location.search);

    const labValue = urlParams.get('lab');
    const nameValue = urlParams.get('name');
    const locationValue = urlParams.get('location');
    const destinationValue = urlParams.get('destination');
    const createdByValue = urlParams.get('created_by');

    const labSelect = document.getElementById('lab');
    const nameSelect = document.getElementById('name');
    const locationSelect = document.getElementById('location');
    const destinationSelect = document.getElementById('destination');
    
    const createdBySelect = document.getElementById('created_by');

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

    if (locationValue !== null) {
        locationSelect.value = locationValue;
    } else {
        locationSelect.value = ''; // Valor por defecto del selector "location"
    }

    if (destinationValue !== null) {
        destinationSelect.value = destinationValue;
    } else {
        destinationSelect.value = ''; // Valor por defecto del selector "location"
    }

   

    if (createdByValue !== null) {
        createdBySelect.value = createdByValue;
    } else {
        createdBySelect.value = ''; // Valor por defecto del selector "location"
    }

    updateSelectOptionsByLab();
}

// Esperar 200 ms después de la carga para configurar los selectores desde la URL
window.addEventListener('load', function () {
    setTimeout(configurarSelectoresDesdeURL, 200);
});
