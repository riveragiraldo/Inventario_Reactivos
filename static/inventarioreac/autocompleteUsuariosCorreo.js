//autocompletar por nombre o código
//Envía valores escritos en el campo name a la vista AutocompleteOutAPI, esta devuelve los valores de code cas y name, se concatenan y 
//se visualizan en forma de lista desplegable 
$(document).ready(function () {
    $("#id_usuario").autocomplete({
        source: "{% url 'reactivos:autocomplete_user' %}",
        minLength: 2,
        select: function (event, ui) {
            // Obtener el Nombres del objeto seleccionado
            var first_name = ui.item.first_name;
            var last_name = ui.item.last_name;
            var email = ui.item.email;
            var id_user = ui.item.id_user;

            // Concatenar el Nombres en un formato deseado
            var optionLabel = first_name + " " + last_name + " - " + email;

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
                item.label = item.first_name + " " + item.last_name + " - " + item.email;
                item.value = item.email;  // Establecer el valor de la opción como el nombre
            });
        }
    });
});



$(document).ready(function () {
    $('#id_usuario').autocomplete({
        source: function (request, response) {
            var term = request.term;
            var lab = $('#lab').val();


            $.getJSON('/autocomplete_user/', { term: term, lab: lab })
                .done(function (data) {
                    response(data);
                });
        },
        select: function (event, ui) {
            // Obtener el NOmbres del objeto seleccionado
            var first_name = ui.item.first_name;
            var last_name = ui.item.last_name;
            var email = ui.item.email;
            var id_user = ui.item.id_user;


            // Concatenar el Nombres en un formato deseado
            var optionLabel = first_name + " " + last_name;

            // Establecer el valor y la etiqueta del campo de entrada
            $("#id_usuario").val(optionLabel);
            

            // Evento blur para verificar y corregir el campo name
            $('#name').on('blur', function () {
                var currentValue = $(this).val();
                nombreAnterior = optionLabel
                // Si el campo name se borra, también borra #id_user
                if (currentValue !== "") {



                if (currentValue !== nombreAnterior) {
                    // Si el valor actual no coincide con la opción autocompletada
                    $(this).val(nombreAnterior); // Corrige el valor
                }
            }
        });

   
},
    minLength: 2

    });

});




function submitForm() {
    const formulario = document.forms["listadoUsuarios"];
    formulario.submit();

}


