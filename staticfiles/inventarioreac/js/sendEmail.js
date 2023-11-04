

const contactForm = document.getElementById('contactForm')


async function  (event){
    event.preventDefault()
    const fd = new FormData(this)

    const response = await fetch('https://formspree.io/f/mpzelald',{
        method='POST',
        body= fd,
        headers:{
            Accept:'application/json'
        }
    })

    if (response.ok){
        this.reset()
        alert('Mensaje enviado')
    }
    else{
        alert('Error al enviar')
    }
}


contactForm.addEventListener('submit',handleSendEmail)