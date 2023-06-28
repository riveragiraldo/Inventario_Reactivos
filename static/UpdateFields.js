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
            var label = document.querySelector('.form-label[for="weight"]');
            
            $('#cas').val(data.cas);
            $('#code').val(data.codigo);
            $('#is_liquid').val(data.liquid);
            $('#unit').val(data.nombre_unit);
        }
    });
};