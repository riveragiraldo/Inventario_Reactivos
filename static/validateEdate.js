// Función para formatear la fecha en "dd/mm/aaaa"
function formatDate(date) {
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
}

// Obtener el elemento edate por su ID
const edateInput = document.getElementById('edate');

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

// Agregar un evento blur al campo edate
edateInput.addEventListener('blur', validateEdate);
