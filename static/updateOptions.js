//Actualiza los select marca y reference dependiendo de la existencia en almacén
// Obtener los elementos del DOM

const nameSelect = document.getElementById('name');
const referenceSelect = document.getElementById('reference');
const trademarkSelect = document.getElementById('trademark');
const labSelect = document.getElementById('lab');


// Manejar el evento de cambio en el primer input name
nameSelect.addEventListener('change', function () {
    updateTrademarkAndReferenceByname() 
});

// Manejar el evento de cambio en el select trademark
trademarkSelect.addEventListener('change', updateReferenceByTrademark);

// Función para actualizar los selects "Trademark" y "Reference" al cambiar el select "Name"
function updateTrademarkAndReferenceByname() {
    // Obtener los valores seleccionados en los selectores "Trademark" y "Reference"
    const selectedTrademark = trademarkSelect.value;
    const selectedReference = referenceSelect.value;

    // Restaurar la selección previa del select "Trademark" si existe
    const previousTrademarkValue = trademarkSelect.dataset.previousValue;
    if (previousTrademarkValue) {
        trademarkSelect.value = previousTrademarkValue;
    }

    // Restaurar la selección previa del select "Reference" si existe
    const previousReferenceValue = referenceSelect.dataset.previousValue;
    if (previousReferenceValue) {
        referenceSelect.value = previousReferenceValue;
    }

    // Guardar el nuevo valor seleccionado en el select "Name"
    const selectedName = nameSelect.value;
    const selectedLab = labSelect.value;

    // Realizar una solicitud AJAX para obtener las marcas y referencias correspondientes al nombre seleccionado
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/trademarksandreferencesbyname?name=${selectedName}&lab=${selectedLab}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones de los selectores "Trademark" y "Reference"
            trademarkSelect.innerHTML = '';
            referenceSelect.innerHTML = '';

            // Agregar opción "Todas" al select "Trademark"
            const allTrademarkOption = document.createElement('option');
            allTrademarkOption.value = '';
            allTrademarkOption.textContent = 'Todas';
            trademarkSelect.appendChild(allTrademarkOption);

            // Agregar opción "Todas" al select "Reference"
            const allReferenceOption = document.createElement('option');
            allReferenceOption.value = '';
            allReferenceOption.textContent = 'Todas';
            referenceSelect.appendChild(allReferenceOption);

            // Iterar sobre la respuesta JSON (lista de marcas y referencias)
            response.forEach(function (item) {
                // Agregar opción al select "Trademark"
                const trademarkOption = document.createElement('option');
                trademarkOption.value = item.trademark;
                trademarkOption.textContent = item.trademark__name;
                trademarkSelect.appendChild(trademarkOption);

                // Agregar opción al select "Reference"
                const referenceOption = document.createElement('option');
                referenceOption.value = item.reference;
                referenceOption.textContent = item.reference;
                referenceSelect.appendChild(referenceOption);
            });

            // Restaurar la selección previa del select "Trademark" si existía y sigue siendo una opción válida
            if (selectedTrademark && trademarkSelect.querySelector(`option[value="${selectedTrademark}"]`)) {
                trademarkSelect.value = selectedTrademark;
            }

            // Restaurar la selección previa del select "Reference" si existía y sigue siendo una opción válida
            if (selectedReference && referenceSelect.querySelector(`option[value="${selectedReference}"]`)) {
                referenceSelect.value = selectedReference;
            }
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
    xhr.open('GET', `/api/referencesbytrademark?name=${selectedName}&lab=${selectedLab}&trademark=${selectedTrademark}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones de los selectores "Trademark" y "Reference"
            referenceSelect.innerHTML = '';

            
            // Agregar opción "Todas" al select "Reference"
            const allReferenceOption = document.createElement('option');
            allReferenceOption.value = '';
            allReferenceOption.textContent = 'Todas';
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

