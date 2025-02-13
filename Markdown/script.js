function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    let message = document.getElementById("message");

    if (fileInput.files.length === 0) {
        message.textContent = "Please select a Markdown file!";
        return;
    }

    let file = fileInput.files[0];
    let formData = new FormData();
    formData.append("file", file);

    fetch("/convert", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.html_file) {
                message.innerHTML = `Converted! <a href="/output/${data.html_file}" target="_blank">View HTML</a>`;
                loadHistory();
            } else {
                message.textContent = "Conversion failed!";
            }
        });
}

function loadHistory() {
    fetch("/history")
        .then(response => response.json())
        .then(data => {
            let historyList = document.getElementById("historyList");
            historyList.innerHTML = "";
            data.forEach(record => {
                historyList.innerHTML += `<li>${record[1]} → <a href="/output/${record[2]}" target="_blank">View</a></li>`;
            });
        });
}

document.addEventListener("DOMContentLoaded", loadHistory);
