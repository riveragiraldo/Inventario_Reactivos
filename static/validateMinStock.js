// Obtener el elemento weight por su ID
const weightInput = document.getElementById('weight');
// Obtener el elemento minstock por su ID
const minstockInput = document.getElementById('minstock');

// Agregar un evento input al campo weight
minstockInput.addEventListener('input', () => {
    // Obtener el valor del campo weight
    const weightValue = parseFloat(weightInput.value);



    // Verificar si el valor de weight es igual a 0
    if (weightValue <= 0 || isNaN(weightValue)) {
        // Mostrar la alerta
        alert('Escriba primero cantidad a retirar');

        // Establecer el valor del campo minstock en 0
        minstockInput.value = '0';
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
        // Mostrar la alerta
        alert('El valor de Stock Mínimo debe ser menor a la cantidad a retirar.');
        minstockInput.value=weightInput.value/10


    }
}

// Agregar un evento blur al campo minstock
minstockInput.addEventListener('blur', validateMinstock);

// Agregar un evento blur al campo minstock
weightInput.addEventListener('blur', validateMinstock);

// Función para validar el campo minstock
function validateMinstockSubmit() {
    // Obtener el valor del campo weight
    const weightValue = parseFloat(weightInput.value);
    // Obtener el valor del campo minstock
    const minstockValue = parseFloat(minstockInput.value);

    // Verificar si el valor de minstock es mayor que weight
    if (minstockValue > weightValue) {
        // Mostrar la alerta
        alert('El valor de Stock Mínimo debe ser menor a la cantidad a retirar.');
        minstockInput.value=weightInput.value/10

        // Evitar que se envíe el formulario
        return false;
    }

    // Permitir el envío del formulario
    return true;
}

// Agregar un controlador de eventos al evento submit del formulario
form.addEventListener('submit', validateMinstockSubmit);