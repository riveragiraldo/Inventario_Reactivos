//Actualiza los select marca y reference dependiendo de la existencia en almacén
// Obtener los elementos del DOM

const nameSelect = document.getElementById('name');
const referenceSelect = document.getElementById('reference');
const trademarkSelect = document.getElementById('trademark');
const labSelect = document.getElementById('lab');


// Manejar el evento de cambio en el primer input name
nameSelect.addEventListener('change', function () {
    updateTrademarkSelect() 
    setTimeout(updateReferenceSelect, 50);
});

// Manejar el evento de cambio en el select trademark
trademarkSelect.addEventListener('change', updateReferenceByTrademark);

// // Función para actualizar los selects "Trademark" y "Reference" al cambiar el select "Name"

function updateTrademarkSelect() {
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;

    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/trademarksbylabandname/?lab=${selectedLab}&name=${selectedName}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones del select "Trademark"
            trademarkSelect.innerHTML = '';

            // Agregar opción "Todas" al select "Trademark"
            const allTrademarkOption = document.createElement('option');
            allTrademarkOption.value = '';
            allTrademarkOption.textContent = 'Seleccione';
            trademarkSelect.appendChild(allTrademarkOption);

            // Iterar sobre la respuesta JSON (lista de marcas)
            response.forEach(function (item) {
                // Agregar opción al select "Trademark"
                const trademarkOption = document.createElement('option');
                trademarkOption.value = item.trademark;
                trademarkOption.textContent = item.trademark__name;
                trademarkSelect.appendChild(trademarkOption);
            });
        }
    };
    xhr.send();
    
}


// Función para actualizar el select "Reference" basado en la selección de "lab" y "name"
function updateReferenceSelect() {
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;

    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/referencesbylabandname/?lab=${selectedLab}&name=${selectedName}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones del select "Reference"
            referenceSelect.innerHTML = '';

            // Agregar opción "Todas" al select "Reference"
            const allReferenceOption = document.createElement('option');
            allReferenceOption.value = '';
            allReferenceOption.textContent = 'Seleccione';
            referenceSelect.appendChild(allReferenceOption);

            // Iterar sobre la respuesta JSON (lista de referencias)
            response.forEach(function (item) {
                // Agregar opción al select "Reference"
                const referenceOption = document.createElement('option');
                referenceOption.value = item.reference;
                referenceOption.textContent = item.reference;
                referenceSelect.appendChild(referenceOption);
            });
        }
    };
    xhr.send();
}




// Función para actualizar el select y "Reference" al cambiar el select "Trademark"
function updateReferenceByTrademark() {
    // Obtener los valores seleccionados en los selectores "Trademark" y "Reference"
    
    const selectedReference = referenceSelect.value;

    // Restaurar la selección previa del select "Reference" si existe
    const previousReferenceValue = referenceSelect.dataset.previousValue;
    if (previousReferenceValue) {
        referenceSelect.value = previousReferenceValue;
    }

    // Guardar el nuevo valor seleccionado en el select "Name"
    const selectedName = nameSelect.value;
    const selectedLab = labSelect.value;
    const selectedTrademark = trademarkSelect.value;

    // Realizar una solicitud AJAX para obtener las marcas y referencias correspondientes al nombre seleccionado
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/referencesbytrademark/?name=${selectedName}&lab=${selectedLab}&trademark=${selectedTrademark}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones de los selectores "Trademark" y "Reference"
            referenceSelect.innerHTML = '';

            
            // Agregar opción "Todas" al select "Reference"
            const allReferenceOption = document.createElement('option');
            allReferenceOption.value = '';
            allReferenceOption.textContent = 'Seleccione';
            referenceSelect.appendChild(allReferenceOption);

            // Iterar sobre la respuesta JSON (lista de marcas y referencias)
            response.forEach(function (item) {
                
                // Agregar opción al select "Reference"
                const referenceOption = document.createElement('option');
                referenceOption.value = item.reference;
                referenceOption.textContent = item.reference;
                referenceSelect.appendChild(referenceOption);
            });

            // Restaurar la selección previa del select "Reference" si existía y sigue siendo una opción válida
            if (selectedReference && referenceSelect.querySelector(`option[value="${selectedReference}"]`)) {
                referenceSelect.value = selectedReference;
            }
        }
    };
    xhr.send();
}

