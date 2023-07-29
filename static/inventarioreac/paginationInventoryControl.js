// Obtener los enlaces de paginación
const perPageLinks = document.querySelectorAll('.btn-group-toggle a');

// Función para resaltar el enlace seleccionado
function resaltarEnlaceSeleccionado() {
    // Recorrer los enlaces y eliminar la clase 'active'
    perPageLinks.forEach(link => {
        link.classList.remove('active');
    });

    // Obtener el valor guardado del enlace seleccionado
    const perPageValue = localStorage.getItem('perPageValue');

    // Si hay un valor guardado, resaltar el enlace correspondiente
    if (perPageValue) {
        const selectedLink = document.getElementById(`per-page-${perPageValue}`);
        if (selectedLink) {
            selectedLink.classList.add('active');
        }
    }
}

// Función para manejar el clic en los enlaces de paginación
function handleClick(event) {
    const perPageValue = event.target.textContent;

    // Guardar el valor del enlace seleccionado en el almacenamiento local
    localStorage.setItem('perPageValue', perPageValue);

    // Resaltar el enlace seleccionado
    resaltarEnlaceSeleccionado();
}

// Agregar el evento 'click' a cada enlace de paginación
perPageLinks.forEach(link => {
    link.addEventListener('click', handleClick);
});

// Resaltar el enlace seleccionado al cargar la página
resaltarEnlaceSeleccionado();