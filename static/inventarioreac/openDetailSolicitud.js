// Evento click para mostrar SweetAlert con la información del solicitud
document.querySelectorAll('.detalle-reactivo').forEach(element => {
    element.addEventListener('click', function () {
        const solicitudId = this.getAttribute('data-solicitud-id');
        const solicitudDate = this.getAttribute('data-solicitud-date');        
        const solicitudTipoSolicitud = this.getAttribute('data-solicitud-tipo');
        const solicitudMensaje = this.getAttribute('data-solicitud-mensaje');
        
        const solicitudUsuarioSolicitud = this.getAttribute('data-solicitud-usuario_solicitud');
        const solicitudUsuarioLab = this.getAttribute('data-solicitud-laboratorio');
        const solicitudUsuarioPhone = this.getAttribute('data-solicitud-telefono');
        const solicitudUsuarioEmail = this.getAttribute('data-solicitud-email');
        const solicitudDateCreate = this.getAttribute('data-solicitud-date_create');
        const solicitudTramitado = this.getAttribute('data-solicitud-tramitado');
        const solicitudRespuesta = this.getAttribute('data-solicitud-respuesta');
        const solicitudUsuarioTramita = this.getAttribute('data-solicitud-usuario-tramita');
        const solicitudFechaTramite = this.getAttribute('data-solicitud-fecha-tramite');
        const solicitudCreateBy = this.getAttribute('data-solicitud-create_by');
        const solicitudLastUpdate = this.getAttribute('data-solicitud-lastupdate');
        const solicitudLastUpdateBy = this.getAttribute('data-solicitud-update_by');
        const solicitud = obtenerInformacionSolicitud(solicitudId, solicitudTipoSolicitud, solicitudDate, solicitudMensaje, solicitudUsuarioSolicitud, solicitudUsuarioLab, solicitudUsuarioPhone, solicitudUsuarioEmail,solicitudDateCreate, solicitudTramitado,solicitudRespuesta,solicitudUsuarioTramita,solicitudFechaTramite,solicitudCreateBy,solicitudLastUpdate,solicitudLastUpdateBy);
        mostrarSweetAlert(solicitud);
    });
});

// Función para obtener la información del solicitud basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionSolicitud(solicitud_id, tipo_solicitud, date, mensaje, usuario, usuario_lab, usuario_tel, usuario_email,date_create,tramitado,respuesta,usuario_tramita,fecha_tramite,create_by,last_update,update_by) {

    const solicitud = {
        solicitud_id: solicitud_id,
        tipo_solicitud: tipo_solicitud,
        date: date,
        mensaje: mensaje,
        usuario: usuario,
        usuario_lab: usuario_lab,
        usuario_tel: usuario_tel,
        date_create: date_create,
        usuario_email: usuario_email,
        tramitado: tramitado,
        respuesta: respuesta,
        usuario_tramita: usuario_tramita,
        fecha_tramite: fecha_tramite,
        create_by: create_by,
        last_update: last_update,
        update_by: update_by,
        

    };
    return solicitud;
}

// Función para mostrar la SweetAlert con la información del solicitud
function mostrarSweetAlert(solicitud) {
    const tramitado = solicitud.tramitado;
   
    // Define una variable para contener los elementos HTML relacionados con la respuesta.
    let respuestaElements = '';
    if (tramitado === 'Tramitado') {
        respuestaElements = `
            <li><strong>Respuesta:</strong> <p>${solicitud.respuesta}<p></li>
            <li><strong>Fecha de respuesta:</strong> ${solicitud.fecha_tramite}</li>
            <li><strong>Usuario que tramita:</strong> ${solicitud.usuario_tramita}</li>
        `;
    }

    Swal.fire({
        icon: 'info',
        title: `Detalle de solicitud`,
        html: `
            <div class="card" style="text-align: left;">
                <div class="card-header">
                    Detalle de registro de solicitud número ${solicitud.solicitud_id} de ${solicitud.date}
                </div>
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Consecutivo:</strong> ${solicitud.solicitud_id}</li>
                        <li><strong>Fecha de registro:</strong> ${solicitud.date}</li>
                        <li><strong>Solicitud:</strong> ${solicitud.tipo_solicitud}</li>
                        <li><strong>Mensaje:</strong> <p>${solicitud.mensaje}</p></li>
                        <li><strong>Usuario que realiza la solicitud:</strong> ${solicitud.usuario}</li>
                        <li><strong>Laboratorio:</strong> ${solicitud.usuario_lab}</li>
                        <li><strong>Teléfono:</strong> ${solicitud.usuario_tel}</li>
                        <li><strong>Correo Elecrtónico:</strong> ${solicitud.usuario_email}</li>
                    </ul>
                    <br>
                    <h5>Trámite de la solicitud:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Estado del trámite:</strong> ${solicitud.tramitado}</li>
                        ${respuestaElements}
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Fecha de registro:</strong> ${solicitud.date_create}</li>
                        <li><strong>Responsable del registro:</strong> ${solicitud.create_by}</li>
                        <li><strong>Última modificación:</strong> ${solicitud.last_update}</li>
                        <li><strong>Última actualización por:</strong> ${solicitud.update_by}</li>
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
