let timerEl = document.getElementById("timer");
let quoteDisplayEl = document.getElementById("quoteDisplay");
let quoteInputEl = document.getElementById("quoteInput");
let resultEl = document.getElementById("result");
let submitBtnEl = document.getElementById("submitBtn");
let resetBtnEl = document.getElementById("resetBtn");
let spinnerEl = document.getElementById("spinner");

let counter = 0;
let timerId = null;

function startTimer() {
    counter = 0;
    timerEl.textContent = counter;
    timerId = setInterval(function() {
        counter += 1;
        timerEl.textContent = counter;
    }, 1000);
}

function getNewQuote() {
    spinnerEl.classList.remove("d-none");
    quoteDisplayEl.textContent = "";
    
    let options = { method: "GET" };
    fetch("https://apis.ccbp.in/random-quote", options)
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonData) {
            spinnerEl.classList.add("d-none");
            quoteDisplayEl.textContent = jsonData.content;
            startTimer();
        });
}

getNewQuote();

submitBtnEl.addEventListener("click", function() {
    if (quoteInputEl.value === quoteDisplayEl.textContent) {
        clearInterval(timerId);
        resultEl.textContent = "You typed it in " + counter + " seconds";
    } else {
        resultEl.textContent = "You typed incorrect sentence";
    }
});

resetBtnEl.addEventListener("click", function() {
    clearInterval(timerId);
    quoteInputEl.value = "";
    resultEl.textContent = "";
    getNewQuote();
});