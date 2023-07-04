//Actualizar Select según selecciones
// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const nameSelect = document.getElementById('name');
const trademarkSelect = document.getElementById('trademark');
const referenceSelect = document.getElementById('reference');

// Función para actualizar el select namesegún cambio en lab
function updateName() {
    // Obtener el valor seleccionado en el select lab
    const selectedLab = labSelect.value;

    // Limpiar las opciones del select name y trademark
    nameSelect.innerHTML = '<option value="">Todos</option>';
    //trademarkSelect.innerHTML = '<option value="">Todas</option>';

    // Realizar una solicitud AJAX para obtener los nombres de los reactivos según el laboratorio seleccionado
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/reactives?lab=${selectedLab}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Iterar sobre la respuesta JSON (lista de nombres de reactivos)
            response.forEach(function (reactive) {
                const option = document.createElement('option');
                option.value = reactive.name__id; // Acceder al ID del reactivo
                option.textContent = reactive.name__name; // Acceder al nombre del reactivo
                nameSelect.appendChild(option);
            });
        }
    };
    xhr.send();
}

// Función para actualizar el select trademark y reference de acuerdo a lab y cambio en name
function updateTrademarkAndReference() {
    // Obtener los valores seleccionados en los selects lab y name
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;

    // Limpiar las opciones de los selects trademark y reference
    trademarkSelect.innerHTML = '<option value="">Todas</option>';
    referenceSelect.innerHTML = '<option value="">Todas</option>';

    // Realizar una solicitud AJAX para obtener las marcas y referencias correspondientes al laboratorio y reactivo seleccionados
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/trademarksandreferences?lab=${selectedLab}&name=${selectedName}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Iterar sobre la respuesta JSON (lista de marcas y referencias)
            response.forEach(function (item) {
                // Agregar opciones al select trademark
                const trademarkOption = document.createElement('option');
                trademarkOption.value = item.trademark__id;
                trademarkOption.textContent = item.trademark__name;
                trademarkSelect.appendChild(trademarkOption);

                // Agregar opciones al select reference
                const referenceOption = document.createElement('option');
                referenceOption.value = item.reference;
                referenceOption.textContent = item.reference;
                referenceSelect.appendChild(referenceOption);
            });
        }
    };
    xhr.send();
}


// Función para actualizar el select reference al cambiar el select trademark
function updateReferenceByTrademark() {
    // Obtener los valores seleccionados en los selects lab, name y trademark
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;
    const selectedTrademark = trademarkSelect.value;

    // Realizar una solicitud AJAX para obtener las referencias correspondientes al laboratorio, reactivo y marca seleccionados
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/referencesbytrademark?lab=${selectedLab}&name=${selectedName}&trademark=${selectedTrademark}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Guardar la selección actual del select reference
            const selectedReference = referenceSelect.value;

            // Limpiar las opciones del select reference
            referenceSelect.innerHTML = '';

            // Agregar opción "Todas"
            const allOption = document.createElement('option');
            allOption.value = '';
            allOption.textContent = 'Todas';
            referenceSelect.appendChild(allOption);

            // Iterar sobre la respuesta JSON (lista de referencias)
            response.forEach(function (reference) {
                const option = document.createElement('option');
                option.value = reference.reference;
                option.textContent = reference.reference;
                referenceSelect.appendChild(option);
            });

            // Restaurar la selección previa del select reference si existe
            if (selectedReference) {
                referenceSelect.value = selectedReference;
            }
        }
    };
    xhr.send();
}

// // Función para actualizar el select trademark al cambiar el select reference
// function updateTrademarkByReference() {
//     // Obtener el valor seleccionado en el select reference
//     const selectedReference = referenceSelect.value;

//     // Realizar una solicitud AJAX para obtener las marcas correspondientes a la referencia seleccionada
//     const xhr = new XMLHttpRequest();
//     xhr.open('GET', `/api/trademarksbyreference?reference=${selectedReference}`);
//     xhr.onload = function () {
//         if (xhr.status === 200) {
//             const response = JSON.parse(xhr.responseText);

//             // Guardar la selección actual del select trademark
//             const selectedTrademark = trademarkSelect.value;

//             // Limpiar las opciones del select trademark
//             trademarkSelect.innerHTML = '';

//             // Agregar opción "Todas"
//             const allOption = document.createElement('option');
//             allOption.value = '';
//             allOption.textContent = 'Todas';
//             trademarkSelect.appendChild(allOption);

//             // Iterar sobre la respuesta JSON (lista de marcas)
//             response.forEach(function (trademark) {
//                 const option = document.createElement('option');
//                 option.value = trademark.trademark__id;
//                 option.textContent = trademark.trademark__name;
//                 trademarkSelect.appendChild(option);
//             });

//             // Restaurar la selección previa del select trademark si existe
//             if (selectedTrademark) {
//                 trademarkSelect.value = selectedTrademark;
//             }
//         }
//     };
//     xhr.send();
// }

// Función para actualizar los selects "Trademark" y "Name" al cambiar el select "Reference"
function updateTrademarkAndNameByReference() {
    // Obtener el valor seleccionado en el select "Reference"
    const selectedReference = referenceSelect.value;

    // Realizar una solicitud AJAX para obtener las marcas y nombres correspondientes a la referencia seleccionada
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/trademarksandnamesbyreference?reference=${selectedReference}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Guardar la selección actual del select "Trademark" y del select "Name"
            const selectedTrademark = trademarkSelect.value;
            const selectedName = nameSelect.value;

            // Limpiar las opciones de los select "Trademark" y "Name"
            trademarkSelect.innerHTML = '';
            nameSelect.innerHTML = '';

            // Agregar opción "Todas" al select "Trademark"
            const allTrademarkOption = document.createElement('option');
            allTrademarkOption.value = '';
            allTrademarkOption.textContent = 'Todas';
            trademarkSelect.appendChild(allTrademarkOption);

            // Agregar opción "Todas" al select "Name"
            const allNameOption = document.createElement('option');
            allNameOption.value = '';
            allNameOption.textContent = 'Todas';
            nameSelect.appendChild(allNameOption);

            // Iterar sobre la respuesta JSON (lista de marcas y nombres)
            response.forEach(function (item) {
                // Agregar opción al select "Trademark"
                const trademarkOption = document.createElement('option');
                trademarkOption.value = item.trademark;
                trademarkOption.textContent = item.trademark__name;
                trademarkSelect.appendChild(trademarkOption);

                // Agregar opción al select "Name"
                const nameOption = document.createElement('option');
                nameOption.value = item.name_id;
                nameOption.textContent = item.name__name;
                nameSelect.appendChild(nameOption);
            });

            // Restaurar la selección previa del select "Trademark" si existe
            if (selectedTrademark) {
                trademarkSelect.value = selectedTrademark;
            }

            // Restaurar la selección previa del select "Name" si existe
            if (selectedName) {
                nameSelect.value = selectedName;
            }
        }
    };
    xhr.send();
}



// Manejar el evento de cambio en el select trademark
trademarkSelect.addEventListener('change', updateReferenceByTrademark);

// Manejar el evento de cambio en el select reference
//referenceSelect.addEventListener('change', updateTrademarkByReference);

// Manejar el evento de cambio en el select reference
referenceSelect.addEventListener('change', updateTrademarkAndNameByReference);

// Manejar el evento de cambio en el select name
nameSelect.addEventListener('change', updateTrademarkAndReference);

// Manejar el evento de cambio en el select lab
labSelect.addEventListener('change', updateName);

// Llamar a la función de actualización al cargar la página
window.addEventListener('load', updateName);


