// convierte número a string de tres cifras


document.getElementById("color").addEventListener("input", updateCode);
document.getElementById("number").addEventListener("input", updateCode);
document.getElementById("subnumber").addEventListener("input", updateCode);

function updateCode() {
    var color = document.getElementById("color").value;
    var number = document.getElementById("number").value.padStart(3, '0');
    var subnumber = document.getElementById("subnumber").value;
    var code;

    if (subnumber) {
        code = color + "-" + number + "-" + subnumber;
    } else {
        code = color + "-" + number;
    }

    document.getElementById("code").value = code;
}

  


