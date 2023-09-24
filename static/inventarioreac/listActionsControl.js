// Abre formulario de agregar entrada de reactvi
function openPopupAdd(url) {
    // Define las dimensiones y otras opciones de la ventana emergente
    var width = 800;
    var height = 600;
    var left = (window.innerWidth - width) / 2;
    var top = (window.innerHeight - height) / 2;
    var options = 'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=' + width + ',height=' + height + ',top=' + top + ',left=' + left;

    // Abre la ventana emergente con la URL proporcionada
    window.open(url, 'popup', options);
}

//Abre formulario de Edición  registro de entrada de reactivo

function openEditFormIn(itemId) {
    // Construye la URL del formulario de edición con el ID del elemento
    var editUrl = '/reactivos/editar_entrada/' + itemId + '/';

    // Abre una nueva ventana emergente con el formulario de edición
    window.open(editUrl, '_blank', 'width=600,height=800');
}

//Abre formulario de Edición  registro de salida de reactivo

function openEditFormOut(itemId) {
    // Construye la URL del formulario de edición con el ID del elemento
    var editUrl = '/reactivos/editar_salida/' + itemId + '/';

    // Abre una nueva ventana emergente con el formulario de edición
    window.open(editUrl, '_blank', 'width=600,height=800');
}

// SOlicitud para eliminar el registro correspondiente
function confirmDeleteIn(itemId, itemName) {
    // Muestra una Sweet Alert de confirmación
    Swal.fire({
        title: '¿Está seguro que desea eliminar el registro número:'+itemId+' "' + itemName + '"?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sí',
        cancelButtonText: 'No',
    }).then((result) => {
        if (result.isConfirmed) {
            // Si el usuario hace clic en "Sí", realiza una solicitud AJAX para eliminar la entrada
            var deleteUrl = '/reactivos/eliminar_entrada/' + itemId + '/';
            
            fetch(deleteUrl, {
                method: 'POST', // O el método HTTP que estés utilizando
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), // Asegúrate de incluir el token CSRF si estás utilizando Django
                },
            })
            .then(response => {
                // Verificar el estado de la respuesta y capturar el mensaje
                if (response.ok) {
                    return response.text();
                } else {
                    throw new Error('Error al eliminar el registro');
                }
            })
            .then(data => {
                icono = 'warning'

                // Mostrar el mensaje de éxito
                Swal.fire({
                    icon: icono,
                    title: 'Mensaje del servidor',
                    text: data,
                }).then(() => {
                    // Recargar la página o realizar otras acciones si es necesario
                    location.reload(); // Recarga la página después de eliminar
                });
            })
            .catch(error => {
                // Manejar errores de la solicitud AJAX
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Ocurrió un error al eliminar el registro',
                });
                location.reload();
            });
        } else {
            // Si el usuario hace clic en "No", cierra la Sweet Alert
            Swal.close();
        }
    });
}

// Función para obtener el token CSRF de las cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Buscar el nombre de la cookie
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}