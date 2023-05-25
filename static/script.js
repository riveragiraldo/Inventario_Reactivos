//Fecha actual

document.addEventListener('DOMContentLoaded', function() {
    limpiarCamposin();
});



function limpiarCamposin() {
    document.getElementById("in_form").reset();
    
    
    $(document).ready(function () {
        var now = new Date();
        var year = now.getFullYear();
        var month = now.getMonth() + 1;
        var day = now.getDate();
        var hours = now.getHours();
        var minutes = now.getMinutes();
        var seconds = now.getSeconds();
        var formattedDate = year + '-' + padNumber(month) + '-' + padNumber(day) + ' ' + padNumber(hours) + ':' + padNumber(minutes) + ':' + padNumber(seconds);
        $('#date').val(formattedDate);
    });

    function padNumber(num) {
        return num < 10 ? '0' + num : num;
    }

    document.getElementById("date").value = $('#date')
}

//autocompletar por nombre o código

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






//Función autocompletar por Ubicación
$(document).ready(function () {
    $("#location").autocomplete({
        source: "autocomplete_location/",
        minLength: 2,
        select: function (event, ui) {
            $("#location").val(ui.item.value);
            return false;
        }
    });
});

//Función autocompletar por Responsable
$(document).ready(function () {
    $("#manager").autocomplete({
        source: "autocomplete_manager/",
        minLength: 2,
        select: function (event, ui) {
            $("#manager").val(ui.item.value);
            return false;
        }
    });
});


//Actualizar campos

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

