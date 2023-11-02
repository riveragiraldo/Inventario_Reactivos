function limpiarCampos(formularioName) {
    // Verificar si la ventana actual es una ventana emergente
    const isPopup = window.opener != null;

    if (!isPopup) {
        // Si es una ventana padre, realiza la acción de limpiar campos
        const formulario = document.forms[formularioName];

        if (formulario) {
            // Recorrer y limpiar todos los campos del formulario, excepto los de tipo "button"
            const campos = formulario.querySelectorAll('input, textarea, select');
            campos.forEach((campo) => {
                if (campo.type !== 'button') {
                    if (campo.tagName === 'SELECT') {
                        // Si es un campo select, restablecerlo a su valor predeterminado
                        campo.selectedIndex = 0; // Establecer el índice seleccionado al valor predeterminado (generalmente 0)
                    } else {
                        // Para otros campos (input y textarea), establecer el valor como cadena vacía
                        campo.value = '';
                    }
                }
            });
        }
    } else {
        // Si es una ventana emergente, cierra la ventana actual
        window.close();
    }
}


function limpiarCamposSol(formularioName) {
    // Verificar si la ventana actual es una ventana emergente
    const isPopup = window.opener != null;

    if (!isPopup) {
        // Si es una ventana padre, realiza la acción de limpiar campos
        const formulario = document.forms[formularioName];

        if (formulario) {
            // Recorrer y limpiar todos los campos del formulario, excepto los de tipo "button"
            const observations = document.getElementById('observations')
            observations.value = ''

        } else {
            // Si es una ventana emergente, cierra la ventana actual
            window.close();
        }
    }
}