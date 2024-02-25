from flask import Flask, render_template, request, jsonify
import pickle
from arduino_data.export_data import read_line

app = Flask(__name__)
classifier = pickle.load(open('fertilizer_rec_system/classifier.pkl', 'rb'))
fertilizers = pickle.load(open('fertilizer_rec_system/fertilizers.pkl', 'rb'))

fertilizer_info = { # Possibly use the organic alternatives to estimate $ comparisons 
    "10-26-26": {
        "description": "Description of FertilizerA. Suitable for conditions X, Y, Z.",
        "alternatives": ["Organic Alternative 1", "Organic Alternative 2"]
    },
    "14-35-14": {
        "description": "Description of FertilizerB. Best used in situations A, B, C.",
        "alternatives": ["Organic Alternative 3", "Organic Alternative 4"]
    },
    "17-17-17": {
        "description": "Description of FertilizerA. Suitable for conditions X, Y, Z.",
        "alternatives": ["Organic Alternative 1", "Organic Alternative 2"]
    },
    "20-20": {
        "description": "Description of FertilizerB. Best used in situations A, B, C.",
        "alternatives": ["Organic Alternative 3", "Organic Alternative 4"]
    },
    "28-28": {
        "description": "Description of FertilizerA. Suitable for conditions X, Y, Z.",
        "alternatives": ["Organic Alternative 1", "Organic Alternative 2"]
    },
    "DAP": {
        "description": "Description of FertilizerB. Best used in situations A, B, C.",
        "alternatives": ["Organic Alternative 3", "Organic Alternative 4"]
    },
    "Urea": {
        "description": "Description of FertilizerB. Best used in situations A, B, C.",
        "alternatives": ["Organic Alternative 3", "Organic Alternative 4"]
    }
}

@app.route('/')
def welcome():
    sensor_values = read_line()
    return render_template('index.html', sensor_values=sensor_values)

@app.route('/predict', methods=['POST'])
def predict():
    sensor_values = read_line()
    soil_type = request.form['soil']
    temp, humid, mois, nitro, pota, phosp = sensor_values

    input_feature = [
        temp,
        humid,
        mois,
        int(soil_type),
        nitro,
        pota,
        phosp
    ]
    prediction = classifier.predict([input_feature])[0]
    res = fertilizers[prediction]
    fert_description = fertilizer_info[res]['description']
    org_alt = fertilizer_info[res]['alternatives']

    return render_template(
        'index.html',
        sensor_values=sensor_values,
        soil_type=soil_type,
        recommended_fertilizer=res,
        description=fert_description,
        alternatives=org_alt
    )

@app.route('/fetch-sensor-data')
def fetch_sensor_data():
    # Assume read_line() is modified or another function is used to fetch all required sensor data
    sensor_values = read_line() or (0, 0, 0, 0, 0, 0)  # Temp, Humid, Mois, Nitro, Pota, Phosp
    return jsonify({
        "temp": sensor_values[0],
        "humid": sensor_values[1],
        "mois": sensor_values[2],
        "nitro": sensor_values[3],
        "pota": sensor_values[4],
        "phosp": sensor_values[5],
    })

if __name__ == '__main__':
    app.run(debug=True)
