// Actualizar Select según selecciones
// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const nameSelect = document.getElementById('name');
const destinationSelect = document.getElementById('destination');
const locationSelect = document.getElementById('location');
const createdBySelect = document.getElementById('created_by');
const startDateSelect = document.getElementById('start_date');
const endDateSelect = document.getElementById('end_date');

function updateSelectOptionsByLab() {
    // Obtener el valor previamente seleccionados en los selectores
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;
    const selectedDestination = destinationSelect.value;
    const selectedLocation = locationSelect.value;
    const selectedCreatedBy = createdBySelect.value;
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

    // Restaurar la selección previa del select "Location" si existe
    const previousLocationValue = locationSelect.dataset.previousValue;
    if (previousLocationValue) {
        locationSelect.value = previousLocationValue;
    }

    // Restaurar la selección previa del select "Location" si existe
    const previousCreatedByValue = createdBySelect.dataset.previousValue;
    if (previousCreatedByValue) {
        createdBySelect.value = previousCreatedByValue;
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
    xhr.open('GET', `/api/out/selectoptionsbylab?lab=${selectedLab}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Limpiar las opciones de los selectores
            nameSelect.innerHTML = '';
            locationSelect.innerHTML = '';
            destinationSelect.innerHTML = '';
            createdBySelect.innerHTML = '';

            // Agregar opción "Todos" al select "Name"
            const allNameOption = new Option('Todos', '');
            nameSelect.add(allNameOption);

            // Agregar opción "Todos" al select "Destination"
            const allDestinationOption = new Option('Todos', '');
            destinationSelect.add(allDestinationOption);

            // Agregar opción "Todos" al select "Location"
            const allLocationOption = new Option('Todos', '');
            locationSelect.add(allLocationOption);

            // Agregar opción "Todos" al select "Created_by"
            const allCreatedByOption = new Option('Todos', '');
            createdBySelect.add(allCreatedByOption);

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

            // Agregar las opciones de nombres al select "Location"
            response.locations.forEach(function (item) {
                const school = item.location__facultad__name
                var facultadIniciales = school.split(' ').map(word => word[0]).join('').toUpperCase();
                nameLocation = item.location__name + ' - ' + facultadIniciales
                const option = new Option(nameLocation, item.location);
                locationSelect.add(option);
            });

            // Agregar las opciones de nombres al select "Created_by"
            response.created_bys.forEach(function (item) {
                nombre = item.created_by__first_name + ' ' + item.created_by__last_name
                const option = new Option(nombre, item.created_by);
                createdBySelect.add(option);
            });

            // Restaurar la selección previa del select "Name" si existía y sigue siendo una opción válida
            if (selectedName && nameSelect.querySelector(`option[value="${selectedName}"]`)) {
                nameSelect.value = selectedName;
                
            }

            // Restaurar la selección previa del select "Destination" si existía y sigue siendo una opción válida
            if (selectedDestination && destinationSelect.querySelector(`option[value="${selectedDestination}"]`)) {
                destinationSelect.value = selectedDestination;
                
            }

            // Restaurar la selección previa del select "Location" si existía y sigue siendo una opción válida
            if (selectedLocation && locationSelect.querySelector(`option[value="${selectedLocation}"]`)) {
                locationSelect.value = selectedLocation;
                
            }

            // Restaurar la selección previa del select "CreatedBY" si existía y sigue siendo una opción válida
            if (selectedCreatedBy && createdBySelect.querySelector(`option[value="${selectedCreatedBy}"]`)) {
                createdBySelect.value = selectedCreatedBy;
                
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
