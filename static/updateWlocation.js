


// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const wlocationInput = document.getElementById('wlocation');

// Función para actualizar los valores del select wlocation
function updateWlocationOptions() {
    // Obtener el valor seleccionado en el campo lab
    const selectedLab = labSelect.value;

    // Limpiar el campo de opciones de wlocation
    wlocationInput.innerHTML = '';

    // Realizar una solicitud AJAX para obtener las ubicaciones correspondientes al laboratorio seleccionado
    fetch(`/api/wlocations?lab=${selectedLab}`)
        .then(response => response.json())
        .then(data => {
            // Iterar sobre la respuesta JSON (lista de ubicaciones)
            data.forEach(function (wlocation) {
                const option = document.createElement('option');
                option.value = wlocation.id; // Acceder a la propiedad "id"
                option.textContent = wlocation.name; // Acceder a la propiedad "name"
                wlocationInput.appendChild(option);
            });
        })
        .catch(error => {
            console.log('Error:', error);
        });
}

if (labSelect) {
    labSelect.addEventListener('change', function () {
        // Retrasar la ejecución de la función updateWlocationOptions
        setTimeout(updateWlocationOptions, 50);
    });

    // Disparar el evento 'change' en el campo lab al cargar la página
    setTimeout(function () {
        labSelect.dispatchEvent(new Event('change'));
        // Actualizar el select wlocation después de actualizar el select lab
        updateWlocationOptions();
    }, 50);
}
