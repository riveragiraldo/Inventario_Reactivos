// Evento click para mostrar SweetAlert con la información del reactivo
document.querySelectorAll('.created_by_cell').forEach(element => {
    element.addEventListener('click', function () {
        const userCreateName = this.getAttribute('date_user_create');
        const reactiveCreateName = this.getAttribute('data-reactivo-name');
        const reactiveCreateDate = this.getAttribute('data-reactivo-date');
        const userCreateId = this.getAttribute('date_user_id');
        const userCreateUsername = this.getAttribute('date_user_username');
        const userCreateMail = this.getAttribute('date_user_mail');
        const userCreatePhone = this.getAttribute('date_user_phone');
        const userCreateLab = this.getAttribute('date_user_lab');
        const userCreateRol = this.getAttribute('date_user_rol');
        const userCreateDatejoined = this.getAttribute('date_user_datejoined');
        const userCreateLastlogin = this.getAttribute('date_user_lastlogin');
        const userCreateType = this.getAttribute('date_user_type');
        const userCreateVist = this.getAttribute('date_user_vist');

        
        const creador = obtenerInformacionCreador(userCreateName,reactiveCreateName,reactiveCreateDate,userCreateId,userCreateUsername,userCreateMail,userCreatePhone,userCreateLab,userCreateRol,userCreateDatejoined,userCreateLastlogin,userCreateType,userCreateVist);
        mostrarSweetAlertUserCreate(creador);
    });
});

// Función para obtener la información del reactivo basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionCreador(name,reactive,date_create,id,username,mail,phone,lab,rol,datejoined,lastlogin,type,vist) {

    const create = {
        name: name,
        reactive:reactive,
        date_create:date_create,
        id:id,
        username:username,
        mail:mail,
        phone:phone,
        lab:lab,
        rol:rol,
        datejoined:datejoined,
        lastlogin:lastlogin,
        type:type,
        vist:vist


    };
    return create;
}

// Función para mostrar la SweetAlert con la información del reactivo
function mostrarSweetAlertUserCreate(create) {
    Swal.fire({
        icon: 'info',
        title: `${create.name}`,
        html: `
            <div class="card" style="text-align: left;">
                <div class="card-header">
                    Detalle usuario que ${create.type} ${create.vist} ${create.reactive} el ${create.date_create}
                </div>
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Identificación :</strong> ${create.id}</li>
                        <li><strong>Nombre:</strong> ${create.name}</li>
                        <li><strong>Nombre de usuario:</strong> ${create.username}</li>
                        <li><strong>Correo Electrónico:</strong> ${create.mail}</li>
                        <li><strong>Teléfono:</strong> ${create.phone}</li>
                        <li><strong>Laboratorio al que pertenece</strong> ${create.lab}</li>
                        <li><strong>Rol de Usuario:</strong> ${create.rol}</li>
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Último Acceso:</strong>${create.lastlogin}</li>
                        <li><strong>Fecha de Alta:</strong> ${create.datejoined}</li>
                        
                        
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
