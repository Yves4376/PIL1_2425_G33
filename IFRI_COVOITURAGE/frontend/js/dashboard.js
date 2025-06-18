document.addEventListener('DOMContentLoaded', async () => {
    const token = localStorage.getItem('token');
    const headers = { 'Authorization': 'Bearer ' + token };

    async function fetchData(endpoint, elementId) {
        try {
            const response = await fetch(endpoint, { headers });
            const data = await response.json();
            const listElement = document.getElementById(elementId);
            if (response.ok && Array.isArray(data)) {
                listElement.innerHTML = data.length > 0 ?
                    data.map(item => `<li>${item.date} - ${item.depart}  ${item.destination}</li>`).join('') :
                    '<li>Aucun résultat</li>';
            } else {
                listElement.innerHTML = `<li class="error-message">${data.message || "Erreur"}</li>`;
            }
        } catch (error) {
            document.getElementById(elementId).innerHTML = '<li class="error-message">Erreur réseau</li>';
        }
    }

    fetchData('/api/mes-trajets', 'mesTrajets');
    fetchData('/api/mes-reservations', 'mesReservations');

    document.getElementById('logoutBtn').addEventListener('click', () => {
        localStorage.removeItem('token');
        window.location.href = 'login.html';
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


  fetch("http://localhost:5000/api/register", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));