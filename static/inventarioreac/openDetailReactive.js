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
        const reactivoMinStock = this.getAttribute('data-reactivo-minstock');
        const reactivoUnit = this.getAttribute('data-reactivo-unit');
        const reactivoWlocation = this.getAttribute('data-reactivo-wlocation');
        const reactivoLab = this.getAttribute('data-reactivo-lab');
        const reactivoEdate = this.getAttribute('data-reactivo-edate');
        const reactivoAI = this.getAttribute('data-reactivo-almacenamiento_interno');
        const reactivoCA = this.getAttribute('data-reactivo-clase_almacenamiento');
        const reactivoState = this.getAttribute('data-reactivo-state');
        const reactivoCreateBy = this.getAttribute('data-reactivo-create_by');
        const reactivoLastUpdate = this.getAttribute('data-reactivo-lastupdate');
        const reactivoLastUpdateBy = this.getAttribute('data-reactivo-update_by');
        const reactivoDateCreate = this.getAttribute('data-reactivo-date_create');
        const reactivo = obtenerInformacionReactivo(reactivoId, reactivoName, reactivoCode, reactivoCas, reactivoTrademark, reactivoReference, reactivoQuantity, reactivoUnit, reactivoWlocation, reactivoLab,reactivoEdate,reactivoAI,reactivoCA,reactivoState,reactivoCreateBy,reactivoLastUpdate,reactivoLastUpdateBy,reactivoDateCreate, reactivoMinStock);
        mostrarSweetAlert(reactivo);
    });
});

// Función para obtener la información del reactivo basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionReactivo(reactivo, name, code, cas, trademark, reference, quantity, unit, wlocation,lab,edate,almacenamiento_interno,clase_almacenamiento,state,create_by,last_update,update_by,date_create, minstock) {

    const inventario = {
        id: reactivo,
        name: name,
        code: code,
        cas: cas,
        almacenamiento_interno: almacenamiento_interno,
        clase_almacenamiento: clase_almacenamiento,
        trademark: trademark,
        reference: reference,
        weight: quantity,
        unit: unit,
        edate: edate,
        wlocation: wlocation,
        lab: lab,
        state: state,
        create_by: create_by,
        last_update: last_update,
        update_by: update_by,
        date_create: date_create,
        minstock:minstock,
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
                        <li><strong>Almacenamiento Interno:</strong> ${inventario.almacenamiento_interno}</li>
                        <li><strong>Clase de almacenamiento:</strong> ${inventario.clase_almacenamiento}</li>
                        <li><strong>Marca:</strong> ${inventario.trademark}</li>
                        <li><strong>Referencia:</strong> ${inventario.reference}</li>
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Cantidad en almacén:</strong> ${inventario.weight} ${inventario.unit}</li>
                        <li><strong>Inventario mínimo:</strong> ${inventario.minstock} ${inventario.unit}</li>
                        <li><strong>Fecha de vencimiento:</strong> ${inventario.edate}</li>
                        <li><strong>Ubicación en almacén:</strong> ${inventario.wlocation}</li>
                        <li><strong>Laboratorio:</strong> ${inventario.lab}</li>
                    </ul>
                    <br>
                    <h5>Detalle del registro:</h5>
                    <ul class="list-unstyled">
                    <li><strong>Fecha de registro:</strong> ${inventario.date_create}</li>
                    <li><strong>Responsable del registro:</strong> ${inventario.create_by}</li>
                    <li><strong>Última modificación:</strong> ${inventario.last_update}</li>
                    <li><strong>Última actualización por:</strong> ${inventario.update_by}</li>
                    </ul>
                    <br>
                    <h5>Información Adicional fichas de seguridad:</h5>
                    <ul class="list-unstyled">
                    <li><strong>Merck Millipore:</strong> <a  href="https://www.merckmillipore.com/CO/es" target="_blank">Click aquí</a></li>
                    <li><strong>Carl Roth:</strong> <a  href="https://www.carlroth.com/com/en/" target="_blank">Click aquí</a></li>
                    <li><strong>Echa:</strong> <a  href="https://echa.europa.eu/es/home" target="_blank">Click aquí</a></li>
                    <li><strong>PubChem:</strong> <a  href="https://pubchem.ncbi.nlm.nih.gov/" target="_blank">Click aquí</a></li>
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Cerrar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
