document.addEventListener("DOMContentLoaded", function () {
    // Función para enviar la solicitud AJAX y actualizar el campo "stock"
    function obtenerStock() {
        var lab = document.getElementById("lab").value;
        var name = document.getElementById("name").value;
        var trademark = document.getElementById("trademark").value;
        var reference = document.getElementById("reference").value;
        
        
        
        

        // Validar que todos los campos tengan un valor
        if (!lab || !name || !trademark || !reference) {
            alert("Por favor, complete los campos nombre, marca y referencia");
            return;
        }

        // Realizar la solicitud AJAX a la vista "obtener_stock"
        var xhr = new XMLHttpRequest();
        xhr.open(
            "GET",
            "/obtener_stock/?lab=" +
            lab +
            "&name=" +
            name +
            "&trademark=" +
            trademark +
            "&reference=" +
            reference,
            true
        );
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Obtener el stock devuelto por la vista
                    var response = JSON.parse(xhr.responseText);
                    if (response.stock === null || xhr.status === 404) {
                        // Mostrar alerta cuando se recibe un valor "none" o 404
                        alert("Los campos no coinciden. Por favor, verifique.");
                        document.getElementById("stock").value = 0;
                    } else {
                        var stock = Math.floor(response.stock.weight);
                        // Actualizar el campo "stock" con el valor obtenido
                        document.getElementById("stock").value = stock;
                    }
                } else {
                    console.log("Error:", xhr.statusText);
                }
            }
        };
        xhr.send();
    }

    // Asignar un evento al clic en el span "Ver"
    document.getElementById("stock-view").addEventListener("click", function () {
        obtenerStock();
    });
});