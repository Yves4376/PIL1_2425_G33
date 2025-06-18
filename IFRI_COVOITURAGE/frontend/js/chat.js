// chat.js
document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    const chatBox = document.getElementById('chatBox');
    const chatInput = document.getElementById('chatInput');
    const chatSend = document.getElementById('chatSend');

    chatSend.addEventListener('click', async () => {
        const message = chatInput.value.trim();
        if (!message) return;

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token
                },
                body: JSON.stringify({ message })
            });

            const data = await response.json();

            if (response.ok) {
                const newMsg = document.createElement('p');
                newMsg.textContent = 'Moi: ' + message;
                chatBox.appendChild(newMsg);
                chatInput.value = '';
            } else {
                alert(data.message || 'Erreur');
            }
        } catch (error) {
            console.error('Erreur d\'envoi de message', error);
        }
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





