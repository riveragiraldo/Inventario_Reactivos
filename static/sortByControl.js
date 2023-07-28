// Variable global para almacenar el estado de ordenamiento
let currentSortState = "asc";
let currentSortedColumnIndex = -1;

// Función para realizar el ordenamiento
function sortTable(columnIndex) {
  const tableBody = document.querySelector("#tabla-inventario tbody");
  const rows = Array.from(tableBody.querySelectorAll("tr"));

  // Obtener el nombre de la columna a ordenar
  const columnName = tableBody.rows[0].cells[columnIndex].textContent;

  // Ordenar las filas
  rows.sort((a, b) => {
    const aValue = a.cells[columnIndex].textContent;
    const bValue = b.cells[columnIndex].textContent;

    if (currentSortState === "asc") {
      return aValue.localeCompare(bValue);
    } else {
      return bValue.localeCompare(aValue);
    }
  });

  // Cambiar el estado de ordenamiento
  if (currentSortState === "asc") {
    currentSortState = "desc";
  } else {
    currentSortState = "asc";
  }

  // Limpiar el cuerpo de la tabla
  tableBody.innerHTML = "";

  // Agregar las filas ordenadas al cuerpo de la tabla
  rows.forEach(row => tableBody.appendChild(row));

  // Eliminar la clase de ordenamiento de la columna anteriormente ordenada
  if (currentSortedColumnIndex !== -1) {
    const previousSortedHeader = document.querySelector(
      `.sortable-header[data-column="${currentSortedColumnIndex}"]`
    );
    previousSortedHeader.classList.remove("sorted-asc", "sorted-desc");
  }

  // Agregar la clase de ordenamiento a la columna actualmente ordenada
  const currentSortedHeader = document.querySelector(
    `.sortable-header[data-column="${columnIndex}"]`
  );
  currentSortedHeader.classList.add(
    currentSortState === "asc" ? "sorted-desc" : "sorted-asc"
  );

  // Actualizar el índice de la columna actualmente ordenada
  currentSortedColumnIndex = columnIndex;
}

// Obtener todos los encabezados de tabla con la clase .sortable-header
const sortableHeaders = document.querySelectorAll(".sortable-header");

// Agregar controlador de eventos click a los encabezados
sortableHeaders.forEach((header) => {
  header.addEventListener("click", () => {
    // Obtener el índice de columna desde el atributo data-column
    const columnIndex = parseInt(header.getAttribute("data-column"));
    sortTable(columnIndex);
  });
});
