// // Función para guardar los valores seleccionados de los selects "Lab" y "Reference" en el almacenamiento local
// function guardarValoresSelect() {
//     const selectedLab = document.getElementById('lab').value;
//     const selectedReference = document.getElementById('reference').value;

//     localStorage.setItem('selectedLab', selectedLab);
//     localStorage.setItem('selectedReference', selectedReference);
//   }

//   // Función para configurar los selects "Lab" y "Reference" con los valores almacenados en el almacenamiento local
//   function configurarSelectsLabReference() {
//     const selectedLab = localStorage.getItem('selectedLab');
//     const selectedReference = localStorage.getItem('selectedReference');

//     // Resto del código para configurar los select "Lab" y "Reference"
//     const selectLab = document.getElementById('lab');
//     const selectReference = document.getElementById('reference');

//     // Obtener las opciones disponibles para el select "Lab"
//     const labOptions = Array.from(selectLab.options).map(option => ({
//       id: option.value,
//       name: option.textContent
//     }));

//     // Obtener las opciones disponibles para el select "Reference"
//     const referenceOptions = Array.from(selectReference.options).map(option => ({
//       id: option.value,
//       name: option.textContent
//     }));

//     // Limpiar las opciones actuales del select "Lab"
//     selectLab.innerHTML = '';

//     // Agregar las opciones almacenadas en el almacenamiento local al select "Lab"
//     labOptions.forEach(function (option) {
//       const optionElement = document.createElement('option');
//       optionElement.value = option.id;
//       optionElement.textContent = option.name;
//       selectLab.appendChild(optionElement);
//     });

//     // Establecer el valor seleccionado para el select "Lab"
//     selectLab.value = selectedLab;

//     // Limpiar las opciones actuales del select "Reference"
//     selectReference.innerHTML = '';

//     // Agregar las opciones almacenadas en el almacenamiento local al select "Reference"
//     referenceOptions.forEach(function (option) {
//       const optionElement = document.createElement('option');
//       optionElement.value = option.id;
//       optionElement.textContent = option.name;
//       selectReference.appendChild(optionElement);
//     });

//     // Establecer el valor seleccionado para el select "Reference"
//     selectReference.value = selectedReference;

//     // Limpiar los valores almacenados en el almacenamiento local
//     localStorage.removeItem('selectedLab');
//     localStorage.removeItem('selectedReference');
//   }

//   window.addEventListener('DOMContentLoaded', function () {
//     // Configurar los selects "Lab" y "Reference" al cargar la página o después de mostrar la página
//     configurarSelectsLabReference();

//     // Agregar el event listener a los selects "Lab" y "Reference" para guardar los valores seleccionados
//     const selectLab = document.getElementById('lab');
//     const selectReference = document.getElementById('reference');

//     selectLab.addEventListener('change', guardarValoresSelect);
//     selectReference.addEventListener('change', guardarValoresSelect);

//     // Agregar el event listener al evento "pageshow" para guardar los valores seleccionados
//     window.addEventListener('pageshow', function (event) {
//       if (event.persisted) {
//         guardarValoresSelect();
//       }
//     });

//     // Agregar el event listener a los enlaces de registros por página para guardar los valores seleccionados
//     const perPage10Link = document.getElementById('per-page-10');
//     const perPage20Link = document.getElementById('per-page-20');
//     const perPage50Link = document.getElementById('per-page-50');

//     perPage10Link.addEventListener('click', guardarValoresSelect);
//     perPage20Link.addEventListener('click', guardarValoresSelect);
//     perPage50Link.addEventListener('click', guardarValoresSelect);
//   });
// Función para guardar los valores seleccionados de los selects "Lab" y "Reference" en el almacenamiento local
// Función para guardar los valores seleccionados de los selects "Lab" y "Reference" en el almacenamiento local
// Función para guardar los valores seleccionados de los selects "Lab" y "Reference" en el almacenamiento local
// Función para guardar los valores seleccionados de los selectores "Lab", "Reference", "Name" y "Trademark" en el almacenamiento local
// Función para guardar los valores seleccionados de los selectores "Lab", "Reference", "Name" y "Trademark" en el almacenamiento local 

// Función para guardar los valores seleccionados de los selectores en el almacenamiento local
// Función para guardar los valores seleccionados de los selectores en el almacenamiento local
function guardarValoresSelect() {
    const selectedTrade = document.getElementById('trademark').value;
    const selectedLab = document.getElementById('lab').value;
    const selectedReference = document.getElementById('reference').value;
    const selectedName = document.getElementById('name').value;
    

    localStorage.setItem('selectedTrademark', selectedTrade);
    localStorage.setItem('selectedLab', selectedLab);
    localStorage.setItem('selectedReference', selectedReference);
    localStorage.setItem('selectedName', selectedName);
    
}

// Función para configurar los selectores con los valores almacenados en el almacenamiento local
function configurarSelects() {
    const selectedTrade = localStorage.getItem('selectedTrademark');
    const selectedLab = localStorage.getItem('selectedLab');
    const selectedReference = localStorage.getItem('selectedReference');
    const selectedName = localStorage.getItem('selectedName');

     // Configurar el selector "Trademark
     const selectTrade = document.getElementById('trademark');
     selectTrade.value = selectedTrade || '';

    // Configurar el selector "Lab"
    const selectLab = document.getElementById('lab');
    selectLab.value = selectedLab || '';

       
    // Configurar el selector "Reference"
    const selectReference = document.getElementById('reference');
    selectReference.value = selectedReference || '';
    
    // Configurar el selector "Name" después de un retraso de 120ms
    setTimeout(() => {
        const selectName = document.getElementById('name');
        selectName.value = selectedName || '';

    }, 120);



}

window.addEventListener('DOMContentLoaded', function () {
    // Configurar los selectores al cargar la página o después de realizar una búsqueda
    configurarSelects();

    // Agregar el event listener a los selectores para guardar los valores seleccionados
    const selectLab = document.getElementById('lab');
    const selectTrade = document.getElementById('trademark');
    const selectReference = document.getElementById('reference');
    const selectName = document.getElementById('name');
    

    selectLab.addEventListener('change', guardarValoresSelect);
    selectReference.addEventListener('change', guardarValoresSelect);
    selectName.addEventListener('change', guardarValoresSelect);
    selectTrade.addEventListener('change', guardarValoresSelect);

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
