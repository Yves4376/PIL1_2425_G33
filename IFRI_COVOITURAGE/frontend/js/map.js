// map.js
document.addEventListener('DOMContentLoaded', () => {
    const map = L.map('map').setView([6.3703, 2.3912], 12); // Ex: Cotonou

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    const points = [
        { lat: 6.3703, lng: 2.3912, label: "Départ" },
        { lat: 6.3603, lng: 2.4000, label: "Destination" }
    ];

    points.forEach(p => {
        L.marker([p.lat, p.lng]).addTo(map)
            .bindPopup(p.label)
            .openPopup();
    });
});


