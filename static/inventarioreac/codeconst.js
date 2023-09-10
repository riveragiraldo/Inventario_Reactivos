// Concatena los campos color - number  - subnumber
// Toma los valores de los campos color, number y subnumber, el campo de number lo vuelve un string de 3 cifras, los concatena
// y los escribe en el campo code

document.getElementById("color").addEventListener("input", updateCode);
document.getElementById("number").addEventListener("input", updateCode);
document.getElementById("subnumber").addEventListener("input", updateCode);

function updateCode() {
    var color = document.getElementById("color").value;
    var number = document.getElementById("number").value.padStart(3, '0'); //El campo code lo convierte en un str de 3 cifras
    var subnumber = document.getElementById("subnumber").value;
    var code;

    //Si subnumber existe concatena code con subnumber si no existe omite el guión y no lo concatena
    if (subnumber) {
        code = color + "-" + number + "-" + subnumber;
    } else {
        code = color + "-" + number;
    }
    
    document.getElementById("code").value = code;
}

  


