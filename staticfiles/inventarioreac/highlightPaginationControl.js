// Obtener todos los enlaces
const perPageNumberLinks = document.querySelectorAll('.btn-group-toggle a');

// Agregar el evento click a cada enlace
perPageNumberLinks.forEach(link => {
    link.addEventListener('click', function (event) {
        // Remover la clase 'active' de todos los enlaces
        perPageLinks.forEach(link => {
            link.classList.remove('active');
        });

        // Agregar la clase 'active' al enlace clicado
        this.classList.add('active');

        // Obtener el ID del enlace activo
        const activeLinkId = this.getAttribute('id');

        // Guardar el ID del enlace activo en localStorage
        localStorage.setItem('activeLinkId', activeLinkId);
    });
});

// Verificar si hay un enlace activo guardado en localStorage al cargar la página
const activeLinkId = localStorage.getItem('activeLinkId');
if (activeLinkId) {
    // Aplicar la clase 'active' al enlace guardado
    const activeLink = document.getElementById(activeLinkId);
    if (activeLink) {
        activeLink.classList.add('active');
    }
}