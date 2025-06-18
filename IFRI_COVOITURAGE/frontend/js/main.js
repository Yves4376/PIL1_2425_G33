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


fetch('http://localhost:5000/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));