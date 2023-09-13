// Limpia campos del formulario de manera que evita que cuando se realice una transacacción y se de atrás, o carguen nuevamente 
//queden valores en los campos y así se genere un doble registro

window.addEventListener('pageshow', function(event) {
    var form = document.querySelector('form[name="form"]');
    form.reset();
  });
  


