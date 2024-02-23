document.addEventListener("DOMContentLoaded", function () {
    const password1Input = document.getElementById("id_password");
    const passwordToggle1 = document.getElementById("toogle-pass");
    
    // Manejador devents mostrar password1
    passwordToggle1.addEventListener("click",function(){
      if (password1Input.type==="password"){
        password1Input.type = "text";
        this.innerHTML = '<i class="fas fa-eye-slash" title="Ocultar contraseña" style="cursor: pointer;"></i>';
      }else if(password1Input.type==="text"){
        password1Input.type = "password";
        this.innerHTML = '<i class="fas fa-eye" title="Ver contraseña" style="cursor: pointer;"></i>';
      }
    })

    
  });