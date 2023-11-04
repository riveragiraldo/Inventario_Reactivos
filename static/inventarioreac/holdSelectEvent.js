// Función para configurar los selectores según los valores en la URL o valores por defecto
function configurarSelectoresDesdeURL() {
    const urlParams = new URLSearchParams(window.location.search);

    
    const idUserValue = urlParams.get('id_user');
    const startDateValue = urlParams.get('start_date');
    const endDateValue = urlParams.get('end_date');
    const nameValue = urlParams.get('name');
    

    
    const idUserInput = document.getElementById('id_user');
    const startDateSelect = document.getElementById('start_date');
    const endDateSelect = document.getElementById('end_date');
    const nameInput = document.getElementById('name');
    
    if (nameValue !== null) {
        nameInput.value = nameValue;
    } else {
        nameInput.value = ''; // Valor por defecto "name"
    }
     
    if (idUserValue !== null) {
        idUserInput.value = idUserValue;
    } else {
        idUserInput.value = ''; // Valor por defecto del selector "id_user"
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
    setTimeout(configurarSelectoresDesdeURL, 50);
});
