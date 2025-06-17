// auth.js
async function login(email, password) {
    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok && data.token) {
            localStorage.setItem('token', data.token);
            window.location.href = 'dashboard.html';
        } else {
            alert(data.message || 'Erreur de connexion');
        }
    } catch (error) {
        console.error('Erreur réseau', error);
    }
}

async function register(userData) {
    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData)
        });

        const data = await response.json();

        if (response.ok) {
            alert('Inscription réussie');
            window.location.href = 'login.html';
        } else {
            alert(data.message || 'Erreur d\'inscription');
        }
    } catch (error) {
        console.error('Erreur réseau', error);
    }
}
