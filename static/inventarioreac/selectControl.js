//Actualizar Select según selecciones
// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const nameSelect = document.getElementById('name');
const trademarkSelect = document.getElementById('trademark');


function updateNameTrademarkAndReferenceByLab() {
    // Obtener los valores seleccionados en los selectores "Name", "Trademark" y "Reference"
    const selectedName = nameSelect.value;
    const selectedTrademark = trademarkSelect.value;

    const selectedLab = labSelect.value;

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


    // Guardar el nuevo valor seleccionado en el select "Lab"


    // Realizar una solicitud AJAX para obtener los nombres, marcas  correspondientes al laboratorio seleccionado
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/namesandtrademarksandreferencesbylab?lab=${selectedLab}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones de los selectores "Name", "Trademark" 
            nameSelect.innerHTML = '';
            trademarkSelect.innerHTML = '';


            // Agregar opción "Todos" al select "Name"
            const allNameOption = document.createElement('option');
            allNameOption.value = '';
            allNameOption.textContent = 'TODOS';
            nameSelect.appendChild(allNameOption);

            // Agregar opción "Todas" al select "Trademark"
            const allTrademarkOption = document.createElement('option');
            allTrademarkOption.value = '';
            allTrademarkOption.textContent = 'TODAS';
            trademarkSelect.appendChild(allTrademarkOption);



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



            // Restaurar la selección previa del select "Name" si existía y sigue siendo una opción válida
            if (selectedName && nameSelect.querySelector(`option[value="${selectedName}"]`)) {
                nameSelect.value = selectedName;
            }

            // Restaurar la selección previa del select "Trademark" si existía y sigue siendo una opción válida
            if (selectedTrademark && trademarkSelect.querySelector(`option[value="${selectedTrademark}"]`)) {
                trademarkSelect.value = selectedTrademark;
            }


        }
    };
    xhr.send();
}



// // Función para actualizar los selects "Trademark" y al cambiar el select "Name"

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





document.addEventListener('DOMContentLoaded', function () {
    // Ejecutar la primera función inmediatamente
    updateNameTrademarkAndReferenceByLab();

    // Agregar evento de cambio al select lab para ejecutar la función cuando cambie la selección
    const labSelect = document.getElementById('lab');
    labSelect.addEventListener('change', updateNameTrademarkAndReferenceByLab);

    // Agregar evento de cambio al select name para ejecutar la función cuando cambie la selección
    nameSelect.addEventListener('change', function () {
        updateTrademarkSelect();
    });

    // Llamar a la función updateTrademarkSelect() después de que la página se haya cargado completamente
    window.addEventListener('load', function () {
        updateNameTrademarkAndReferenceByLab();
    });
});










