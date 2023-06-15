// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const wlocationInput = document.getElementById('wlocation');


if (labSelect) {
    labSelect.addEventListener('change', function () {
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
                    option.value = wlocation.id; // Acceder a la propiedad "wlocation__id"
                    option.textContent = wlocation.name; // Acceder a la propiedad "wlocation__name"
                    wlocationInput.appendChild(option);
                });
            })
            .catch(error => {
                console.log('Error:', error);
            });
    });

    // Disparar el evento 'change' en el campo lab al cargar la página
    labSelect.dispatchEvent(new Event('change'));
}
