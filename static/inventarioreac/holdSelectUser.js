// Función para configurar los selectores según los valores en la URL o valores por defecto
function configurarSelectoresDesdeURL() {
    const urlParams = new URLSearchParams(window.location.search);

    const labValue = urlParams.get('lab');
    const nameValue = urlParams.get('name');
    const idUserValue = urlParams.get('id_user');


    const labSelect = document.getElementById('lab');
    const nameInput = document.getElementById('name');
    const idUserInput = document.getElementById('id_user');
    
    // Verificar si hay valores en la URL, si no, asignar valores por defecto
    if (labValue !== null) {
        labSelect.value = labValue;
    } else {
        labSelect.value = labDefault; // Valor por defecto del selector "lab"
    }

    

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

    
}

// Esperar 200 ms después de la carga para configurar los selectores desde la URL
window.addEventListener('load', function () {
    setTimeout(configurarSelectoresDesdeURL, 200);
});
