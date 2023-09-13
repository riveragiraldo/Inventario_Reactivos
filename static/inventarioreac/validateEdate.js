// Función para formatear la fecha en "dd/mm/aaaa"
function formatDate(date) {
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
}

// Obtener el elemento edate por su ID
const edateInput = document.getElementById('edate');

// Obtener el elemento orderdate por su ID
const orderDateInput = document.getElementById('orderdate');

// Función para validar la fecha y establecer la fecha por defecto si es necesario
function validateEdate() {
    // Obtener el valor del campo edate
    const edateValue = edateInput.value;

    // Obtener la fecha de hoy en formato yyyy-mm-dd
    const today = new Date().toISOString().split('T')[0];

    // Verificar si la fecha es hoy o anterior
    if (edateValue <= today || edateValue > '2100-12-31') {
        // Mostrar la alerta con el rango de fechas correcto
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        const tomorrowFormatted = formatDate(tomorrow);

        // Establecer la fecha por defecto en el campo edate (mañana)
        tomorrow.setDate(tomorrow.getDate()+30);
        const tomorrowFormattedInput = tomorrow.toISOString().split('T')[0];
        edateInput.value = tomorrowFormattedInput;

        //Mostrar Alerta
        Swal.fire({
            icon: 'warning',
            title: 'Fecha de vencimiento incorrecta',
            text: 'Ingrese una fecha de vencimiento válida: entre ' + tomorrowFormatted + ' y 31/12/2100',
            confirmButtonText: 'Aceptar',
            didClose: () => {
                // Posicionar el foco en el campo minstock para que el usuario pueda escribir
                edateInput.focus();
            }
        })

        
    }
}

// Función para validar la fecha y establecer la fecha por defecto si es necesario
function validateOrderDate() {
    
    // Obtener el valor del campo edate
    const orderDateValue = orderDateInput.value;

    // Obtener la fecha de hoy en formato yyyy-mm-dd
    const today = new Date().toISOString().split('T')[0];

    // Verificar si la fecha es hoy o anterior
    if (orderDateValue >= today) {
        // Mostrar la alerta con el rango de fechas correcto
        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        const yesterdayFormatted = formatDate(yesterday);

        // Establecer la fecha por defecto en el campo orderdate
        
        orderDateInput.value = '';

        //Mostrar Alerta
        Swal.fire({
            icon: 'warning',
            title: 'Fecha de orden de compra incorrecta',
            text: 'Ingrese una fecha de orden válida: entre ' + yesterdayFormatted + ' o anterior.',
            confirmButtonText: 'Aceptar',
            didClose: () => {
                // Posicionar el foco en el campo minstock para que el usuario pueda escribir
                orderDateInput.focus();
            }
        })

        
    }
}

// Agregar un evento blur al campo edate
edateInput.addEventListener('blur', validateEdate);

//------------------------------------------------------------------------------------------------------//
//--Validaciones de orderDate--//

// Agregar un evento blur al campo orderdate
orderDateInput.addEventListener('blur', validateOrderDate);

// Obtener referencias a los campos de entrada
const orderInput = document.getElementById('order');
const orderDInput = document.getElementById('orderdate');
let orderDateClicked = false; // Variable para rastrear si se hizo clic en orderdate

// Función para manejar el evento blur
function handleBlurEvent() {
    // Verificar si el campo de fecha de orden está vacío
    if (orderInput.value.trim() !== '' && orderDInput.value.trim() === '' && !orderDateClicked) {
        // Hacer foco en el campo de fecha de orden
        orderDInput.focus();

        // Mostrar la notificación con SweetAlert2
        Swal.fire({
            icon: 'warning',
            title: 'Error en la orden de compra',
            text: 'Debe escribir una fecha para la orden de compra',
            confirmButtonText: 'Aceptar'
        });


    }

    // Reiniciar la variable de clic para la próxima vez
    orderDateClicked = false;
}
// Función para manejar el evento blur
function handleBlurrEvent() {
    // Verificar si el campo de fecha de orden está vacío
    if (orderInput.value.trim() !== '' && orderDInput.value.trim() === '' && !orderDateClicked) {
        
        // Mostrar la notificación con SweetAlert2
        Swal.fire({
            icon: 'warning',
            title: 'Error en la orden de compra',
            text: 'Debe escribir una fecha válida para la orden de compra',
            confirmButtonText: 'Aceptar'
        });


    }

    // Reiniciar la variable de clic para la próxima vez
    orderDateClicked = false;
}

// Agregar un controlador de eventos al campo de entrada de orden
orderInput.addEventListener('blur', function () {
    // Esperar 100 ms antes de ejecutar la función
    setTimeout(handleBlurEvent, 100);
});

// Agregar un controlador de eventos al campo de entrada de fecha de orden
orderDInput.addEventListener('focus', function () {
    // Marcar que se hizo clic en orderdate
    orderDateClicked = true;
    // Agregar un controlador de eventos al campo de entrada de orden
    orderDInput.addEventListener('blur', function () {
        // Esperar 100 ms antes de ejecutar la función
        setTimeout(handleBlurrEvent, 2);
    });
});



