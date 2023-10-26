$(document).ready(function() {
    // Función para ocultar o mostrar los elementos siguientes
    function alternarSiguientes(elemento) {
        if (elemento.nextAll('li[id^="li_"]').is(':visible')) {
            elemento.nextAll('li[id^="li_"]').hide();
        } else {
            elemento.nextAll('li[id^="li_"]').show();
        }
    }

    // Reactivos
    $("#reactivos_button").click(function() {
        alternarSiguientes($("#li_reactivos"));
    });

    // Inventarios
    $("#inventarios_button").click(function() {
        alternarSiguientes($("#li_inventarios"));
    });

    // Solicitudes
    $("#solicitudes_button").click(function() {
        alternarSiguientes($("#li_solicitudes"));
    });

    // Usuarios
    $("#usuarios_button").click(function() {
        alternarSiguientes($("#li_usuarios"));
    });

    // Administrar
    $("#administrar_button").click(function() {
        alternarSiguientes($("#li_administrar"));
    });
});