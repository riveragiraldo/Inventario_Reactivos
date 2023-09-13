//Actualiza las ubicaciones en almacen dependiendo de laboratorio en que se encuentre

// Función para actualizar los valores del select wlocation
function updateWlocationOptions() {
    // Obtener los elementos del DOM
    const labSelect = document.getElementById('lab');
    const wlocationInput = document.getElementById('wlocation');

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

document.addEventListener('DOMContentLoaded', function () {
    // Llamar a la función updateWlocationOptions al cargar la página
    updateWlocationOptions();

    // Agregar evento de cambio al select lab para ejecutar la función cuando cambie la selección
    const labSelect = document.getElementById('lab');
    labSelect.addEventListener('change', updateWlocationOptions);
});



