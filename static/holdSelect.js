
// Función para guardar los valores seleccionados de los selectores en el almacenamiento local
function guardarValoresSelect() {
    const selectedTrade = document.getElementById('trademark').value;
    const selectedLab = document.getElementById('lab').value;
    const selectedReference = document.getElementById('reference').value;
    const selectedName = document.getElementById('name').value;
    const selectedSortBy = document.getElementById('sort-by-select').value;
    



    localStorage.setItem('selectedTrademark', selectedTrade);
    localStorage.setItem('selectedLab', selectedLab);
    localStorage.setItem('selectedReference', selectedReference);
    localStorage.setItem('selectedName', selectedName);
    localStorage.setItem('selectedSortBy', selectedSortBy);

}

// Función para configurar los selectores con los valores almacenados en el almacenamiento local
function configurarSelects() {
    const selectedTrade = localStorage.getItem('selectedTrademark');
    const selectedLab = localStorage.getItem('selectedLab');
    const selectedReference = localStorage.getItem('selectedReference');
    const selectedName = localStorage.getItem('selectedName');
    const selectedSortBy = localStorage.getItem('selectedSortBy');
    

    // Configurar el selector "Trademark
    const selectTrade = document.getElementById('trademark');
    selectTrade.value = selectedTrade || '';


    // Configurar el selector "Lab"
    const selectLab = document.getElementById('lab');
    selectLab.value = selectedLab || '';


    // Configurar el selector "Reference"
    const selectReference = document.getElementById('reference');
    selectReference.value = selectedReference || '';

    // Configurar el selector "Name"
    const selectName = document.getElementById('name');
    selectName.value = selectedName || '';

    // Configurar el selector "sortBy"
    const selectSortBy = document.getElementById('sort-by-select');
    selectSortBy.value = selectedSortBy || 'name';
    

}

window.addEventListener('DOMContentLoaded', function () {
    // Configurar los selectores al cargar la página o después de realizar una búsqueda
    configurarSelects();

    // Agregar el event listener a los selectores para guardar los valores seleccionados
    const selectLab = document.getElementById('lab');
    const selectTrade = document.getElementById('trademark');
    const selectReference = document.getElementById('reference');
    const selectName = document.getElementById('name');
    const selectSortBy = document.getElementById('sort-by-select');


    selectLab.addEventListener('change', guardarValoresSelect);
    selectReference.addEventListener('change', guardarValoresSelect);
    selectName.addEventListener('change', guardarValoresSelect);
    selectTrade.addEventListener('change', guardarValoresSelect);
    selectSortBy.addEventListener('change', guardarValoresSelect);

    // Agregar el event listener al evento pageshow para guardar los valores seleccionados cuando se muestra la página
    window.addEventListener('pageshow', function (event) {
        if (!event.persisted) {
            configurarSelects();
        }
    });

    // Agregar el event listener a los enlaces de registros por página para guardar los valores seleccionados
    const perPage10Link = document.getElementById('per-page-10');
    const perPage20Link = document.getElementById('per-page-20');
    const perPage50Link = document.getElementById('per-page-50');

    perPage10Link.addEventListener('click', guardarValoresSelect);
    perPage20Link.addEventListener('click', guardarValoresSelect);
    perPage50Link.addEventListener('click', guardarValoresSelect);
});
