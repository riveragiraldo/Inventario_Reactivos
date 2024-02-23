// Obtener la URL actual
const currentUrl = window.location.href;

// Verificar si la URL no tiene parámetros de búsqueda para inventario
if (currentUrl.endsWith('/reactivos/inventario/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?lab='+labDefault+'&name=&id_r=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda para entradas
if (currentUrl.endsWith('/reactivos/listado_entradas/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?lab='+labDefault+'&name=&id_r=&start_date=&end_date=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda para salidas
if (currentUrl.endsWith('/reactivos/listado_salidas/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?lab='+labDefault+'&name=&location=&destination=&location=&created_by=&start_date=&end_date=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda para reactivos
if (currentUrl.endsWith('/reactivos/listado_reactivos/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?name=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda para usuarios
if (currentUrl.endsWith('/usuarios/listar/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?lab='+labDefault+'&name=&id_user=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda para solicitudes
if (currentUrl.endsWith('/solicitudes/listado_solicitudes/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?start_date=&end_date=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda para solicitudes
if (currentUrl.endsWith('/administrar/listado_eventos/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?name=&id_user=&start_date=&end_date='+today;

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda para inventario
if (currentUrl.endsWith('/solicitudes/solicitudes_externas/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?lab='+labDefault+'&start_date=&end_date=&keyword=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}