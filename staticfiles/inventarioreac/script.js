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

