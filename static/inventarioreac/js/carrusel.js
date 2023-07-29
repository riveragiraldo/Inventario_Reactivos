/**
     * Array con las ubicaciones de las imagenes
     */
var imagenes=new Array(
    ['images/fondos/fondo.jpg'],
    ['images/fondos/fondo1.jpg']

);
var contador=0;

/**
 * Funcion para cambiar la imagen
 */
function rotarImagenes()
{
    // cambiamos la imagen
    contador++
    document.getElementById("imagen").src=imagenes[contador%imagenes.length][0];
}

/**
 * Función que se ejecuta una vez cargada la página
 */
onload=function()
{
    // Cargamos una imagen aleatoria
    rotarImagenes();

    // Indicamos que cada 3 minutos cambie la imagen
    setInterval(rotarImagenes,180000);
}