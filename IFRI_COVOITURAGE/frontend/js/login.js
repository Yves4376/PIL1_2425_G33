document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    try {
      const response = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });
  
      const data = await response.json();
  
      if (response.ok) {
        alert("Connexion réussie !");
        localStorage.setItem("token", data.token);  // si JWT
        window.location.href = "/dashboard.html";
      } else {
        alert(data.message || "Erreur de connexion");
      }
    } catch (err) {
      console.error(err);
      alert("Erreur réseau");
    }
  });
  