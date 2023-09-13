
var cuerpo = document.getElementById("cuerpo");

var imagenes=new Array(
    ['/images/fondos/fondo.jpg'],
    ['/images/fondos/fondo1.jpg'],
    ['/images/fondos/fondo2.jpg']
);
var uImage=imagenes[0];


var contador=0;
function rotarImagenes()
{
    
    contador++
    uImage=imagenes[contador%imagenes.length][0];
    cuerpo.style.backgroundImage = 'url('+uImage+')';
}




onload=function()
{
   
    rotarImagenes();

   
    setInterval(rotarImagenes,180000);
}

 

