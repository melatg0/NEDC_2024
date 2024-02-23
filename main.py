from flask import Flask, request, render_template, jsonify
import pickle
import time 
from arduino_data.export_data import get_soil_value

app = Flask(__name__)
classifier = pickle.load(open(r'fertilizer_rec_system\classifier.pkl', 'rb'))
fertilizers = pickle.load(open(r'fertilizer_rec_system\fertilizers.pkl', 'rb'))

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
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp = request.form.get('temp')
    humid = request.form.get('humid')
    mois = request.form.get('mois')
    soil_type = request.form.get('soil')
    nitro = request.form.get('nitro')
    pota = request.form.get('pota')
    phosp = request.form.get('phos')
    input = [
        int(temp),
        int(humid),
        int(mois),
        int(soil_type),
        int(nitro),
        int(pota),
        int(phosp)
        ]
    res = fertilizers.classes_[classifier.predict([input])][0]
    fert_description = fertilizer_info[res]['description']
    org_alt = fertilizer_info[res]['alternatives']
    return render_template(
        'index.html',
        temp=temp,
        humid=humid,
        mois=mois,
        soil_type=soil_type,
        nitro=nitro,
        pota=pota,
        phosp=phosp,
        recommended_fertilizer=res,
        description=fert_description,
        alternatives=org_alt
    )

@app.route('/soil-moisture')
def soil_moisture():
    # Simulate getting a soil moisture value
    moisture_value = get_soil_value()
    return jsonify({"moisture": moisture_value, "time": time.time()})

if __name__ == '__main__':
    app.run(debug=True)