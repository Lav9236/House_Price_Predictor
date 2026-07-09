document.getElementById("resetBtn").addEventListener("click", function (e) {

    e.preventDefault();

    window.location.href = "/predict";

});

const form = document.getElementById("predictionForm");

const spinner = document.getElementById("loadingSpinner");

form.addEventListener("submit", function(){

    spinner.style.display = "block";

});