// main.js - Add any JavaScript needed for frontend interactivity
// Example: Sortable table


document.addEventListener('DOMContentLoaded', () => {
    const table = document.querySelector('.data');
    if (table) {
        const headers = table.querySelectorAll('th');
        headers.forEach((header, index) => {
            header.addEventListener('click', () => {
                sortTable(table, index);
            });
        });
    }
 });
 
 
 function sortTable(table, columnIndex) {
    const rows = Array.from(table.querySelectorAll('tr:nth-child(n+2)'));
    const isAscending = table.querySelectorAll('th')[columnIndex].classList.contains('ascending');
     rows.sort((rowA, rowB) => {
        const cellA = rowA.cells[columnIndex].innerText.trim();
        const cellB = rowB.cells[columnIndex].innerText.trim();
     
        if (isNaN(cellA) || isNaN(cellB)) {
            return cellA.localeCompare(cellB);
        }
     
        return parseFloat(cellA) - parseFloat(cellB);
    });
     if (isAscending) {
        rows.reverse();
    }
 
 
    table.querySelector('tbody').append(...rows);
    table.querySelectorAll('th').forEach((th) => th.classList.remove('ascending'));
    table.querySelectorAll('th')[columnIndex].classList.add(isAscending ? 'descending' : 'ascending');
 }
 
 
 
 
 
 