//autocompletar por nombre o código
//Envía valores escritos en el campo name a la vista AutocompleteOutAPI, esta devuelve los valores de code cas y name, se concatenan y 
//se visualizan en forma de lista desplegable 
$(document).ready(function () {
    $("#name").autocomplete({
        source: "{% url 'reactivos:autocomplete_out' %}",
        minLength: 2,
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
        source: function (request, response) {
            var term = request.term;
            var lab = $('#lab').val();
            

            $.getJSON('/autocomplete_out/', { term: term, lab: lab })
                .done(function (data) {
                    response(data);
                });
        },
        select: function (event, ui) {
            // Obtener el código, nombre y CAS del objeto seleccionado
            var code = ui.item.code;
            var name = ui.item.name;
            var cas = ui.item.cas;

            // Concatenar el código, nombre y CAS en un formato deseado
            var optionLabel = code + " - " + name + " - " + cas;

            // Establecer el valor y la etiqueta del campo de entrada
            $("#name").val(optionLabel);


            setTimeout(function () {
                updateFields();
            }, 100);
        },
        minLength: 2
    });
});


$('#name').on('input', function () {
    setTimeout(function () {
        updateFields();
    }, 100);
});


//Función autocompletar por Ubicación
//Envía valores escritos en el campo location a la vista Autocomplete_location, esta devuelve los valores de location y 
//se visualizan en forma de lista desplegable 
$(document).ready(function () {
    $("#location").autocomplete({
        source: "/autocomplete_location/",
        minLength: 2,
        select: function (event, ui) {
            // Muestra el nombre y correo electrónico en la lista desplegable
            $("#location").val(ui.item.name);
            return false;
        },
        create: function () {
            // Muestra solo el nombre en la lista desplegable
            $(this).data('ui-autocomplete')._renderItem = function (ul, item) {
                var facultadIniciales = item.facultad.split(' ').map(word => word[0]).join('').toUpperCase();
                
                return $("<li>")
                    .append($("<div>").text(item.name + ' (' + facultadIniciales + ')'))
                    .appendTo(ul);
            };
        },
        focus: function (event, ui) {
            // Muestra solo el nombre en el campo de entrada mientras se desplaza por la lista desplegable
            $("#locarion").val(ui.item.name);
            $("#facultad").val(ui.item.facultad);
            return false;
        }
    });
});


//Envía valores escritos en el campo maneger a la vista Autocomplete_manager, esta devuelve los valores de manager
//se visualizan en forma de lista desplegable 
//Función autocompletar por Responsable


$(document).ready(function () {
    $("#manager").autocomplete({
        source: "/autocomplete_manager/",
        minLength: 2,
        select: function (event, ui) {
            // Muestra el nombre y correo electrónico en la lista desplegable
            $("#manager").val(ui.item.name);
            return false;
        },
        create: function () {
            // Muestra solo el nombre en la lista desplegable
            $(this).data('ui-autocomplete')._renderItem = function (ul, item) {
                return $("<li>")
                    .append($("<div>").text(item.name + ' (' + item.mail + ')'))
                    .appendTo(ul);
            };
        },
        focus: function (event, ui) {
            // Muestra solo el nombre en el campo de entrada mientras se desplaza por la lista desplegable
            $("#manager").val(ui.item.name);
            $("#correo").val(ui.item.mail);
            return false;
        }
    });
});


//Actualizar campos
//Dependiendo del valor autocompletado  en el campo name envía a la vista get-value, esta devuelve los valores de code cas state y unir
//y los escribe en los campos correspondientes
function updateFields() {
    var valueSelected = $('#name').val();
    $.ajax({
        url: '/get-value/',
        data: {
            'value_selected': valueSelected
        },
        dataType: 'json',
        success: function (data) {
            $('#cas').val(data.cas);
            $('#code').val(data.codigo);
            $('#is_liquid').val(data.liquid);
            $('#unit').val(data.nombre_unit);
        }
    });
};



