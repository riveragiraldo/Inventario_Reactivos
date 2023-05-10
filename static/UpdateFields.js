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
            var label = document.querySelector('.form-label[for="weight"]');
            if (data.liquid === 'SI') {
                label.innerHTML = 'Volumen:';
            }
            else if (data.liquid === 'NO') {
                label.innerHTML = 'Masa:';
            }
            else {
                label.innerHTML = 'Cantidad:';
            }
            $('#cas').val(data.cas);
            $('#code').val(data.codigo);
            $('#is_liquid').val(data.liquid);
            $('#unit').val(data.nombre_unit);
        }
    });
};