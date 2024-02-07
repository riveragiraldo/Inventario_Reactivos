// Actualizar Select según selecciones
// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const nameSelect = document.getElementById('name');
const destinationSelect = document.getElementById('destination');

const startDateSelect = document.getElementById('start_date');
const endDateSelect = document.getElementById('end_date');

function updateSelectOptionsByLab() {
    // Obtener el valor previamente seleccionados en los selectores
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;
    const selectedDestination = destinationSelect.value;
    
    const selectedStartDate = startDateSelect.value;
    const selectedEndDate = endDateSelect.value;  



    // Restaurar la selección previa del select "Name" si existe
    const previousNameValue = nameSelect.dataset.previousValue;
    if (previousNameValue) {
        nameSelect.value = previousNameValue;
    }

    // Restaurar la selección previa del select "Destination" si existe
    const previousDestinationValue = destinationSelect.dataset.previousValue;
    if (previousDestinationValue) {
        destinationSelect.value = previousDestinationValue;
    }

    
    // Restaurar la selección previa del select "StartDate" si existe
    const previousStartDateValue = startDateSelect.dataset.previousValue;
    if (previousStartDateValue) {
        startDateSelect.value = previousStartDateValue;
    }

    // Restaurar la selección previa del select "StartDate" si existe
    const previousEndDateValue = endDateSelect.dataset.previousValue;
    if (previousEndDateValue) {
        endDateSelect.value = previousEndDateValue;
    }


    // Realizar una solicitud AJAX para obtener las opciones actualizadas
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/in/selectoptionsbylab?lab=${selectedLab}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones de los selectores
            nameSelect.innerHTML = '';
            destinationSelect.innerHTML = '';
            

            // Agregar opción "Todos" al select "Name"
            const allNameOption = new Option('Todos', '');
            nameSelect.add(allNameOption);

            // Agregar opción "Todos" al select "Destination"
            const allDestinationOption = new Option('Todos', '');
            destinationSelect.add(allDestinationOption);

            // Agregar las opciones de nombres al select "Name"
            response.names.forEach(function (item) {
                const option = new Option(item.name__name, item.name);
                nameSelect.add(option);
            });

            // Agregar las opciones de nombres al select "Destination"
            response.destinations.forEach(function (item) {
                const option = new Option(item.destination__name, item.destination);
                destinationSelect.add(option);
            });

            

            // Restaurar la selección previa del select "Name" si existía y sigue siendo una opción válida
            if (selectedName && nameSelect.querySelector(`option[value="${selectedName}"]`)) {
                nameSelect.value = selectedName;
                
            }

            // Restaurar la selección previa del select "Destination" si existía y sigue siendo una opción válida
            if (selectedDestination && destinationSelect.querySelector(`option[value="${selectedDestination}"]`)) {
                destinationSelect.value = selectedDestination;
                
            }

            
            // Restaurar la selección previa del select "StartDate" si existía y sigue siendo una opción válida
            if (selectedStartDate && startDateSelect.querySelector(`option[value="${selectedStartDate}"]`)) {
                startDateSelect.value = selectedStartDate;
                
            }

            // Restaurar la selección previa del select "EndDate" si existía y sigue siendo una opción válida
            if (selectedEndDate && endDateSelect.querySelector(`option[value="${selectedEndDate}"]`)) {
                endDateSelect.value = selectedEndDate;
                
            }
        }
    };

    xhr.send();
}

document.addEventListener('DOMContentLoaded', function () {
    // Ejecutar la primera función inmediatamente
    updateSelectOptionsByLab();

    // Agregar evento de cambio al select lab para ejecutar la función cuando cambie la selección
    labSelect.addEventListener('change', updateSelectOptionsByLab);
});
