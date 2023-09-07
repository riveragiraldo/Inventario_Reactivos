// Actualizar Select según selecciones
// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const nameSelect = document.getElementById('name');
const destinationSelect = document.getElementById('destination');
const locationSelect = document.getElementById('location');
const createdBySelect = document.getElementById('created_by');

function updateSelectOptionsByLab() {
    // Obtener el valor seleccionado en el selector "Lab"
    const selectedLab = labSelect.value;

    // Realizar una solicitud AJAX para obtener las opciones actualizadas
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/selectoptionsbylab?lab=${selectedLab}`);
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
                nameLocation=item.location__name+' - '+facultadIniciales
                const option = new Option(nameLocation, item.location);
                locationSelect.add(option);
            });

            // Agregar las opciones de nombres al select "Created_by"
            response.created_bys.forEach(function (item) {
                nombre=item.created_by__first_name+' '+item.created_by__last_name
                const option = new Option(nombre, item.created_by);
                createdBySelect.add(option);
            });
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
