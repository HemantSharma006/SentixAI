
const textArea = document.getElementById("text");
const charCount = document.getElementById("char-count");
const exampleButtons = document.querySelectorAll("[data-text]");
const form = document.getElementById("sentiment-form");
const analyzeButton = document.querySelector(".analyze-button");

function updateCharacterCount() {
    if (!textArea || !charCount) return;

    charCount.textContent = `${textArea.value.length} / 500 characters`;
}

if (textArea) {
    textArea.addEventListener("input", updateCharacterCount);
    updateCharacterCount();
}

exampleButtons.forEach((button) => {
    button.addEventListener("click", () => {
        textArea.value = button.dataset.text || "";
        updateCharacterCount();
        textArea.focus();
        textArea.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
    });
});

if (form && analyzeButton) {
    form.addEventListener("submit", () => {
        if (!textArea.value.trim()) {
            textArea.focus();
            return;
        }

        analyzeButton.disabled = true;
        analyzeButton.innerHTML = "<span>✦</span> Analyzing sentiment...";

        // Re-enable if browser validation prevents submission.
        window.setTimeout(() => {
            analyzeButton.disabled = false;
            analyzeButton.innerHTML =
                '<span>✦</span> Analyze Sentiment <span class="button-arrow">→</span>';
        }, 10000);
    });
}
