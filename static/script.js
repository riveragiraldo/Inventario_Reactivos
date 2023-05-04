//Fecha actual

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


//autocompletar por nombre o código

$(document).ready(function () {
    
    $("#name").autocomplete({
        source: "{% url 'reactivos:autocomplete' %}",
        minLength: 2,
        select: function (event, ui) {
            $("#name").val(ui.item.value);
            return false;
        }
    });
});

//Función autocompletar por Ubicación
$(document).ready(function () {
    $("#location").autocomplete({
        source: "autocomplete_location", 
        minLength: 2,
        select: function (event, ui) {
            $("#location").val(ui.item.value);
            return false;
        }
    });
});


//Actualiza campos código, cas, is_liquid, unidades    
$(document).ready(function () {
    var updateFields = function () {
        var valueSelected = $('#name').val();
        $.ajax({
            url: '/get-value/',
            data: {
                'value_selected': valueSelected
            },
            dataType: 'json',
            success: function (data) {
                var label = document.querySelector('.form-label[for="weight"]'); // selecciona la etiqueta con el id "weight"
                if (data.liquid === 'SI') {
                    label.innerHTML = 'Volumen:'; // actualiza el texto a "Volumen"
                }
                else if (data.liquid === 'NO') {
                    label.innerHTML = 'Masa:'; // actualiza el texto a "Masa"
                }
                else {
                    label.innerHTML = 'Cantidad:'; // actualiza el texto a "Masa"
                }
                $('#cas').val(data.cas);
                $('#code').val(data.codigo);
                $('#is_liquid').val(data.liquid);
                $('#unit').val(data.nombre_unit);
            }
        });
    };

    $('#name').autocomplete({
        source: '/autocomplete/',
        select: function (event, ui) {
            setTimeout(function(){
                updateFields();
            }, 100);
        },
        minLength: 3
    });
});
