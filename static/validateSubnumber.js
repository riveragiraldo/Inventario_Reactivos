document.addEventListener("DOMContentLoaded", function () {
    const subnumberInput = document.getElementById("subnumber");
    // Obtener el formulario por su ID
    const form = document.getElementById('createForm');

    function validateSubnumber() {
        const pattern = new RegExp(subnumberInput.getAttribute("pattern"));
        const title = subnumberInput.getAttribute("title");
        const value = subnumberInput.value
        if (value != "") {

            if (!pattern.test(subnumberInput.value)) {
                Swal.fire({
                    icon: "warning",
                    title: "Subnúmero no permitido",
                    text: title,
                    confirmButtonText: "Aceptar",
                    didClose: () => {
                        // Posicionar el foco en el campo subnumber para que el usuario pueda escribir
                        subnumberInput.focus();
                    },
                });
            }
        }
    }

    subnumberInput.addEventListener("blur", validateSubnumber);
});