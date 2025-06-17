
    const token = localStorage.getItem("token");
    fetch("http://localhost:5000/api/profile", {
      headers: { Authorization: "Bearer " + token }
    }).then(r => r.json()).then(data => {
      document.getElementById("nom").value = data.nom;
      document.getElementById("prenom").value = data.prenom;
      document.getElementById("photo_url").value = data.photo_url;
      document.getElementById("marque_vehicule").value = data.marque_vehicule;
      document.getElementById("modele_vehicule").value = data.modele_vehicule;
      document.getElementById("nombre_places").value = data.nombre_places;
    });

    document.getElementById("profileForm").addEventListener("submit", async e => {
      e.preventDefault();
      const res = await fetch("http://localhost:5000/api/profile", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token
        },
        body: JSON.stringify({
          nom: nom.value,
          prenom: prenom.value,
          photo_url: photo_url.value,
          marque_vehicule: marque_vehicule.value,
          modele_vehicule: modele_vehicule.value,
          nombre_places: nombre_places.value
        })
      });
      const d = await res.json();
      document.getElementById("message").textContent = d.message || "Profil mis à jour";
    });
  