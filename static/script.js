function fetchSensorData() {
    fetch('/fetch-sensor-data')
        .then(response => response.json())
        .then(data => {
            // Update temperature, humidity, and moisture fields
            document.querySelector('input[name="temp"]').value = data.temp;
            document.querySelector('input[name="humid"]').value = data.humid;
            document.querySelector('input[name="mois"]').value = data.mois;
            
            // Update NPK fields
            document.querySelector('input[name="nitro"]').value = data.nitro;
            document.querySelector('input[name="pota"]').value = data.pota;
            document.querySelector('input[name="phos"]').value = data.phosp;
        })
        .catch(error => console.error('Error fetching sensor data:', error));
}

// Fetch sensor data every 5 seconds
setInterval(fetchSensorData, 5000);
