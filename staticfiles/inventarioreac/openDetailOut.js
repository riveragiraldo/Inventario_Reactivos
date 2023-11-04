// Evento click para mostrar SweetAlert con la información del reactivo
document.querySelectorAll('.detalle-reactivo').forEach(element => {
    element.addEventListener('click', function () {
        const reactivoId = this.getAttribute('data-reactivo-id');        
        const reactivoName = this.getAttribute('data-reactivo-name');
        const reactivoDate = this.getAttribute('data-reactivo-date');
        const reactivoTrademark = this.getAttribute('data-reactivo-trademark');
        const reactivoReference = this.getAttribute('data-reactivo-reference');
        const reactivoQuantity = this.getAttribute('data-reactivo-quantity');
        const reactivoUnit = this.getAttribute('data-reactivo-unit');
        const reactivoLab = this.getAttribute('data-reactivo-lab');
        const reactivoDateCreate = this.getAttribute('data-reactivo-date_create');
        const reactivoDestination = this.getAttribute('data-reactivo-destination');
        const reactivoManager = this.getAttribute('data-reactivo-manager');
        const reactivoLocation = this.getAttribute('data-reactivo-location');
        const reactivoSchool = this.getAttribute('data-reactivo-school');
        const reactivoObservations = this.getAttribute('data-reactivo-observations');
        const reactivoCreateBy = this.getAttribute('data-reactivo-create_by');
        const reactivoLastUpdate = this.getAttribute('data-reactivo-lastupdate');
        const reactivoLastUpdateBy = this.getAttribute('data-reactivo-update_by');
        const reactivoIdInventario = this.getAttribute('data-reactivo-id_inventario');
        const reactivo = obtenerInformacionReactivo(reactivoId, reactivoName, reactivoDate, reactivoTrademark, reactivoReference, reactivoQuantity, reactivoUnit, reactivoLab,reactivoDateCreate,reactivoDestination,reactivoManager,reactivoLocation,reactivoSchool,reactivoObservations,reactivoCreateBy,reactivoLastUpdate,reactivoLastUpdateBy,reactivoIdInventario);
        mostrarSweetAlert(reactivo);
    });
});

// Función para obtener la información del reactivo basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionReactivo(reactivo, name, date, trademark, reference, quantity, unit, lab,date_create,destination,manager,location,school,observations,create_by,last_update,update_by,id_inventario) {

    const salida = {
        id: reactivo,
        name: name,
        date: date,
        trademark: trademark,
        reference: reference,
        weight: quantity,
        unit: unit,
        date_create: date_create,
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
    return salida;
}

// Función para mostrar la SweetAlert con la información del reactivo
function mostrarSweetAlert(salida) {
    Swal.fire({
        icon: 'info',
        title: `Registro de salida  ${salida.name}`,
        html: `
            <div class="card" style="text-align: left;">
                <div class="card-header">
                    Detalle de registro de salida del reactivo ${salida.name} el ${salida.date}
                </div>
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Id de registro salida:</strong> ${salida.id}</li>
                        <li><strong>Nombre:</strong> ${salida.name}</li>
                        <li><strong>Marca:</strong> ${salida.trademark}</li>
                        <li><strong>Referencia:</strong> ${salida.reference}</li>
                        <li><strong>Cantidad registrada:</strong> ${salida.weight} ${salida.unit}</li>
                        <li><strong>Laboratorio:</strong> ${salida.lab}</li>
                        <li><strong>Destino:</strong> ${salida.destination}</li>
                        <li><strong>Responsable:</strong> ${salida.manager}</li>
                        <li><strong>Asignatura/Ubicación:</strong> ${salida.location}</li>
                        <li><strong>Facultad:</strong> ${salida.school}</li>
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Observaciones:</strong> ${salida.observations}</li>
                        <li><strong>Consecutivo de Inventario:</strong> ${salida.id_inventario}</li>
                        <li><strong>Fecha de registro:</strong> ${salida.date_create}</li>
                        <li><strong>Responsable del registro:</strong> ${salida.create_by}</li>
                        <li><strong>Última modificación:</strong> ${salida.last_update}</li>
                        <li><strong>Última actualización por:</strong> ${salida.update_by}</li>
                        
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
