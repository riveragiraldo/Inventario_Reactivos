//Función "autocomplete" se utiliza para autocompletar el campo "name" basándose en el valor ingresado en dicho campo.
//El valor escrito se envía a la vista "autocomplete", la cual devuelve una lista de valores de "code", "cas" y "name".
//Estos valores se concatenan y se presentan en un menú desplegable. Al seleccionar uno de ellos, se establece el valor 
//de "name" en el campo correspondiente.

$(document).ready(function () {
    $("#name").autocomplete({
        source: "{% url 'reactivos:autocomplete' %}",
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
        source: '/autocomplete/',
        select: function (event, ui) {
            setTimeout(function () {
                updateFields();
            }, 100);
        },
        minLength: 3
    });

    $('#name').on('input', function () {
        setTimeout(function () {
            updateFields();
        }, 100);
    });
});

//Función "autocomplete_location" se encarga de autocompletar el campo "location" basándose en el valor ingresado en 
//dicho campo. Se envía este valor a la vista "autocomplete_location", la cual devuelve una lista de nombres de 
//ubicaciones asociadas. Estos nombres se presentan en un menú desplegable y, al seleccionar uno de ellos, se establece 
//dicho valor de ubicación en el campo "location".


$(document).ready(function () {
    $("#location").autocomplete({
        source: "/autocomplete_location/",
        minLength: 2,
        select: function (event, ui) {
            // Muestra el nombre y correo electrónico en la lista desplegable
            $("#location").val(ui.item.name);
            $("#facultad").val(ui.item.facultad);
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
            $("#location").val(ui.item.name);
            $("#facultad").val(ui.item.facultad);
            return false;
        }
    });
});


//Función "autocomplete_manager" se encarga de autocompletar el campo "manager" basándose en el valor ingresado en el 
//campo "location".Utiliza una vista llamada "autocomplete_manager" que devuelve los nombres de los responsables 
//correspondientes.Estos nombres se muestran en una lista desplegable y, al seleccionar uno, se establece el nombre 
//del responsable en el campo "manager".
 

    $(document).ready(function () {
        $("#manager").autocomplete({
            source: "/autocomplete_manager/",
            minLength: 2,
            select: function (event, ui) {
                // Muestra el nombre y correo electrónico en la lista desplegable
                $("#manager").val(ui.item.name);
                $("#correo").val(ui.item.mail);
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
     


//Actualizar campos: segun la entrada en el campo name envía valor a la vista def get_value(request) y este devuelve 
//valor de cas, ceode, is_liquid y unit y los actualiza en los campos correspondientes

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
