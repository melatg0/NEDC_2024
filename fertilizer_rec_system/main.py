from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
classifier = pickle.load(open(r'fertilizer_rec_system\classifier.pkl', 'rb'))
fertilizers = pickle.load(open(r'fertilizer_rec_system\fertilizers.pkl', 'rb'))


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
    res = fertilizers.classes_[classifier.predict([input])]
    return render_template('index.html', x=f'Predicted Fertilizer is {res}')


if __name__ == '__main__':
    app.run(debug=True)

''' 1 routes information from arduino as averages over time 
# 2 gets reccomendation for fertilizer from classifer.pkl
# 3 lists data from arduino, organic/cost-effective alternatives on website
# 4 remember to set up informative, pretty website '''