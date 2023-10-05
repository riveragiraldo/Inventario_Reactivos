//Función "autocomplete" se utiliza para autocompletar el campo "name" basándose en el valor ingresado en dicho campo.
//El valor escrito se envía a la vista "autocomplete", la cual devuelve una lista de valores de "code", "cas" y "name".
//Estos valores se concatenan y se presentan en un menú desplegable. Al seleccionar uno de ellos, se establece el valor 
//de "name" en el campo correspondiente.

$(document).ready(function () {
    $("#name").autocomplete({
        source: '/autocomplete/',
        minLength: 3,
        select: function (event, ui) {
            // Obtener el código, nombre y CAS del objeto seleccionado
            var code = ui.item.code;
            var name = ui.item.name;
            var cas = ui.item.cas;

            // Concatenar el código, nombre y CAS en un formato deseado
            var optionLabel = code + " - " + name + " - " + cas;

            // Establecer el valor y la etiqueta del campo de entrada
            $("#name").val(optionLabel);

            return false;
        },
        focus: function (event, ui) {
            // Prevenir la actualización del valor del campo de entrada al enfocar una opción
            event.preventDefault();
        },
        response: function (event, ui) {
            // Manipular la respuesta antes de mostrar las opciones
            ui.content.forEach(function (item) {
                // Agregar el código, nombre y CAS al objeto de la opción
                item.label = item.code + " - " + item.name + " - " + item.cas;
                item.value = item.name;  // Establecer el valor de la opción como el nombre
            });
        }
    });
});

$(document).ready(function () {
    $('#name').autocomplete({
        source: '/autocomplete/',
        select: function (event, ui) {
            setTimeout(function () {
                submitForm();
            }, 30);

        },
        minLength: 3
    });

    $('#name').on('input', function () {
        // setTimeout(function () {
        //     submitForm();
        // }, 100);

    });
});

function submitForm() {
    const formulario = document.forms["listadoReactivos"];
    formulario.submit();

}
