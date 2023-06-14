document.addEventListener('DOMContentLoaded', function () {
    // Obtener los elementos del DOM
    const nameInput = document.getElementById('name');
    const referenceInput = document.getElementById('reference');
    const trademarkInput = document.getElementById('trademark');
    const stockInput = document.getElementById('stock');

    // Manejar el evento de cambio en el primer input
    nameInput.addEventListener('change', function () {
        // Obtener los valores seleccionados en los inputs
        const selectedName = nameInput.value;
        const selectedReference = referenceInput.value;
        const selectedTrademark = trademarkInput.value;
        const selectedLab = document.getElementById('lab').value;

        // Retraso de 1 segundo antes de enviar la solicitud
        setTimeout(function () {
            // Realizar una solicitud AJAX para obtener el valor de weight correspondiente
            fetch(`/api/weight?name=${selectedName}&reference=${selectedReference}&trademark=${selectedTrademark}&lab=${selectedLab}`)
                .then(response => response.json())
                .then(data => {
                    if (data.weight) {
                        // Asignar el valor de weight a la input de stock
                        stockInput.value = data.weight;
                    } else {
                        // Limpiar el valor de stock si no se encuentra un peso correspondiente
                        stockInput.value = '';
                    }
                })
                .catch(error => {
                    //console.log('Error:', error);
                });
        }, 1000);
    });
});
