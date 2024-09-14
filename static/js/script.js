// search table function
function searchTable() {
  // Get the search input value
  var input = document.getElementById("searchInput");
  var filter = input.value.toUpperCase();
  var table = document.getElementById("myTable");
  var tr = table.getElementsByTagName("tr");

  // Loop through table rows and hide those that don't match the search query
  for (var i = 1; i < tr.length; i++) {
    var td = tr[i].getElementsByTagName("td");
    var match = false;

    // Loop through all table columns to check if any cell matches the search input
    for (var j = 0; j < td.length; j++) {
      if (td[j]) {
        if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
          match = true;
          break;
        }
      }
    }

    // Show or hide the row based on the match result
    tr[i].style.display = match ? "" : "none";
  }
}

// sort table function
function sortTable(columnIndex) {
  var table = document.getElementById("myTable");
  var rows = Array.from(table.rows).slice(1); // Exclude the header row
  var isAscending =
    table.rows[0].cells[columnIndex].getAttribute("data-order") === "asc";

  rows.sort(function (rowA, rowB) {
    var cellA = rowA.cells[columnIndex];
    var cellB = rowB.cells[columnIndex];

    // Ensure the cells exist before comparing
    if (!cellA || !cellB) {
      return 0;
    }

    var valueA = cellA.innerText || cellA.textContent;
    var valueB = cellB.innerText || cellB.textContent;

    // Convert to number if both values are numeric
    if (!isNaN(valueA) && !isNaN(valueB)) {
      valueA = parseFloat(valueA);
      valueB = parseFloat(valueB);
    }

    if (valueA < valueB) return isAscending ? -1 : 1;
    if (valueA > valueB) return isAscending ? 1 : -1;
    return 0;
  });

  rows.forEach((row) => table.tBodies[0].appendChild(row));

  // Toggle sort direction
  table.rows[0].cells[columnIndex].setAttribute(
    "data-order",
    isAscending ? "desc" : "asc"
  );
}
