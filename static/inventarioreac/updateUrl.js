// Obtener la URL actual
const currentUrl = window.location.href;

// Verificar si la URL no tiene parámetros de búsqueda
if (currentUrl.endsWith('/reactivos/inventario/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?lab='+labDefault+'&name=&trademark=';

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}

// Verificar si la URL no tiene parámetros de búsqueda
if (currentUrl.endsWith('/reactivos/listado_entradas/')) {
    // Modificar la URL agregando los parámetros de búsqueda deseados
    const newUrl = currentUrl + '?lab='+labDefault+'&name=&location=&destination=&location=&created_by=&start_date='+oneMonthAgo+'&end_date='+today;

    // Redirigir a la nueva URL
    window.location.href = newUrl;
}