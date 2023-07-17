//Actualizar Select según selecciones
// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const nameSelect = document.getElementById('name');
const trademarkSelect = document.getElementById('trademark');
const referenceSelect = document.getElementById('reference');

function updateNameTrademarkAndReferenceByLab() {
    // Obtener los valores seleccionados en los selectores "Name", "Trademark" y "Reference"
    const selectedName = nameSelect.value;
    const selectedTrademark = trademarkSelect.value;
    const selectedReference = referenceSelect.value;

    // Restaurar la selección previa del select "Name" si existe
    const previousNameValue = nameSelect.dataset.previousValue;
    if (previousNameValue) {
        nameSelect.value = previousNameValue;
    }

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

    // Guardar el nuevo valor seleccionado en el select "Lab"
    

    // Realizar una solicitud AJAX para obtener los nombres, marcas y referencias correspondientes al laboratorio seleccionado
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/namesandtrademarksandreferencesbylab?lab=${selectedLab}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones de los selectores "Name", "Trademark" y "Reference"
            nameSelect.innerHTML = '';
            trademarkSelect.innerHTML = '';
            referenceSelect.innerHTML = '';

            // Agregar opción "Todos" al select "Name"
            const allNameOption = document.createElement('option');
            allNameOption.value = '';
            allNameOption.textContent = 'Todos';
            nameSelect.appendChild(allNameOption);

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

            // Agregar las opciones de nombres al select "Name"
            response.names.forEach(function (item) {
                const option = document.createElement('option');
                option.value = item.name;
                option.textContent = item.name__name;
                nameSelect.appendChild(option);
            });

            // Agregar las opciones de marcas al select "Trademark"
            response.trademarks.forEach(function (item) {
                const option = document.createElement('option');
                option.value = item.trademark;
                option.textContent = item.trademark__name;
                trademarkSelect.appendChild(option);
            });

            // Agregar las opciones de referencias al select "Reference"
            response.references.forEach(function (item) {
                const option = document.createElement('option');
                option.value = item.reference;
                option.textContent = item.reference;
                referenceSelect.appendChild(option);
            });

            // Restaurar la selección previa del select "Name" si existía y sigue siendo una opción válida
            if (selectedName && nameSelect.querySelector(`option[value="${selectedName}"]`)) {
                nameSelect.value = selectedName;
            }

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


// Función para actualizar los selects "Trademark" y "Reference" al cambiar el select "Name"
// // Función para actualizar los selects "Trademark" y "Reference" al cambiar el select "Name"

function updateTrademarkSelect() {
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;

    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/trademarksbylabandname?lab=${selectedLab}&name=${selectedName}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones del select "Trademark"
            trademarkSelect.innerHTML = '';

            // Agregar opción "Todas" al select "Trademark"
            const allTrademarkOption = document.createElement('option');
            allTrademarkOption.value = '';
            allTrademarkOption.textContent = 'Todas';
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
    xhr.open('GET', `/api/referencesbylabandname?lab=${selectedLab}&name=${selectedName}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones del select "Reference"
            referenceSelect.innerHTML = '';

            // Agregar opción "Todas" al select "Reference"
            const allReferenceOption = document.createElement('option');
            allReferenceOption.value = '';
            allReferenceOption.textContent = 'Todas';
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

// Manejar el evento de cambio en el select trademark
trademarkSelect.addEventListener('change', updateReferenceByTrademark);

// Manejar el evento de cambio en el select name
nameSelect.addEventListener('change', updateTrademarkSelect()
,setTimeout(updateReferenceSelect, 50));



// Llamar a las funciones de actualización con retraso
window.addEventListener('load', function () {
    // Obtener el valor actual del select "Name"
    const selectedName = nameSelect.value;

    // Ejecutar la primera función inmediatamente
    updateNameTrademarkAndReferenceByLab();

    if (selectedName !== '') {
        // Ejecutar la segunda función después de 100 ms
        setTimeout(function () {
            updateTrademarkSelect()
            setTimeout(updateReferenceSelect, 50);

            // Obtener el valor actual del select "Trademark"
            const selectedTrademark = trademarkSelect.value;

            if (selectedTrademark !== '') {
                // Ejecutar la tercera función después de 100 ms
                setTimeout(function () {
                    updateReferenceByTrademark();
                }, 300);
            }
        }, 300);
    }
});


