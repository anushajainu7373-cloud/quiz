
let time = 60;

const timer = setInterval(function () {

    time--;

    document.getElementById("time").textContent = time;

    if (time <= 0) {

        clearInterval(timer);

        alert("Time is up!");

        document.getElementById("quizForm").submit();
    }

}, 1000);

