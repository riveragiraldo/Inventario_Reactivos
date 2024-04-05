function limpiarCampos(formularioName) {
    // Si es una ventana padre, realiza la acción de limpiar campos
    const formulario = document.forms[formularioName];

    if (formulario) {
        // Recorrer y limpiar todos los campos del formulario
        const campos = formulario.querySelectorAll('input, textarea, select');
        campos.forEach((campo) => {
            
            if (campo.tagName.toLowerCase() === 'select') {
                // Si es un elemento select, establecer el valor en ''
                campo.value = '';
            } else {
                // Para otros campos, establecer el valor como cadena vacía
                campo.value = '';
            }
            if (campo.id=='lab'){
                campo.value=labDefault  
            }
        });

        // Después de limpiar los campos, realiza la función de submit en el formulario
        formulario.submit();
    }
}


