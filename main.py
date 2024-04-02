# Import necessary libraries and modules
from flask import Flask, render_template, request, jsonify, session
import pickle
from arduino_data.export_data import read_line  # Importing function to read sensor data from Arduino

# Initialize Flask application
app = Flask(__name__)
app.secret_key = "xxxxxxxxxxxxxxxx"

# Load pre-trained machine learning model and encoded fertilizer labels for fertilizer recommendation
model = pickle.load(open('fertilizer_rec_system/classifier.pkl', 'rb'))
fertilizers = pickle.load(open('fertilizer_rec_system/fertilizers.pkl', 'rb'))

# Function to fetch fertilizer information based on language preference
def get_fert_info(lang: str) -> dict:
    if lang=='es':
        fertilizer_info = {
            "10-26-26": {
                "description": "Alto contenido de fósforo, adecuado para plantas con flores.",
                "alternatives": [
                    "Harina ósea: Una fuente de fósforo de liberación lenta, que también proporciona calcio. Ideal para promover el desarrollo de raíces y flores. Es particularmente eficaz cuando se incorpora al suelo en el momento de la siembra para cultivos de raíces y bulbos.",
                    "Fosfato de roca: Ofrece una fuente de fósforo a largo plazo, que se libera lentamente a lo largo de varios años. Se aplica mejor en función de las pruebas de suelo para abordar las deficiencias de fósforo para una mejora sostenible a largo plazo.",
                    "Compost: Mejora la estructura del suelo, la retención de humedad y la actividad microbiana. Proporciona una amplia gama de nutrientes, incluidas pequeñas cantidades de N-P-K, mejorando la salud general de las plantas y la fertilidad del suelo."
                ],
                "resources": [
                    "https://www.gardeners.com/how-to/vegetable-gardening/5069.html",
                    "https://www.epa.gov/recycle/composting-home"
                ],
            },
            "14-35-14": {
                "description": "Fomenta el desarrollo de raíces y la floración.",
                "alternatives": [
                    "Guano murciélago: Rico en fósforo, con relaciones N-P-K variables dependiendo de la fuente. Promueve el crecimiento y la floración de las raíces. Algunos tipos también ofrecen un impulso rápido de nitrógeno. Es de acción rápida y se puede utilizar como aderezo superior o preparado en un té rico en nutrientes.",
                    "Harina ósea: Una fuente de fósforo de liberación lenta, que también proporciona calcio. Ideal para promover el desarrollo de raíces y flores. Es particularmente eficaz cuando se incorpora al suelo en el momento de la siembra para cultivos de raíces y bulbos."
                ],
                "resources": ["https://www.youtube.com/watch?v=IOu0DuxFAT0"]
            },
            "17-17-17": {
                "description": "Fertilizante equilibrado para la salud general del jardín.",
                "alternatives": [
                    "Estiércol compostado (por ejemplo, pollo, vaca): Proporciona nutrientes equilibrados. El estiércol de pollo es más alto en nitrógeno, mientras que el estiércol de vaca es más equilibrado. Use estiércol bien compostado para minimizar el riesgo de quemar plantas.",
                    "Harina de sangre: Una fuente de nitrógeno de acción rápida, se puede usar junto con harina de huesos y compost para crear una mezcla equilibrada de N-P-K. Es particularmente eficaz para promover el crecimiento verde y frondoso.",
                    "Harina ósea: Una fuente de fósforo de liberación lenta, que también proporciona calcio. Ideal para promover el desarrollo de raíces y flores. Es particularmente eficaz cuando se incorpora al suelo en el momento de la siembra para cultivos de raíces y bulbos."
                ],
                "resources": ["https://www.snapgardens.org/snap-participant/"]
            },
            "20-20": {
                "description": "Fertilizante de propósito general para mantener la salud del jardín.",
                "alternatives": [
                    "Emulsión de pescado: Proporciona nitrógeno, fósforo y potasio rápidamente disponibles, junto con oligoelementos. Adecuado para la alimentación general, especialmente durante la temporada de crecimiento.", 
                    "Algas marinas: ofrece un amplio espectro de oligoelementos y hormonas vegetales, mejorando la salud de las plantas y la resistencia al estrés. Se trata más de mejorar la vitalidad general de las plantas que de proporcionar nutrientes primarios"
                ],
                "resources": ["https://communitygarden.org/"]
            },
            "28-28": {
                "description": "Fertilizante equilibrado, adecuado para todas las etapas de crecimiento.",
                "alternatives": [
                    "Harina de semilla de algodón: De liberación lenta, ácida, con una relación equilibrada N-P-K sesgada hacia el nitrógeno. Bueno para plantas amantes de los ácidos y como fertilizante orgánico general con el tiempo.",
                    "Harina ósea: Una fuente de fósforo de liberación lenta, que también proporciona calcio. Ideal para promover el desarrollo de raíces y flores. Es particularmente eficaz cuando se incorpora al suelo en el momento de la siembra para cultivos de raíces y bulbos."
                ],
                "resources": [
                    "https://www.gardeners.com/how-to/vegetable-gardening/5069.html",
                    "https://www.epa.gov/recycle/composting-home"
                ]
            },
            "DAP": {
                "description": "Alto en nitrógeno, adecuado para el crecimiento de hojas verdes.",
                "alternatives": [
                    "Estiércol de pollo: Alto contenido en nitrógeno y fósforo, es excelente para las primeras etapas de crecimiento de las plantas. Asegúrese de que esté bien compostado para evitar quemar plantas y reducir los patógenos.",
                    "Fosfato de roca: Ofrece una fuente de fósforo a largo plazo, que se libera lentamente a lo largo de varios años. Se aplica mejor en función de las pruebas de suelo para abordar las deficiencias de fósforo para una mejora sostenible a largo plazo."
                ],
                "resources": ["https://www.youtube.com/watch?v=n9OhxlrWwc", "https://www.gardeners.com/"]
            },
            "Urea": {
                "description": "Fuente rápida de nitrógeno para el crecimiento de hojas verdes.",
                "alternatives": [
                    "Fosfato de roca: Ofrece una fuente de fósforo a largo plazo, que se libera lentamente a lo largo de varios años. Se aplica mejor en función de las pruebas de suelo para abordar las deficiencias de fósforo para una mejora sostenible a largo plazo.",
                    "Harina de soja: Proporciona nitrógeno durante un período de liberación moderado, lo que favorece el crecimiento vegetativo. Es un subproducto de la producción de aceite de soja, lo que lo convierte en una opción sostenible para el nitrógeno orgánico."
                ],
                "resources": ["https://www.epa.gov/recycle/composting-home", "https://communitygarden.org/"]
            }}
    else:
        fertilizer_info = {
            "10-26-26": {
                "description": "High phosphorus content, suitable for flowering plants.",
                "alternatives": [
                    "Bone Meal: A slow-release phosphorus source, also providing calcium. Ideal for promoting root and flower development. It's particularly effective when incorporated into the soil at planting time for root crops and bulbs.",
                    "Rock Phosphate: Offers a long-term phosphorus source, releasing slowly over several years. Best applied based on soil tests to address phosphorus deficiencies for sustainable, long-term improvement.",
                    "Compost: Enhances soil structure, moisture retention, and microbial activity. Provides a wide range of nutrients, including minor amounts of N-P-K, improving overall plant health and soil fertility."
                ],
                "resources": [
                    "https://www.gardeners.com/how-to/vegetable-gardening/5069.html",
                    "https://www.epa.gov/recycle/composting-home"
                ],
            },
            "14-35-14": {
                "description": "Promotes root development and flowering.",
                "alternatives": [
                    "Bat Guano: Rich in phosphorus, with varying N-P-K ratios depending on the source. Promotes root growth and flowering. Some types also offer a quick nitrogen boost. It's fast-acting and can be used as a top dressing or brewed into a nutrient-rich tea.",
                    "Bone Meal: A slow-release phosphorus source, also providing calcium. Ideal for promoting root and flower development. It's particularly effective when incorporated into the soil at planting time for root crops and bulbs."
                ],
                "resources": ["https://www.youtube.com/watch?v=IOu0DuxFAT0"]
            },
            "17-17-17": {
                "description": "Balanced fertilizer for overall garden health.",
                "alternatives": [
                    "Composted Manure (e.g., Chicken, Cow): Provides balanced nutrients. Chicken manure is higher in nitrogen, while cow manure is more balanced. Use well-composted manure to minimize the risk of burning plants.",
                    "Blood Meal: A fast-acting nitrogen source, it can be used in conjunction with bone meal and compost to create a balanced N-P-K mix. It's particularly effective in promoting green, leafy growth.",
                    "Bone Meal: A slow-release phosphorus source, also providing calcium. Ideal for promoting root and flower development. It's particularly effective when incorporated into the soil at planting time for root crops and bulbs."
                ],
                "resources": ["https://www.snapgardens.org/snap-participant/"]
            },
            "20-20": {
                "description": "All-purpose fertilizer for maintaining garden health.",
                "alternatives": [
                    "Fish Emulsion: Provides quickly available nitrogen, phosphorus, and potassium, along with trace elements. Suitable for general feeding, especially during the growing season.",
                    "Seaweed/Kelp: Offers a broad spectrum of trace minerals and plant hormones, improving plant health and stress resistance. It's more about enhancing overall plant vitality than providing primary nutrients"
                ],
                "resources": ["https://communitygarden.org/"]
            },
            "28-28": {
                "description": "Balanced fertilizer, suitable for all growth stages.",
                "alternatives": [
                    "Cottonseed Meal: Slow-release, acidic, with a balanced N-P-K ratio skewed towards nitrogen. Good for acid-loving plants and as a general organic fertilizer over time.",
                    "Bone Meal: A slow-release phosphorus source, also providing calcium. Ideal for promoting root and flower development. It's particularly effective when incorporated into the soil at planting time for root crops and bulbs."
                ],
                "resources": [
                    "https://www.gardeners.com/how-to/vegetable-gardening/5069.html",
                    "https://www.epa.gov/recycle/composting-home"
                ]
            },
            "DAP": {
                "description": "High in nitrogen, suitable for leafy growth.",
                "alternatives": [
                    "Chicken Manure: High in nitrogen and phosphorus, it’s excellent for early plant growth stages. Ensure it is well-composted to avoid burning plants and to reduce pathogens.",
                    "Rock Phosphate: Offers a long-term phosphorus source, releasing slowly over several years. Best applied based on soil tests to address phosphorus deficiencies for sustainable, long-term improvement."
                ],
                "resources": ["https://www.youtube.com/watch?v=n9OhxlrWwc", "https://www.gardeners.com/"]
            },
            "Urea": {
                "description": "Rapid nitrogen source for green leafy growth.",
                "alternatives": [
                    "Soybean Meal: Provides nitrogen over a moderate release period, supporting vegetative growth. It’s a by-product of soybean oil production, making it a sustainable choice for organic nitrogen.",
                    "Rock Phosphate: Offers a long-term phosphorus source, releasing slowly over several years. Best applied based on soil tests to address phosphorus deficiencies for sustainable, long-term improvement."
                ],
                "resources": ["https://www.epa.gov/recycle/composting-home", "https://communitygarden.org/"]
            }}
    return fertilizer_info

@app.route('/')
def welcome():
    sensor_values = read_line()
    return render_template('index.html', sensor_values=sensor_values)

@app.route('/fetch-sensor-data')
def fetch_sensor_data():
    # Assume read_line() is modified or another function is used to fetch all required sensor data
    sensor_values = read_line() or (0, 0, 0, 0, 0, 0)  # Temp, Humid, Mois, Nitro, Pota, Phosp
    return jsonify({
        "temp": sensor_values[4],
        "humid": sensor_values[5],
        "mois": sensor_values[3],
        "nitro": sensor_values[0],
        "pota": sensor_values[1],
        "phosp": sensor_values[2],
    })

@app.route('/predict', methods=['POST'])
def predict():
    lang = request.form.get('lang', 'en')

    fert_info = get_fert_info(lang)
    temp = int(request.form['temp'])
    humid = int(request.form['humid'])
    soil_mois = int(request.form['mois'])
    nitro = int(request.form['nitro'])
    pota = int(request.form['pota'])
    phosp = int(request.form['phos'])
    soil_type = int(request.form['soil'])
    
    input_features = [temp, humid, soil_mois, soil_type, nitro, pota, phosp]
    res = fertilizers.classes_[model.predict([input_features])[0]]
    return render_template(
        'index.html',
        sensor_values=(temp, humid, soil_mois, nitro, pota, phosp),
        soil_type=soil_type,
        recommended_fertilizer=res,
        description=fert_info[res]['description'],
        alternatives=fert_info[res]['alternatives'],
        resources=fert_info[res]['resources'],
        fertilizer_info=fert_info
    )

@app.route('/gardening-tips')
def gardening_tips():
    return render_template('gardening_tips.html')

@app.route('/set-language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
