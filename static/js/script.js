/* ======================================================
   House Price Prediction System
   Global JavaScript
====================================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("House Price Prediction System Loaded Successfully");

    /* ==========================================
       Active Navbar Link
    ========================================== */

    const currentPath = window.location.pathname;

    const navLinks = document.querySelectorAll(".navbar .nav-link");

    navLinks.forEach(link => {

        if (link.getAttribute("href") === currentPath) {

            link.classList.add("active");

        }

    });

});


/* ==========================================
   Smooth Scroll
========================================== */

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        document.querySelector(this.getAttribute("href"))
            .scrollIntoView({

                behavior: "smooth"

            });

    });

});


/* ==========================================
   Scroll To Top
========================================== */

function scrollToTop() {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

}


/* ==========================================
   Loading Button
========================================== */

function showLoading(button) {

    button.disabled = true;

    button.innerHTML = `
        <span class="spinner-border spinner-border-sm"></span>
        Loading...
    `;

}


/* ==========================================
   Reset Button
========================================== */

function resetButton(button, text) {

    button.disabled = false;

    button.innerHTML = text;

}


/* ==========================================
   Number Formatter
========================================== */

function formatCurrency(number) {

    return new Intl.NumberFormat("en-IN", {

        style: "currency",

        currency: "INR",

        maximumFractionDigits: 0

    }).format(number);

}


/* ==========================================
   Card Hover Animation
========================================== */

const cards = document.querySelectorAll(".card");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-8px)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px)";

    });

});


/* ==========================================
   Fade In Animation
========================================== */

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("show");

        }

    });

});

document.querySelectorAll(".fade-in").forEach((element) => {

    observer.observe(element);

});