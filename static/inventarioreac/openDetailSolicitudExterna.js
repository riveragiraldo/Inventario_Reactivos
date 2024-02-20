// Evento click para mostrar SweetAlert con la información del solicitud
document.querySelectorAll('.solicitud-externa').forEach(element => {
    element.addEventListener('click', function () {
        const solicitudId = this.getAttribute('data-sol-id');
        const solicitudDate = this.getAttribute('data-solicitud-date');
        const solicitudTipoLab = this.getAttribute('data-solicitud-lab');        
        const solicitudTipoSolicitud = this.getAttribute('data-solicitud-tipo');
        const solicitudMensaje = this.getAttribute('data-solicitud-mensaje');
        const solicitudAdjuntos = this.getAttribute('data-solicitud-adjuntos');
        const solicitudAdjuntosUrl = this.getAttribute('data-solicitud-adjuntos-url');
        const solicitudName = this.getAttribute('data-solicitud-nombre');
        const solicitudDepartment = this.getAttribute('data-solicitud-area');
        const solicitudPhoneNumber = this.getAttribute('data-solicitud-telefono');
        const solicitudEmail = this.getAttribute('data-solicitud-email');
        const solicitudEncondedId = this.getAttribute('data-solicitud-encoded-id');
        
        
        
        
        const solicitud = obtenerInformacionSolicitud(solicitudId, solicitudTipoSolicitud, solicitudDate,solicitudTipoLab, solicitudMensaje, solicitudAdjuntos, solicitudAdjuntosUrl, solicitudName, solicitudDepartment, solicitudPhoneNumber, solicitudEmail,solicitudEncondedId);
        mostrarSweetAlert(solicitud);
    });
});

// Función para obtener la información del solicitud basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionSolicitud(solicitud_id, tipo_solicitud, date, lab, mensaje, adjuntos, adjuntos_url, nombres, area, telefono, email, id_codificado) {

    const solicitud = {
        solicitud_id: solicitud_id,
        tipo_solicitud: tipo_solicitud,
        date: date,
        lab: lab,
        mensaje: mensaje,
        adjuntos:adjuntos,
        adjuntos_url:adjuntos_url,
        nombres:nombres,
        area:area,
        telefono:telefono,
        email:email,
        id_codificado:id_codificado,       

    };
    return solicitud;
}

// Función para mostrar la SweetAlert con la información del solicitud
function mostrarSweetAlert(solicitud) {
    const adjuntos = solicitud.adjuntos;
    console.log(adjuntos)
   
    // Define una variable para contener los elementos HTML relacionados con la respuesta.
    let archivos_adjuntos = '';
    if (adjuntos) {
        archivos_adjuntos=`<a href='${solicitud.adjuntos_url}' target='_blank'>${adjuntos}</a>`;
    }else{
        archivos_adjuntos = '';
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
                        <li><strong>Laboratorio al cual va dirigido:</strong> ${solicitud.lab}</li>
                        <li><strong>Fecha de registro:</strong> ${solicitud.date}</li>
                        <li><strong>Asunto:</strong> ${solicitud.tipo_solicitud}</li>
                        <li><strong>Mensaje:</strong> ${solicitud.mensaje}</li>
                        <li><strong>Archivos Adjuntos:</strong> ${archivos_adjuntos}</li>
                        </ul>
                        <br>
                    <h5>Datos del remitente</h5>
                    <ul class="list-unstyled">
                        <li><strong>Nombres y apellidos:</strong> ${solicitud.nombres}</li>
                        <li><strong>Área:</strong> ${solicitud.area}</li>
                        <li><strong>Teléfono:</strong> ${solicitud.telefono}</li>
                        <li><strong>Correo Electrónico:</strong> ${solicitud.email}</li>
                    </ul>
                    
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    }).then(() => {
        solicitudLeida(solicitud.id_codificado, '')
    });
}
