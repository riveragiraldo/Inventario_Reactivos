document.addEventListener('DOMContentLoaded', function () {
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');
    const startDateValidation = document.getElementById('start-date-validation');
    const endDateValidation = document.getElementById('end-date-validation');

    // Oculta los mensajes de validación al cargar la página
    startDateValidation.style.display = 'none';
    endDateValidation.style.display = 'none';

    startDateInput.addEventListener('input', function () {
        const selectedStartDate = new Date(startDateInput.value);
        const today = new Date();
        if (selectedStartDate > today) {
            startDateValidation.style.display = 'block';
        } else {
            startDateValidation.style.display = 'none';
        }
    });

    endDateInput.addEventListener('input', function () {
        const selectedEndDate = new Date(endDateInput.value);
        const today = new Date();
        if (selectedEndDate > today) {
            endDateValidation.style.display = 'block';
        } else {
            endDateValidation.style.display = 'none';
        }
    });
});