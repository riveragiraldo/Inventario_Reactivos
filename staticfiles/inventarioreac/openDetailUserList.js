// Evento click para mostrar SweetAlert con la información del usuario
document.querySelectorAll('.detalle-reactivo').forEach(element => {
    element.addEventListener('click', function () {
        const usuarioId = this.getAttribute('data-usuario-id');        
        const usuarioName = this.getAttribute('data-usuario-name');
        const usuarioDate = this.getAttribute('data-usuario-date');
        const usuarioUserName = this.getAttribute('data-usuario-username');
        const usuarioEmail = this.getAttribute('data-usuario-email');
        const usuarioCc = this.getAttribute('data-usuario-cc');
        const usuarioPhone = this.getAttribute('data-usuario-phone');
        const usuarioLab = this.getAttribute('data-usuario-lab');
        const usuarioRol = this.getAttribute('data-usuario-rol');
        const usuarioTdp = this.getAttribute('data-usuario-tdp'); 
        const usuarioisActive = this.getAttribute('data-usuario-is_active');
        const usuarioLastLogin = this.getAttribute('data-usuario-last_login');
        const usuarioDateCreate = this.getAttribute('data-usuario-date_create');
        const usuarioUserCreate = this.getAttribute('data-usuario-user_create');
        const usuarioLastUpdate = this.getAttribute('data-usuario-last_update');
        const usuarioLastUpdateBy = this.getAttribute('data-usuario-update_by');
        const usuario = obtenerInformacionUsuario(usuarioId, usuarioName, usuarioDate, usuarioUserName, usuarioEmail, usuarioCc, usuarioPhone, usuarioLab,usuarioRol,usuarioTdp,usuarioisActive,usuarioLastLogin,usuarioDateCreate,usuarioUserCreate,usuarioLastUpdate,usuarioLastUpdateBy);
        mostrarSweetAlert(usuario);
    });
});

// Función para obtener la información del usuario basado en su ID (puedes hacer la solicitud al servidor)
function obtenerInformacionUsuario(id, name, date, username, email, cc, phone, lab,rol,tdp,isactive,lastlogin,datecreate,usercreate,lastupdate,lastupdateby) {

    const usuario = {
        id: id,
        name: name,
        date: date,
        username: username,
        email: email,
        cc: cc,
        phone: phone,
        lab: lab,
        rol: rol,
        tdp: tdp,
        isactive:isactive,
        lastlogin:lastlogin,
        datecreate:datecreate,
        usercreate:usercreate,
        lastupdate:lastupdate,
        lastupdateby:lastupdateby,
        

    };
    return usuario;
}

// Función para mostrar la SweetAlert con la información del usuario
function mostrarSweetAlert(usuario) {
    Swal.fire({
        icon: 'info',
        title: `Detalle de usuario  ${usuario.name}`,
        html: `
            <div class="card" style="text-align: left;">
                <br>
                <div class="card-body">
                    <h5>Información principal:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Id de registro usuario:</strong> ${usuario.id}</li>
                        <li><strong>Nombre:</strong> ${usuario.name}</li>
                        <li><strong>Nombre de usuario:</strong> ${usuario.username}</li>
                        <li><strong>Identificación:</strong> ${usuario.cc}</li>
                        <li><strong>Correo Electrónico:</strong> ${usuario.email}</li>
                        <li><strong>Teléfono:</strong> ${usuario.phone}</li>
                        <li><strong>Laboratorio al que pertenece:</strong> ${usuario.lab}</li>
                        <li><strong>Rol:</strong> ${usuario.rol}</li>
                        <li><strong>Acepta tratamiento de datos personales:</strong> ${usuario.tdp}</li>
                    </ul>
                    <br>
                    <h5>Información adicional:</h5>
                    <ul class="list-unstyled">
                        <li><strong>Activo:</strong> ${usuario.isactive}</li>
                        <li><strong>Último Acceso:</strong> ${usuario.lastlogin}</li>
                        <li><strong>Fecha de registro:</strong> ${usuario.datecreate}</li>
                        <li><strong>Usuario que crea registro:</strong> ${usuario.usercreate}</li>
                        <li><strong>Última actualización:</strong> ${usuario.lastupdate}</li>
                        <li><strong>Última actualización por:</strong> ${usuario.lastupdateby}</li>
                        
                    </ul>
                </div>
            </div>
        `,
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
        customClass: 'custom-swal-class' // Clase CSS personalizada para dar estilo a la alerta
    });
}
