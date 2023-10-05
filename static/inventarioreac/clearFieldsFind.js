// Si la ventana es emergente al cancelar se cierra, si la venana es normal, limpia los campos

function limpiarCampos(formularioName) {
    // Si es una ventana padre, realiza la acción de limpiar campos
    const formulario = document.forms[formularioName];
    
    

    if (formulario) {
        // Recorrer y limpiar todos los campos del formulario
        const campos = formulario.querySelectorAll('input, textarea');
        campos.forEach((campo) => {
            campo.value = ''; // Establecer el valor del campo como cadena vacía
        });
        // Después de limpiar los campos, realiza la función de submit en el formulario
        formulario.submit();
    }

}