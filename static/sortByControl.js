// Función para enviar los datos a la list view Inventarios
function sendSortBy() {
    // Obtener el valor seleccionado
    const sortBy = sortBySelect.value;
    const labS = labSel.value;
    const namS = namSel.value;
    const tradS = tradSel.value;
    const refS = refSel.value;

    // Generar la URL con el nuevo valor de sort y v
    const url = inventarioUrl + "?" + new URLSearchParams({ sort: sortBy, lab: labS, name: namS, trademark: tradS, reference: refS });

    // Redirigir a la nueva URL
    window.location.href = url;
}

// Obtener el elemento select
const sortBySelect = document.getElementById('sort-by-select');
const labSel = document.getElementById('lab');
const namSel = document.getElementById('name');
const tradSel = document.getElementById('trademark');
const refSel = document.getElementById('reference');

// Agregar un controlador de eventos al cambio de selección del sort by
sortBySelect.addEventListener('change', () => {
    sendSortBy();
});



// Obtener el valor seleccionado almacenado en la URL (si existe)
const urlParams = new URLSearchParams(window.location.search);
const selectedSortBy = urlParams.get('sort');

// Establecer el valor seleccionado en el elemento select
if (selectedSortBy) {
    sortBySelect.value = selectedSortBy;
}
