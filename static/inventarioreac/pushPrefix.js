
const prefixInput = document.querySelector('input[name="prefix"]');
const input = document.querySelector("#phone");

//Llama la api con el listado de banderas y prefijos
const iti = window.intlTelInput(input, {
    preferredCountries: ["co"],
    separateDialCode: true,
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js"
});

// Evento change para actualizar el valor de la input prefix
input.addEventListener("change", function () {
    const selectedCountryData = iti.getSelectedCountryData();
    Prefijo = selectedCountryData.dialCode;
    Prefijo = "+" + Prefijo
    prefixInput.value = Prefijo;
});