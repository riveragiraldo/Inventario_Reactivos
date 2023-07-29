const contenedorQR = document.getElementById('contenedorQR');
const formulario = document.getElementById('link');

const QR = new QRCode (contenedorQR);
QR.makeCode(formulario.value);



const contenedorQR_2 = document.getElementById('contenedorQR_2');
const formulario_2 = document.getElementById('link_2');

const QR_2 = new QRCode (contenedorQR_2);
QR_2.makeCode(formulario_2.value);






