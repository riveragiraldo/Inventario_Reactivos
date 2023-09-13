// Obtener el checkbox "Acepta Política"
var acceptDataProcessing = document.getElementById("acceptDataProcessing");
acceptDataProcessing.addEventListener("change", function () {

  if (this.checked) {
    acceptDataProcessing.value = 'Acepta';
  } else {
    acceptDataProcessing.value = '';
  }
});