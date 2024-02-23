const ctx = document.getElementById('soilMoistureChart').getContext('2d');
const soilMoistureChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [], // This will hold the string labels for timestamps
        datasets: [{
            label: 'Soil Moisture',
            data: [], // Data points for soil moisture
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                type: 'category', // Using category type for simplicity with string labels
                ticks: {
                    autoSkip: true,
                    maxTicksLimit: 20 // Limit number of displayed labels
                }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true // Ensure Y-axis starts at 0
                }
            }]
        }
    }
});

// Function to fetch new data and update the chart
function fetchDataAndUpdateChart() {
    fetch('/soil-moisture')
        .then(response => response.json())
        .then(data => {
            // Assuming the backend sends data in {"moisture": value, "time": timestamp} format
            const now = new Date(data.time * 1000); // Convert UNIX timestamp to JS Date
            soilMoistureChart.data.labels.push(`${now.getHours()}:${now.getMinutes()}:${now.getSeconds()}`);
            soilMoistureChart.data.datasets.forEach((dataset) => {
                dataset.data.push(data.moisture);
            });
            soilMoistureChart.update();
        });
}

// Fetch new data every 5 seconds
setInterval(fetchDataAndUpdateChart, 5000);