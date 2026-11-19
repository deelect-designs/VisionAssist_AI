// VisionAssist AI - Text-to-Speech Reader

document.addEventListener("DOMContentLoaded", function () {

    const textElement = document.getElementById("extracted-text");

    const speakButton = document.getElementById("speak-button");
    const pauseButton = document.getElementById("pause-button");
    const resumeButton = document.getElementById("resume-button");
    const stopButton = document.getElementById("stop-button");
    const statusElement = document.getElementById("speech-status");

    // Only run on pages containing the voice reader.
    if (
        !textElement ||
        !speakButton ||
        !pauseButton ||
        !resumeButton ||
        !stopButton ||
        !statusElement
    ) {
        return;
    }

    // Check whether the browser supports speech synthesis.
    if (!("speechSynthesis" in window)) {
        statusElement.textContent =
            "Sorry, your browser does not support voice reading.";

        speakButton.disabled = true;
        return;
    }

    const speechEngine = window.speechSynthesis;

    let currentUtterance = null;

    function resetControls() {
        speakButton.disabled = false;
        pauseButton.disabled = true;
        resumeButton.disabled = true;
        stopButton.disabled = true;
    }

    // Start reading the extracted document.
    speakButton.addEventListener("click", function () {

        const documentText = textElement.textContent.trim();

        if (!documentText) {
            statusElement.textContent =
                "There is no extracted text to read.";
            return;
        }

        // Stop any previous speech.
        speechEngine.cancel();

        currentUtterance = new SpeechSynthesisUtterance(
            documentText
        );

        // Set the intended language.
        currentUtterance.lang = "en-NG";

        // Normal speaking speed.
        currentUtterance.rate = 1;

        // Normal voice pitch.
        currentUtterance.pitch = 1;

        currentUtterance.onstart = function () {
            statusElement.textContent =
                "Reading your document aloud.";

            speakButton.disabled = true;
            pauseButton.disabled = false;
            resumeButton.disabled = true;
            stopButton.disabled = false;
        };

        currentUtterance.onend = function () {
            statusElement.textContent =
                "Document reading completed.";

            resetControls();
        };

        currentUtterance.onerror = function (event) {

            // Ignore cancellation errors caused by the Stop button.
            if (event.error === "canceled" ||
                event.error === "interrupted") {
                return;
            }

            statusElement.textContent =
                "An error occurred while reading the document.";

            resetControls();
        };

        speechEngine.speak(currentUtterance);

        statusElement.textContent =
            "Preparing to read your document.";
    });

    // Pause the reading.
    pauseButton.addEventListener("click", function () {

        if (speechEngine.speaking && !speechEngine.paused) {

            speechEngine.pause();

            pauseButton.disabled = true;
            resumeButton.disabled = false;

            statusElement.textContent =
                "Document reading paused.";
        }
    });

    // Continue reading from where it stopped.
    resumeButton.addEventListener("click", function () {

        if (speechEngine.paused) {

            speechEngine.resume();

            pauseButton.disabled = false;
            resumeButton.disabled = true;

            statusElement.textContent =
                "Document reading resumed.";
        }
    });

    // Stop the reading completely.
    stopButton.addEventListener("click", function () {

        speechEngine.cancel();

        currentUtterance = null;

        resetControls();

        statusElement.textContent =
            "Document reading stopped.";
    });

});