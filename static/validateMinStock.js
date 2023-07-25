// Obtener el elemento weight por su ID
const weightInput = document.getElementById('weight');
// Obtener el elemento minstock por su ID
const minstockInput = document.getElementById('minstock');
// Obtener el elemento laboratorio por su ID
const labInput = document.getElementById('lab');

// Agregar un evento input al campo weight
minstockInput.addEventListener('input', () => {
    // Obtener el valor del campo weight
    const weightValue = parseFloat(weightInput.value);

    // Verificar si el valor de weight es igual a 0
    if (weightValue <= 0 || isNaN(weightValue)) {
        // Establecer el valor del campo minstock en 0
        minstockInput.value = '';
        // Mostrar la alerta
        Swal.fire({
            icon: 'warning',
            title: 'Orden de los campos incorrecto',
            text: "Se debe registrar primero Cantidad Retiro",
            confirmButtonText: 'Aceptar',
            didClose: () => {
                // Posicionar el foco en el campo weight para que el usuario pueda escribir
                weightInput.focus();
            }
        })
    }
});

// Función para validar el campo minstock
function validateMinstock() {
    // Obtener el valor del campo weight
    const weightValue = parseFloat(weightInput.value);
    // Obtener el valor del campo minstock
    const minstockValue = parseFloat(minstockInput.value);

    // Verificar si el valor de minstock es mayor que weight
    if (minstockValue > weightValue) {
        minstockInput.value = Math.round(weightInput.value / 10);
        // Mostrar la alerta

        Swal.fire({
            icon: 'warning',
            title: 'Coherencia de los campos',
            text: "El valor de Stock Mínimo debe ser menor a la Cantidad a retirar",
            confirmButtonText: 'Aceptar',
            didClose: () => {
                // Posicionar el foco en el campo weight para que el usuario pueda escribir
                minstockInput.focus();
            }
        })



    }
}

// Agregar un evento blur al campo minstock
minstockInput.addEventListener('blur', validateMinstock);

// Agregar un evento blur al campo minstock
weightInput.addEventListener('blur', validateMinstock);

// Función para validar el campo minstock al enviar la información
function validateMinstockSubmit() {
    // Obtener el valor del campo weight
    const weightValue = parseFloat(weightInput.value);
    // Obtener el valor del campo minstock
    const minstockValue = parseFloat(minstockInput.value);
    // Obtener el valor de lab
    const labValue = labInput.value;

    // Verificar si la input con id=lab es igual a "LABORATORIO DE QUIMICA"
    // y minstock es vacío o igual a 0
    if (labValue === "LABORATORIO DE QUIMICA" && (minstockValue === 0 || isNaN(minstockValue))) {
        // Mostrar la alerta y colocar el foco en la entrada minstock
        Swal.fire({
            icon: 'warning',
            title: 'Validación de campos',
            text: "Debe registrar un stock mínimo",
            confirmButtonText: 'Aceptar',
            didClose: () => {
                minstockInput.focus();
            }
        });
        // Evitar que se envíe el formulario
        return false;
    }

    // Verificar si el valor de minstock es mayor que weight
    if (minstockValue > weightValue) {
        minstockInput.value = Math.round(weightInput.value / 10);
        // Mostrar la alerta
        Swal.fire({
            icon: 'warning',
            title: 'Coherencia de los campos',
            text: "El valor de Stock Mínimo debe ser menor a la Cantidad a retirar",
            confirmButtonText: 'Aceptar',
            didClose: () => {
                // Posicionar el foco en el campo minstock para que el usuario pueda escribir
                minstockInput.focus();
            }
        });

        // Evitar que se envíe el formulario
        return false;
    }

    // Permitir el envío del formulario
    return true;
}

// Agregar un controlador de eventos al evento submit del formulario
form.addEventListener('submit', validateMinstockSubmit);
