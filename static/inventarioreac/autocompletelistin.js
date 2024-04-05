
// Autocoompleta teniendo en cuenta el laboratorio pero manejado con id

$(document).ready(function () {
    $('#name').autocomplete({
        source: function (request, response) {
            var term = request.term;
            var lab = $('#lab').val();
            $.getJSON('/autocomplete_react/', { term: term, lab: lab })
                .done(function (data) {
                    response(data);
                });
        },
        response: function (event, ui) {
            // Manipular la respuesta antes de mostrar las opciones
            ui.content.forEach(function (item) {
                // Agregar el código, nombre y CAS al objeto de la opción
                item.label = item.code + " - " + item.name + " - " + item.cas;
                item.value = item.name;  // Establecer el valor de la opción como el nombre
            });
        },
        select: function (event, ui) {
            var name = ui.item.name;
            var id_react = ui.item.id;

            $("#name").val(name);
            $("#id_r").val(id_react);

            setTimeout(function () {
                submitForm();
            }, 30);
        },
        minLength: 3
    });

    $('#name').on('input', function () {
        // Puedes agregar lógica adicional aquí si es necesario
        // setTimeout(function () {
        //     submitForm();
        // }, 100);
    });
});

function submitForm() {
    const formulario = document.forms["listadoReactivos"];
    formulario.submit();

}