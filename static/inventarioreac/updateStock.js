document.addEventListener("DOMContentLoaded", function () {
    // Función para enviar la solicitud AJAX y actualizar el campo "stock"


    function obtenerStock() {
        var lab = document.getElementById("lab").value;
        var nameInput = document.getElementById("name").value;
        var trademark = document.getElementById("trademark").value;
        var reference = document.getElementById("reference").value;


        // Validar que todos los campos tengan un valor
        if (!lab || !nameInput || !trademark || !reference) {
            Swal.fire({
                icon: 'warning',
                title: 'Campos no diligenciados',
                text: "Por favor complete los campos Nombre, Marca y Referencia",
                confirmButtonText: 'Aceptar',
            });
            return;
        }

        // Realizar la solicitud AJAX a la vista "obtener_stock"
        var xhr = new XMLHttpRequest();
        xhr.open(
            "GET",
            "/obtener_stock/?lab=" + lab + "&name=" + nameInput + "&trademark=" + trademark + "&reference=" + reference, true
        );
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                
                if (xhr.status === 404) {
                    // Mostrar alerta cuando se recibe un valor "none" o 404
                    Swal.fire({
                        icon: 'warning',
                        title: 'Mensaje del servidor',
                        text: "El reactivo "+nameInput+" no se encuentra en la base de datos, los valores no coinciden, por favor verifique",
                        confirmButtonText: 'Aceptar',
                        
                    });
                    document.getElementById("stock").value = 0;
                }
                else if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    var stock = Math.floor(response.stock.weight);
                    // Actualizar el campo "stock" con el valor obtenido
                    document.getElementById("stock").value = stock;
                }
                else {
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