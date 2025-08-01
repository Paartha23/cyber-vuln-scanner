document.addEventListener("DOMContentLoaded", function () {
  const scanBtn = document.getElementById("scan-btn");
  const urlInput = document.getElementById("url-input");
  const errorMessage = document.getElementById("error-message");

  scanBtn.addEventListener("click", function (event) {
    const url = urlInput.value.trim();
    const urlPattern = /^(https?:\/\/)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(\/\S*)?$/;

    if (!urlPattern.test(url)) {
      errorMessage.style.display = "block";
      event.preventDefault(); // stop form submission or redirect
    } else {
      errorMessage.style.display = "none";
    }
  });
});
