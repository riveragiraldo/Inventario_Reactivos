
// Obtener los elementos del DOM

const nameInput = document.getElementById('name');
const referenceInput = document.getElementById('reference');
const trademarkInput = document.getElementById('trademark');
const labSelect = document.getElementById('lab');
const stockInput = document.getElementById('stock');
const wlocationInput = document.getElementById('wlocation');

// Manejar el evento de cambio en el primer input
nameInput.addEventListener('change', function () {
    // Obtener el valor seleccionado en el primer input
    const selectedName = nameInput.value;
    // Obtener el valor seleccionado en el campo lab
    const selectedLab = labSelect.value;

    // Limpiar el valor del segundo y tercer input
    referenceInput.innerHTML = '';
    trademarkInput.innerHTML = '';
    wlocationInput.innerHTML = '';

    // Realizar una solicitud AJAX para obtener el ID correspondiente al nombre y laboratorio seleccionados
    fetch(`/autocomplete?term=${selectedName}&lab=${selectedLab}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                const reactiveId = data[0].id;

                // Realizar una solicitud AJAX para obtener las referencias correspondientes al reactivo y laboratorio seleccionados
                fetch(`/api/references?reactive_id=${reactiveId}&lab=${selectedLab}`)
                    .then(response => response.json())
                    .then(data => {
                        // Iterar sobre la respuesta JSON (lista de referencias)
                        data.forEach(function (reference) {
                            const option = document.createElement('option');
                            option.value = reference.reference; // Acceder a la propiedad "reference"
                            option.textContent = reference.reference; // Acceder a la propiedad "reference"
                            referenceInput.appendChild(option);
                        });
                    })
                    .catch(error => {
                        console.log('Error:', error);
                    });
            }
        })
        .catch(error => {
            console.log('Error:', error);
        });

    // Realizar una solicitud AJAX para obtener el ID correspondiente al nombre y laboratorio seleccionados
    fetch(`/autocomplete?term=${selectedName}&lab=${selectedLab}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                const reactiveId = data[0].id;

                // Realizar una solicitud AJAX para obtener las marcas correspondientes al reactivo y laboratorio seleccionados
                fetch(`/api/trademarks?reactive_id=${reactiveId}&lab=${selectedLab}`)
                    .then(response => response.json())
                    .then(data => {
                        // Iterar sobre la respuesta JSON (lista de marcas)
                        data.forEach(function (trademark) {
                            const option = document.createElement('option');
                            option.value = trademark.trademark__id; // Acceder a la propiedad "trademark__id"
                            option.textContent = trademark.trademark__name; // Acceder a la propiedad "trademark__name"
                            trademarkInput.appendChild(option);
                        });
                    })
                    .catch(error => {
                        console.log('Error:', error);
                    });
            }
        })
        .catch(error => {
            console.log('Error:', error);
        });

        // Realizar una solicitud AJAX para obtener el ID correspondiente al nombre y laboratorio seleccionados
    fetch(`/autocomplete?term=${selectedName}&lab=${selectedLab}`)
    .then(response => response.json())
    .then(data => {
        if (data.length > 0) {
            const reactiveId = data[0].id;

            // Realizar una solicitud AJAX para obtener las ubicaciones correspondientes al reactivo y laboratorio seleccionados
            fetch(`/api/trademarks?reactive_id=${reactiveId}&lab=${selectedLab}`)
                .then(response => response.json())
                .then(data => {
                    // Iterar sobre la respuesta JSON (lista de marcas)
                    data.forEach(function (trademark) {
                        const option = document.createElement('option');
                        option.value = trademark.trademark__id; // Acceder a la propiedad "trademark__id"
                        option.textContent = trademark.trademark__name; // Acceder a la propiedad "trademark__name"
                        trademarkInput.appendChild(option);
                    });
                })
                .catch(error => {
                    console.log('Error:', error);
                });
        }
    })
    .catch(error => {
        console.log('Error:', error);
    });
});


