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
        const selectedEndDate = new Date(endDateInput.value);

        const today = new Date();
        const formattedDate = today.toLocaleDateString('es-ES'); // Formatea la fecha en DD/MM/AAAA
        if (selectedStartDate > today) {
            startDateValidation.textContent = 'La fecha inicial debe ser anterior o igual a '+formattedDate;
            startDateValidation.style.display = 'block';
            startDateInput.setCustomValidity('La fecha inicial debe ser anterior o igual a '+formattedDate);
        } else {
            startDateValidation.style.display = 'none';
        }

        // Validar si start_date es mayor que end_date
        if (selectedStartDate > selectedEndDate) {
            startDateValidation.textContent = 'La fecha inicial no puede ser mayor que la fecha final.';
            startDateValidation.style.display = 'block';
            startDateInput.setCustomValidity('La fecha inicial no puede ser mayor que la fecha final.');
        } else {
            endDateInput.setCustomValidity('');
        }
    });

    endDateInput.addEventListener('input', function () {
        const selectedStartDate = new Date(startDateInput.value);
        const selectedEndDate = new Date(endDateInput.value);

        const today = new Date();
        const formattedDate = today.toLocaleDateString('es-ES'); // Formatea la fecha en DD/MM/AAAA
        if (selectedEndDate > today) {
            endDateValidation.textContent = 'La fecha final debe ser anterior o igual a '+formattedDate;
            endDateValidation.style.display = 'block';
            endDateInput.setCustomValidity('La fecha final debe ser anterior o igual a '+formattedDate);
        } else {
            endDateValidation.style.display = 'none';
        }

        // Validar si end_date es mayor que start_date
        if (selectedEndDate < selectedStartDate) {
            endDateValidation.textContent = 'La fecha final no puede ser menor que la fecha inicial.';
            endDateValidation.style.display = 'block';
            endDateInput.setCustomValidity('La fecha final no puede ser menor que la fecha inicial.');
        } else {
            endDateInput.setCustomValidity('');
        }
    });
});
