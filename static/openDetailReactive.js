// Agregar un controlador de eventos a las imágenes de detalle del reactivo
const detalleReactivoImages = document.getElementsByClassName('detalle-reactivo');
for (const image of detalleReactivoImages) {
    image.addEventListener('click', function () {
        const reactivoId = this.getAttribute('data-reactivo-id');
        const url = `/reactivos/${reactivoId}`;
        window.open(url, '_blank', 'width=600,height=700');
    });
}