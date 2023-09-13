// Evento click para mostrar SweetAlert con la información del reactivo
document.querySelectorAll('.detalle-reactivo').forEach(element => {
    element.addEventListener('click', function () {
        const reactivoId = this.getAttribute('data-reactivo-id');
        const reactivoName = this.getAttribute('data-reactivo-name');
        const reactivoCode = this.getAttribute('data-reactivo-code');
        const reactivoCas = this.getAttribute('data-reactivo-cas');
        const reactivoTrademark = this.getAttribute('data-reactivo-trademark');
        const reactivoReference = this.getAttribute('data-reactivo-reference');
        const reactivoQuantity = this.getAttribute('data-reactivo-quantity');
        const reactivoUnit = this.getAttribute('data-reactivo-unit');
        const reactivoWlocation = this.getAttribute('data-reactivo-wlocation');
        const reactivoLab = this.getAttribute('data-reactivo-lab');
        const reactivoEdate = this.getAttribute('data-reactivo-edate');
        const reactivoRespel = this.getAttribute('data-reactivo-respel');
        const reactivoSga = this.getAttribute('data-reactivo-sga');
        const reactivoState = this.getAttribute('data-reactivo-state');
        const reactivo = obtenerInformacionReactivo(reactivoId, reactivoName, reactivoCode, reactivoCas, reactivoTrademark, reactivoReference, reactivoQuantity, reactivoUnit, reactivoWlocation, reactivoLab,reactivoEdate,reactivoRespel,reactivoSga,reactivoState);
        mostrarSweetAlert(reactivo);
    });
});

// Función para obtener la información del reactivo basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionReactivo(reactivo, name, code, cas, trademark, reference, quantity, unit, wlocation,lab,edate,respel,sga,state) {

    const inventario = {
        id: reactivo,
        name: name,
        code: code,
        cas: cas,
        respel: respel,
        sga: sga,
        trademark: trademark,
        reference: reference,
        weight: quantity,
        unit: unit,
        edate: edate,
        wlocation: wlocation,
        lab: lab,
        state: state
    };
    return inventario;
}

// Función para mostrar la SweetAlert con la información del reactivo
function mostrarSweetAlert(inventario) {
    Swal.fire({
        icon: 'info',
        title: `Detalle del reactivo ${inventario.name}`,
        html: `
            <div class="card" style="text-align: left;">
                <div class="card-header">
                    Detalle del reactivo ${inventario.name} en ${inventario.lab}
                </div>
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Id de inventario:</strong> ${inventario.id}</li>
                        <li><strong>Nombre:</strong> ${inventario.name}</li>
                        <li><strong>Código Interno:</strong> ${inventario.code}</li>
                        <li><strong>CAS:</strong> ${inventario.cas}</li>
                        <li><strong>Estado:</strong> ${inventario.state}</li>
                        <li><strong>Clasificación Respel:</strong> ${inventario.respel}</li>
                        <li><strong>Codificación SGA:</strong> ${inventario.sga}</li>
                        <li><strong>Marca:</strong> ${inventario.trademark}</li>
                        <li><strong>Referencia:</strong> ${inventario.reference}</li>
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Cantidad en almacén:</strong> ${inventario.weight} ${inventario.unit}</li>
                        <li><strong>Fecha de vencimiento:</strong> ${inventario.edate}</li>
                        <li><strong>Ubicación en almacén:</strong> ${inventario.wlocation}</li>
                        <li><strong>Laboratorio:</strong> ${inventario.lab}</li>
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
