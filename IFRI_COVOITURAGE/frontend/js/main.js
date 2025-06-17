document.addEventListener("DOMContentLoaded",
function () {
    lottie.loadAnimation({
        container:
        document.getElementById("background-animation"),
        path:"../carpool.json" ,
        renderer: "svg",
        loop: true,
        autoplay:true,
    });
});
