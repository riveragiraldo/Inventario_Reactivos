// Obtener el checkbox "Acepta Política"
var aplicaCAS = document.getElementById("aplicaCAS");
aplicaCAS.addEventListener("change", function () {

  if (this.checked) {
    aplicaCAS.value = 'Aplica';
  } else {
    aplicaCAS.value = 'No Aplica';
  }
});



// // Función para manejar cambios en el checkbox
// function handleCheckboxChange() {
//     var checkbox = document.getElementById("aplicaCAS");
//     var casInput = document.getElementById("cas");
//     console.log('Hola Mundo')

//     if (checkbox.checked) {
//         // Si el checkbox está marcado, establece el valor y desactiva el campo CAS
//         console.log('Aplica Cas')
//         checkbox.value = "Aplica";
//         casInput.value = "";
//     } else {
//         // Si el checkbox no está marcado, establece el valor y habilita el campo CAS
//         console.log('Aplica Cas')
//         checkbox.value = "No aplica";
//         casInput.value = "NO APLICA";
//         casInput.readOnly = true;
//     }
// }

// // Agrega un event listener al checkbox para manejar cambios
// var checkbox = document.getElementById("aplicaCAS");
// checkbox.addEventListener("change", handleCheckboxChange);

// // Llama a la función para configurar el estado inicial
// handleCheckboxChange();