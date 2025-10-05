document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-btn");
    const shortText = document.getElementById("short-text");
    const fullText = document.getElementById("full-text");

    if (!btn || !shortText || !fullText) return;

    btn.addEventListener("click", function () {
        if (fullText.style.display === "none") {
            fullText.style.display = "block";
            shortText.style.display = "none";
            btn.innerText = "Show less";
        } else {
            fullText.style.display = "none";
            shortText.style.display = "block";
            btn.innerText = "Read more";
        }
    });
});
