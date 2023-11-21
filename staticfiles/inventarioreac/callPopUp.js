//Funciones para llamar Ventanas emergentes en el formulario de creación de reactivo

//Llama PopUp Clasificación almacenamiento_interno
function openPopupWindowalmacenamiento_interno() {
    var w = 450; // ancho de la ventana emergente
    var h = 400; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/almacenamiento_interno/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Llama PopUp Clasificación almacenamiento_interno
function openPopupWindowclase_almacenamiento() {
    var w = 450; // ancho de la ventana emergente
    var h = 400; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/clase_almacenamiento/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}



//Llama PopUp Crear Unidades
function openPopupWindowUnit() {
    var w = 450; // ancho de la ventana emergente
    var h = 400; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/unidades/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Llama PopUp Crear Reactivo
function openPopupWindowReagent() {
    var w = 600; // ancho de la ventana emergente
    var h = 800; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/reactivos/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Llama PopUp Crear Marca
function openPopupWindowTrademark() {
    var w = 450; // ancho de la ventana emergente
    var h = 400; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/marcas/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Llama PopUp Crear Asignatura
function openPopupWindowLocation() {
    var w = 450; // ancho de la ventana emergente
    var h = 400; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/ubicaciones/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Llama PopUp Crear Responsables
function openPopupWindowManager() {
    var w = 450; // ancho de la ventana emergente
    var h = 450; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/responsables/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Llama PopUp Crear Ubicaciones en almacén
function openPopupWindowWlocation() {
    var w = 450; // ancho de la ventana emergente
    var h = 500; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/ubicaciones_almacen/crear", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}


//Llama PopUp Crear Roles
function openPopupWindowRol() {
    var w = 450; // ancho de la ventana emergente
    var h = 500; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/roles/crear/", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Llama PopUp Crear Roles
function openPopupWindowLab() {
    var w = 450; // ancho de la ventana emergente
    var h = 500; // altura de la ventana emergente
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    window.open("/laboratorios/crear/", "popup", "width=" + w + ",height=" + h + ",left=" + left + ",top=" + top);
}

//Lee que formulario es de acuerdo con entrada oculta "wf"
var wf = document.getElementById("wf").value;


if (wf == "crear") {

    //Leer Valores
    var addclase_almacenamientoBtn = document.getElementById("add_clase_almacenamiento_btn");
    var addalmacenamiento_internoBtn = document.getElementById("add_almacenamiento_interno_btn");
    var addUnitBtn = document.getElementById("add_unit_btn");

    // Escucha el clic en add y llamar función 
    addclase_almacenamientoBtn.addEventListener("click", openPopupWindowclase_almacenamiento);
    addalmacenamiento_internoBtn.addEventListener("click", openPopupWindowalmacenamiento_interno);
    addUnitBtn.addEventListener("click", openPopupWindowUnit);
}

else if (wf == "entrada") {
   

    //Leer Valores
    var addReagentBtn = document.getElementById("add_reagent_btn");
    var addTrademarkBtn = document.getElementById("add_trademark_btn");
    var addLocationBtn = document.getElementById("add_location_btn");
    var addManagerBtn = document.getElementById("add_manager_btn");
    var addWlocationBtn = document.getElementById("add_wlocation_btn");

    // Escucha el clic en add y llamar función 
    addReagentBtn.addEventListener("click", openPopupWindowReagent);
    addTrademarkBtn.addEventListener("click", openPopupWindowTrademark);
    addLocationBtn.addEventListener("click", openPopupWindowLocation);
    addManagerBtn.addEventListener("click", openPopupWindowManager);
    addWlocationBtn.addEventListener("click", openPopupWindowWlocation);
}



else if (wf == "salida") {
    
    //Leer Valores
    var addManagerBtn = document.getElementById("add_manager_btn");
    var addLocationBtn = document.getElementById("add_location_btn");

    // Escucha el clic en add y llamar función 
    addManagerBtn.addEventListener("click", openPopupWindowManager);
    addLocationBtn.addEventListener("click", openPopupWindowLocation);
}
else if (wf == "user_create") {
    
    //Leer Valores
    var addRolBtn = document.getElementById("add_rol_btn");
    var addLabBtn = document.getElementById("add_lab_btn");

    // Escucha el clic en add y llamar función 
    addRolBtn.addEventListener("click", openPopupWindowRol);
    addLabBtn.addEventListener("click", openPopupWindowLab);
}