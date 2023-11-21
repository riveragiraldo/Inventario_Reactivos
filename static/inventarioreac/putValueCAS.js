// Obtener el checkbox "Acepta Política"
var aplicaCAS = document.getElementById("aplicaCAS");
var casInput = document.getElementById("cas");
aplicaCAS.addEventListener("change", function () {
    var aplicaCAS = document.getElementById("aplicaCAS");
    var casInput = document.getElementById("cas");

    if (this.checked) {
        aplicaCAS.value = 'Aplica';
        casInput.value = ''
        casInput.readOnly = false;
    } else {
        aplicaCAS.value = 'No Aplica';
        casInput.value = 'NO APLICA'
        casInput.readOnly = true;
    }
});

document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Obtener el elemento del campo CAS
        var casInput = document.getElementById("cas");
        // Obtener el elemento del checkbox
        var aplicaCASCheck = document.getElementById("aplicaCAS");
    
        // Verificar si el valor de CAS es "NO APLICA" después de 500 ms
        if (casInput.value.trim() === "NO APLICA") {
            // Establecer el campo CAS como de solo lectura
            casInput.readOnly = true;
            // Marcar el checkbox como unchecked
            aplicaCASCheck.checked = false;
        }
    }, 250); // 250 ms de retraso
});
