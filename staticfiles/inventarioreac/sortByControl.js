document.addEventListener("DOMContentLoaded", function () {
  // Variable global para almacenar el estado de ordenamiento por columna
  const columnSortStates = {};

  // Función para realizar el ordenamiento
  function sortTable(columnIndex) {
    const tableBody = document.querySelector("#tabla-inventario tbody");
    const rows = Array.from(tableBody.querySelectorAll("tr"));
    const tableHead = document.querySelector("#tabla-inventario thead");
    // Obtener el nombre de la columna a ordenar
    const columnName = tableHead.rows[0].cells[columnIndex].getAttribute("data-column-name");
    

    // Obtener el estado de ordenamiento actual de la columna
    let currentSortState = columnSortStates[columnName] || "asc";

    // Ordenar las filas
    rows.sort((a, b) => {
      const aValue = a.cells[columnIndex].textContent;
      const bValue = b.cells[columnIndex].textContent;


      if (columnName === "id" || columnName === "date") {

        if (columnName === "id") {
          // Tratamiento especial para ordenar numéricamente la columna "id"
          
          aNumericValue = parseInt(aValue);
          bNumericValue = parseInt(bValue);
        } else if (columnName === "date") {
          // Tratamiento especial para ordenar como feha la columna  "date"
          
          const aDateValue = convertDateToValidFormat(aValue);
          const bDateValue = convertDateToValidFormat(bValue);
          
          if (currentSortState === "asc") {
            return aDateValue.localeCompare(bDateValue);
          } else {
            return bDateValue.localeCompare(aDateValue);
          }
        }


        if (currentSortState === "asc") {
          return aNumericValue - bNumericValue;
        } else {
          return bNumericValue - aNumericValue;
        }
      } else {
        // Ordenamiento alfabético para otras columnas
        if (currentSortState === "asc") {
          return aValue.localeCompare(bValue);
        } else {
          return bValue.localeCompare(aValue);
        }
      }
    });

    // Cambiar el estado de ordenamiento
    if (currentSortState === "asc") {
      currentSortState = "desc";
    } else {
      currentSortState = "asc";
    }

    // Almacenar el nuevo estado de ordenamiento de la columna
    columnSortStates[columnName] = currentSortState;

    // Limpiar el cuerpo de la tabla
    tableBody.innerHTML = "";

    // Agregar las filas ordenadas al cuerpo de la tabla
    rows.forEach((row) => tableBody.appendChild(row));

    // Eliminar la clase de ordenamiento de todas las columnas
    const sortableHeaders = document.querySelectorAll(".sortable-header");
    sortableHeaders.forEach((header) => {
      header.classList.remove("sorted-asc", "sorted-desc");
    });

    // Agregar la clase de ordenamiento a la columna actualmente ordenada
    const currentSortedHeader = document.querySelector(
      `.sortable-header[data-column="${columnIndex}"]`
    );
    currentSortedHeader.classList.add(
      currentSortState === "asc" ? "sorted-desc" : "sorted-asc"
    );
  }


  // Obtener todos los encabezados de tabla con la clase .sortable-header
  const sortableHeaders = document.querySelectorAll(".sortable-header");

  // Agregar controlador de eventos click a los encabezados
  sortableHeaders.forEach((header, index) => {
    header.addEventListener("click", () => {
      // Obtener el índice de columna desde el atributo data-column
      sortTable(index);
    });
  });
});


function convertDateToValidFormat(dateString) {
  // Dividir la cadena de fecha en partes
  const parts = dateString.split('/'); // Supongo que el formato es "DD/MM/YYYY"

  // Verificar si hay tres partes (día, mes, año)
  if (parts.length === 3) {
    const day = parts[0];
    const month = parts[1];
    const year = parts[2];

    // Crear una fecha válida en formato "YYYY-MM-DD"
    const validDate = `${year}-${month}-${day}`;

    return validDate;
  } else {
    // Si el formato no es válido, devolver la cadena original
    return dateString;
  }
}

