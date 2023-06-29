// function guardarValoresSelect() {

//     // Obtener los valores y opciones seleccionadas para el select "Marca"
//     const selectTrademark = document.getElementById('trademark');
//     const selectedTrademarkOption = selectTrademark.value;
//     const trademarkOptions = Array.from(selectTrademark.options).map(option => option.value);


//     // Obtener los valores y opciones seleccionadas para el select "Nombre"
//     const selectName = document.getElementById('name');
//     const selectedNameOption = selectName.value;
//     const nameOptions = Array.from(selectName.options).map(option => option.value);

//     // Guardar los valores en el almacenamiento local para el select "Nombre"
//     localStorage.setItem('selectedNameOption', selectedNameOption);
//     localStorage.setItem('nameOptions', JSON.stringify(nameOptions));

//     // Guardar los valores en el almacenamiento local para el select "Marca"
//     localStorage.setItem('selectedTrademarkOption', selectedTrademarkOption);
//     localStorage.setItem('trademarkOptions', JSON.stringify(trademarkOptions));
// }

// document.addEventListener('DOMContentLoaded', function () {

//     // Verificar si hay valores almacenados en el almacenamiento local para el select "Nombre"
//     const selectedNameOption = localStorage.getItem('selectedNameOption');

//     const nameOptions = JSON.parse(localStorage.getItem('nameOptions'));

//     // Verificar si hay valores almacenados en el almacenamiento local para el select "Marca"
//     const selectedTrademarkOption = localStorage.getItem('selectedTrademarkOption');

//     const trademarkOptions = JSON.parse(localStorage.getItem('trademarkOptions'));

//     // Configurar el select "Marca" con los valores almacenados

//     const selectTrademark = document.getElementById('trademark');
//     trademarkOptions.forEach(function (option) {
//         if (option && option.id && option.name) {
//             const optionElement = document.createElement('option');
//             optionElement.value = option
//             optionElement.textContent = option
//             selectTrademark.appendChild(optionElement);
//         }
//     });

//     // Configurar el select "Nombre" con los valores almacenados
//     const selectName = document.getElementById('name');

//     nameOptions.forEach(function (option) {
//         if (option && option.id && option.name) {
//             const optionElement = document.createElement('option');
//             optionElement.value = option.id;
//             optionElement.textContent = option.name;
//             selectName.appendChild(optionElement);
//         }
//     });

//     // Establecer el valor seleccionado para el select "Nombre"
//     selectName.value = selectedNameOption;

//     // Establecer el valor seleccionado para el select "Marca"
//     selectTrademark.value = selectedTrademarkOption;

//     // Limpiar los valores almacenados en el almacenamiento local para el select "Marca"
//     localStorage.removeItem('selectedTrademarkOption');
//     localStorage.removeItem('trademarkOptions');

//     // Limpiar los valores almacenados en el almacenamiento local para el select "Nombre"
//     localStorage.removeItem('selectedNameOption');
//     localStorage.removeItem('nameOptions');
// });


// document.addEventListener('DOMContentLoaded', function () {
//     // Obtener los enlaces por su ID
//     const perPage10Link = document.getElementById('per-page-10');
//     const perPage20Link = document.getElementById('per-page-20');
//     const perPage50Link = document.getElementById('per-page-50');

//     // Agregar event listener a cada enlace
//     perPage10Link.addEventListener('click', guardarValoresSelect);
//     perPage20Link.addEventListener('click', guardarValoresSelect);
//     perPage50Link.addEventListener('click', guardarValoresSelect);
// });


// //Actualizar el tercer select trademarks

// //Obtener los elementos del DOM
// const nameSelect = document.getElementById('name');
// const trademarkSelect = document.getElementById('trademark');

// // Manejar el evento de cambio en el primer select
// nameSelect.addEventListener('change', function () {
//     // Obtener el valor seleccionado en el primer select
//     const selectedNameId = nameSelect.value;


//     // Limpiar las opciones del tercer select trademarks
//     trademarkSelect.innerHTML = '<option value="">Todas</option>';

//     // Realizar una solicitud AJAX para obtener las marcas correspondientes al reactivo seleccionado
//     const xhr = new XMLHttpRequest();
//     xhr.open('GET', `/api/trademarks?reactive_id=${selectedNameId}`);
//     xhr.onload = function () {
//         if (xhr.status === 200) {
//             const response = JSON.parse(xhr.responseText);

//             // Iterar sobre la respuesta JSON (lista de marcas)
//             response.forEach(function (trademark) {
//                 const option = document.createElement('option');
//                 option.value = trademark.trademark__id; // Acceder a la propiedad "trademark__id"
//                 option.textContent = trademark.trademark__name; // Acceder a la propiedad "trademark__name"
//                 trademarkSelect.appendChild(option);
//             });
//         }
//     };
//     xhr.send();
// });

// Obtener los elementos del DOM
const labSelect = document.getElementById('lab');
const nameSelect = document.getElementById('name');
const trademarkSelect = document.getElementById('trademark');

// Función para actualizar el select name y trademark
function updateNameAndTrademark() {
    // Obtener el valor seleccionado en el select lab
    const selectedLab = labSelect.value;

    // Limpiar las opciones del select name y trademark
    nameSelect.innerHTML = '<option value="">Todos</option>';
    trademarkSelect.innerHTML = '<option value="">Todas</option>';

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

// Manejar el evento de cambio en el select lab
labSelect.addEventListener('change', updateNameAndTrademark);

// Llamar a la función de actualización al cargar la página
window.addEventListener('load', updateNameAndTrademark);






// Función para actualizar el select trademark
function updateTrademark() {
    // Obtener los valores seleccionados en los selects lab y name
    const selectedLab = labSelect.value;
    const selectedName = nameSelect.value;

    // Limpiar las opciones del select trademark
    trademarkSelect.innerHTML = '<option value="">Todas</option>';

    // Realizar una solicitud AJAX para obtener las marcas correspondientes al laboratorio y reactivo seleccionados
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/trademarks?lab=${selectedLab}&name=${selectedName}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);

            // Iterar sobre la respuesta JSON (lista de marcas)
            response.forEach(function (trademark) {
                const option = document.createElement('option');
                option.value = trademark.trademark__id; // Acceder al ID de la marca
                option.textContent = trademark.trademark__name; // Acceder al nombre de la marca
                trademarkSelect.appendChild(option);
            });
        }
    };
    xhr.send();
}

// Manejar el evento de cambio en el select name
nameSelect.addEventListener('change', updateTrademark);



