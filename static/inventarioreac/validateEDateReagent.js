document.addEventListener('DOMContentLoaded', function () {
    // Obtén todas las celdas de la columna de vencimiento
    const cells = document.querySelectorAll("#tabla-inventario tbody td:nth-child(11)");

    // Recorre las celdas y comprueba si el reactivo está vencido
    cells.forEach((cell) => {
        const dateString = cell.textContent.trim();
        const dateParts = dateString.split('/');
        const reactivoDate = new Date(dateParts[2], dateParts[1] - 1, dateParts[0]); // Formato DD/MM/YYYY

        // Comprueba si la fecha del reactivo es menor o igual que la fecha actual
        if (reactivoDate <= new Date()) {
            cell.classList.add("reactivo-vencido"); // Agrega una clase CSS para resaltarla
            const reactivoName = cell.getAttribute("data-reactivo-name");
            const reactivoEdate = cell.getAttribute("data-reactivo-edate");
            cell.title = `El reactivo ${reactivoName} necesita su atención, ya que expiró su fecha de vencimiento: ${reactivoEdate}`;
        }
    });
});