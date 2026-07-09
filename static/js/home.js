console.log("Home Page Loaded");

/* ==========================================
Counter Animation
========================================== */

const counters = document.querySelectorAll(".counter");

const speed = 100;

counters.forEach(counter => {

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const count = +counter.innerText;

        const increment = target / speed;

        if(count < target){

            counter.innerText = Math.ceil(count + increment);

            setTimeout(updateCounter,20);

        }

        else{

            counter.innerText = target;

        }

    };

    updateCounter();

});

/* ==========================================
Performance Preview
========================================== */

document.getElementById("rmse-value").innerHTML = "--";

document.getElementById("mae-value").innerHTML = "--";

document.getElementById("r2-value").innerHTML = "--";