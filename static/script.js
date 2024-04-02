function checkNPKRanges() {
    // Define the good ranges for each soil type
    const goodRanges = {
        nitrogen: {low: 100, high: 200},
        phosphorus: {low: 100, high: 142},
        potassium: {low: 200, high: 400},
        moisture: {low: 400, high: 600} // Define the good range for soil moisture
    };

    // Retrieve the current NPK values from the input boxes
    const nitrogenValue = parseInt(document.querySelector('input[name="nitro"]').value);
    const phosphorusValue = parseInt(document.querySelector('input[name="phos"]').value);
    const potassiumValue = parseInt(document.querySelector('input[name="pota"]').value);
    const moistureValue = parseInt(document.querySelector('input[name="mois"]').value); // Retrieve soil moisture value

    // Check if values are within the good ranges and update the background color
    document.querySelector('input[name="nitro"]').style.backgroundColor = (nitrogenValue >= goodRanges.nitrogen.low && nitrogenValue <= goodRanges.nitrogen.high) ? '#90EE90' : '#FFFF99';
    document.querySelector('input[name="phos"]').style.backgroundColor = (phosphorusValue >= goodRanges.phosphorus.low && phosphorusValue <= goodRanges.phosphorus.high) ? '#90EE90' : '#FFFF99';
    document.querySelector('input[name="pota"]').style.backgroundColor = (potassiumValue >= goodRanges.potassium.low && potassiumValue <= goodRanges.potassium.high) ? '#90EE90' : '#FFFF99';
    document.querySelector('input[name="mois"]').style.backgroundColor = (moistureValue >= goodRanges.moisture.low && moistureValue <= goodRanges.moisture.high) ? '#90EE90' : '#FFFF99'; // Update soil moisture background color
}


// Call the checkNPKRanges function after the sensor data is fetched and on every subsequent fetch
function fetchSensorData() {
    fetch('/fetch-sensor-data')
        .then(response => response.json())
        .then(data => {
            // Update the sensor data input fields
            document.querySelector('input[name="temp"]').value = data.temp;
            document.querySelector('input[name="humid"]').value = data.humid;
            document.querySelector('input[name="mois"]').value = data.mois;
            document.querySelector('input[name="nitro"]').value = data.nitro;
            document.querySelector('input[name="pota"]').value = data.pota;
            document.querySelector('input[name="phos"]').value = data.phosp;

            checkNPKRanges();
        })
        .catch(error => console.error('Error fetching sensor data:', error));
}

// Fetch sensor data every 5 seconds and check NPK ranges
setInterval(fetchSensorData, 3000);