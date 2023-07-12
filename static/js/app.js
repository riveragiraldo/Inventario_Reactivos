

const contactForm = document.getElementById('contactForm');
const registro = document.getElementById('registro');
const exito = document.getElementById('exito');


contactForm.addEventListener('submit', async(e)=>{

    e.preventDefault();
    

    try{
        const respuesta = await fetch('https://sheet.best/api/sheets/4b0e3de5-b959-4292-9f99-962537bd36cf',{
        method:'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({
            "Fecha": contactForm.fecha.value,
            "Nombre": contactForm.nombre.value,
            "Email": contactForm.email.value,
            "Telefono": contactForm.telefono.value,
            "Asunto": contactForm.asunto.value,
            "Mensaje": contactForm.mensaje.value,
            "AceptaPol": contactForm.tratamiento.value,
            
        })
    });
    const contenido = await respuesta.json();
    console.log(contenido);

    } 
    catch(error){
console.log(error);
    }
    

    
    registro.classList.remove('activo');
    exito.classList.add('activo');


});


