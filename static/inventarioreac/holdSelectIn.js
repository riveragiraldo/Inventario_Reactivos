// Función para configurar los selectores según los valores en la URL o valores por defecto
function configurarSelectoresDesdeURL() {
    const urlParams = new URLSearchParams(window.location.search);

    const labValue = urlParams.get('lab');
    const nameValue = urlParams.get('name');
    const reagentValue = urlParams.get('id_r');
    
    const startDateValue = urlParams.get('start_date');
    const endDateValue = urlParams.get('end_date');

    const labSelect = document.getElementById('lab');
    const nameSelect = document.getElementById('name');
    
    const reagentSelect = document.getElementById('id_r');
    
    const startDateSelect = document.getElementById('start_date');
    const endDateSelect = document.getElementById('end_date');

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

   

    if (reagentValue !== null) {
        reagentSelect.value = reagentValue;
    } else {
        reagentSelect.value = ''; // Valor por defecto del selector "id_r"
    }
        

    if (startDateValue !== null) {
        startDateSelect.value = startDateValue;
    } else {
        startDateSelect.value = ''; // Valor por defecto del selector "start_date"
    }

    if (endDateValue !== null) {
        endDateSelect.value = endDateValue;
    } else {
        endDateSelect.value = ''; // Valor por defecto del selector "start_date"
    }

    
}

// Esperar 200 ms después de la carga para configurar los selectores desde la URL
window.addEventListener('load', function () {
    setTimeout(configurarSelectoresDesdeURL, 200);
});
