function filterTable() {
    let input = document.getElementById("assetSearch").value.toUpperCase();
    let table = document.querySelector("table");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName("td");
        let match = false;
        for (let j = 0; j < cells.length; j++) {
            if (cells[j].innerText.toUpperCase().includes(input)) {
                match = true;
                break;
            }
        }
        rows[i].style.display = match ? "" : "none";
    }
}

function confirmSubmit() {
    return confirm("Are you sure you want to submit this?");
}
