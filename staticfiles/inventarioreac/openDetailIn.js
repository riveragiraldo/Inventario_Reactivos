// Evento click para mostrar SweetAlert con la información del reactivo
document.querySelectorAll('.detalle-reactivo').forEach(element => {
    element.addEventListener('click', function () {
        const reactivoId = this.getAttribute('data-reactivo-id');        
        const reactivoName = this.getAttribute('data-reactivo-name');
        const reactivoDate = this.getAttribute('data-reactivo-date');
        const reactivoOrder = this.getAttribute('data-reactivo-order');
        const reactivoTrademark = this.getAttribute('data-reactivo-trademark');
        const reactivoReference = this.getAttribute('data-reactivo-reference');
        const reactivoQuantity = this.getAttribute('data-reactivo-quantity');
        const reactivoUnit = this.getAttribute('data-reactivo-unit');
        const reactivoDateOrder = this.getAttribute('data-reactivo-date_order');
        const reactivoLab = this.getAttribute('data-reactivo-lab');
        const reactivoDateCreate = this.getAttribute('data-reactivo-date_create');
        const reactivoNProject = this.getAttribute('data-reactivo-nproject');
        const reactivoPrice = this.getAttribute('data-reactivo-price');
        const reactivoDestination = this.getAttribute('data-reactivo-destination');
        const reactivoManager = this.getAttribute('data-reactivo-manager');
        const reactivoLocation = this.getAttribute('data-reactivo-location');
        const reactivoSchool = this.getAttribute('data-reactivo-school');
        const reactivoObservations = this.getAttribute('data-reactivo-observations');
        const reactivoCreateBy = this.getAttribute('data-reactivo-create_by');
        const reactivoLastUpdate = this.getAttribute('data-reactivo-lastupdate');
        const reactivoLastUpdateBy = this.getAttribute('data-reactivo-update_by');
        const reactivoIdInventario = this.getAttribute('data-reactivo-id_inventario');
        const reactivo = obtenerInformacionReactivo(reactivoId, reactivoName, reactivoDate, reactivoOrder, reactivoTrademark, reactivoReference, reactivoQuantity, reactivoUnit, reactivoDateOrder, reactivoLab,reactivoDateCreate,reactivoNProject,reactivoPrice,reactivoDestination,reactivoManager,reactivoLocation,reactivoSchool,reactivoObservations,reactivoCreateBy,reactivoLastUpdate,reactivoLastUpdateBy,reactivoIdInventario);
        mostrarSweetAlert(reactivo);
    });
});

// Función para obtener la información del reactivo basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionReactivo(reactivo, name, date, order, trademark, reference, quantity, unit, date_order,lab,date_create,nproject,price,destination,manager,location,school,observations,create_by,last_update,update_by,id_inventario) {

    const entrada = {
        id: reactivo,
        name: name,
        date: date,
        order: order,
        nproject: nproject,
        price: price,
        trademark: trademark,
        reference: reference,
        weight: quantity,
        unit: unit,
        date_create: date_create,
        date_order: date_order,
        lab: lab,
        destination: destination,
        manager: manager,
        location: location,
        school: school,
        observations: observations,
        create_by: create_by,
        last_update: last_update,
        update_by: update_by,
        id_inventario: id_inventario

    };
    return entrada;
}

// Función para mostrar la SweetAlert con la información del reactivo
function mostrarSweetAlert(entrada) {
    Swal.fire({
        icon: 'info',
        title: `Registro de entrada  ${entrada.name}`,
        html: `
            <div class="card" style="text-align: left;">
                <div class="card-header">
                    Detalle de registro de entrada del reactivo ${entrada.name} el ${entrada.date}
                </div>
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Id de registro entrada:</strong> ${entrada.id}</li>
                        <li><strong>Nombre:</strong> ${entrada.name}</li>
                        <li><strong>Marca:</strong> ${entrada.trademark}</li>
                        <li><strong>Referencia:</strong> ${entrada.reference}</li>
                        <li><strong>Cantidad registrada:</strong> ${entrada.weight} ${entrada.unit}</li>
                        <li><strong>Orden de entrada:</strong> ${entrada.order} de ${entrada.date_order}</li>
                        <li><strong>Número de proyecto:</strong> ${entrada.nproject}</li>
                        <li><strong>Laboratorio:</strong> ${entrada.lab}</li>
                        <li><strong>Valor de ingreso:</strong> ${entrada.price}</li>
                        <li><strong>Destino:</strong> ${entrada.destination}</li>
                        <li><strong>Responsable:</strong> ${entrada.manager}</li>
                        <li><strong>Asignatura/Ubicación:</strong> ${entrada.location}</li>
                        <li><strong>Facultad:</strong> ${entrada.school}</li>
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Observaciones:</strong> ${entrada.observations}</li>
                        <li><strong>Consecutivo de Inventario:</strong> ${entrada.id_inventario}</li>
                        <li><strong>Fecha de registro:</strong> ${entrada.date_create}</li>
                        <li><strong>Responsable del registro:</strong> ${entrada.create_by}</li>
                        <li><strong>Última modificación:</strong> ${entrada.last_update}</li>
                        <li><strong>Última actualización por:</strong> ${entrada.update_by}</li>
                        
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
