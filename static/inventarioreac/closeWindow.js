function closeTab() {
    
    let countdown = 3;

    // Abre una SweetAlert con un div personalizado para mostrar el contador.
    Swal.fire({
        title: 'Redirigiendo...',
        html: '<div id="countdown">' + countdown + '</div>',
        showConfirmButton: false,
    });

    // Actualiza el contador en el div personalizado cada segundo.
    const countdownInterval = setInterval(function () {
        countdown--;
        const countdownElement = document.getElementById('countdown');
        if (countdownElement) {
            countdownElement.innerText = countdown;
        }

        if (countdown <= 0) {
            clearInterval(countdownInterval);
            Swal.close(); // Cierra la SweetAlert.
            
                window.location.href = '/UniCLab/';
            
        }
    }, 1000); // 1000 ms = 1 segundo
}