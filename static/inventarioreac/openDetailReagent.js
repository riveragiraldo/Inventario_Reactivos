// Evento click para mostrar SweetAlert con la información del reactivo
document.querySelectorAll('.detalle-reactivo').forEach(element => {
    element.addEventListener('click', function () {
        const reactivoId = this.getAttribute('data-reactivo-id');        
        const reactivoName = this.getAttribute('data-reactivo-name');
        const reactivoColor = this.getAttribute('data-reactivo-color');
        const reactivoNumber = this.getAttribute('data-reactivo-number');
        const reactivoSubNumber = this.getAttribute('data-reactivo-subnumber');
        const reactivoCode = this.getAttribute('data-reactivo-code');
        const reactivoCas = this.getAttribute('data-reactivo-cas');
        const reactivoRespel = this.getAttribute('data-reactivo-respel');
        const reactivoSGA = this.getAttribute('data-reactivo-sga');
        const reactivoState = this.getAttribute('data-reactivo-state');
        const reactivoUnit = this.getAttribute('data-reactivo-unit');
        const reactivoIsActive = this.getAttribute('data-reactivo-active');
        const reactivoDateCreate = this.getAttribute('data-reactivo-date_create');
        const reactivoCreateBy = this.getAttribute('data-reactivo-create_by');
        const reactivoLastUpdate = this.getAttribute('data-reactivo-lastupdate');
        const reactivoLastUpdateBy = this.getAttribute('data-reactivo-update_by');
        
        const reactivo = obtenerInformacionReactivo(reactivoId, reactivoName, reactivoColor, reactivoNumber, reactivoSubNumber, reactivoCode, reactivoCas, reactivoRespel,reactivoSGA,reactivoState,reactivoUnit,reactivoIsActive,reactivoDateCreate,reactivoCreateBy,reactivoLastUpdate,reactivoLastUpdateBy);
        mostrarSweetAlert(reactivo);
    });
});

// Función para obtener la información del reactivo basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionReactivo(id, name, color, number, subnumber, code, cas, respel,sga,state,unit,is_active,date_create,create_by,last_update,update_by) {

    const reactivo = {
        id: id,
        name: name,
        color: color,
        number: number,
        subnumber: subnumber,
        code: code,
        cas: cas,
        respel: respel,
        sga: sga,
        state: state,
        unit: unit,
        is_active: is_active,
        date_create: date_create,
        create_by: create_by,
        last_update: last_update,
        update_by: update_by,

    };
    return reactivo;
}

// Función para mostrar la SweetAlert con la información del reactivo
function mostrarSweetAlert(reactivo) {
    Swal.fire({
        icon: 'info',
        title: `Reactivo  ${reactivo.name}`,
        html: `
            <div class="card" style="text-align: left;">
                <div class="card-header">
                    Detalle del reactivo ${reactivo.name}
                </div>
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Id de registro salida:</strong> ${reactivo.id}</li>
                        <li><strong>Nombre:</strong> ${reactivo.name}</li>
                        <li><strong>Color:</strong> ${reactivo.color}</li>
                        <li><strong>Número:</strong> ${reactivo.number}</li>
                        <li><strong>Subnumero:</strong> ${reactivo.number}</li>
                        <li><strong>Código:</strong> ${reactivo.code}</li>
                        <li><strong>CAS:</strong> ${reactivo.cas}</li>
                        <li><strong>Clasificación Respel:</strong> ${reactivo.respel}</li>
                        <li><strong>Codificación SGA:</strong> ${reactivo.sga}</li>
                        <li><strong>Estado:</strong> ${reactivo.state}</li>
                        <li><strong>Unidades:</strong> ${reactivo.unit}</li>
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Estado:</strong> ${reactivo.is_active}</li>
                        <li><strong>Fecha de registro:</strong> ${reactivo.date_create}</li>
                        <li><strong>Responsable del registro:</strong> ${reactivo.create_by}</li>
                        <li><strong>Última modificación:</strong> ${reactivo.last_update}</li>
                        <li><strong>Última actualización por:</strong> ${reactivo.update_by}</li>
                        
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
