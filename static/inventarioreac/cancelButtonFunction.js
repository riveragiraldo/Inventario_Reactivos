// Si la ventana es emergente al cancelar se cierra, si la venana es normal, limpia los campos

function limpiarCampos(formularioName) {
    // Verificar si la ventana actual es una ventana emergente
    const isPopup = window.opener != null;

    if (!isPopup) {
        // Si es una ventana padre, realiza la acción de limpiar campos
        const formulario = document.forms[formularioName];

        if (formulario) {
            // Recorrer y limpiar todos los campos del formulario
            const campos = formulario.querySelectorAll('input, textarea');
            campos.forEach((campo) => {
                campo.value = ''; // Establecer el valor del campo como cadena vacía
            });
        }
    } else {
        // Si es una ventana emergente, cierra la ventana actual
        window.close();
    }
}