from flask import Flask, request,render_template
import pickle
from sklearn.preprocessing import StandardScaler

# create an application of Flask
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index3_4.html')


@app.route("/predict", methods=["POST"])
def predict():
    Location = request.form['Location']
    MinTemp = request.form['MinTemp']
    MaxTemp = request.form['MaxTemp']
    Rainfall = request.form['Rainfall']
    Evaporation = request.form['Evaporation']
    Sunshine = request.form['Sunshine']
    WindGustDir = request.form['WindGustDir']
    WindGustSpeed = request.form['WindGustSpeed']

    WindDir3pm = request.form['WindDir3pm']

    WindSpeed3pm = request.form['WindSpeed3pm']

    Humidity3pm = request.form['Humidity3pm']

    Pressure3pm = request.form['Pressure3pm']

    Cloud3pm = request.form['Cloud3pm']

    Temp3pm = request.form['Temp3pm']
    RainToday = request.form['RainToday']

    loc = {
        'Adelaide': 0,
        'Albany': 1,
        'Albury': 2,
        'AliceSprings': 3,
        'BadgerysCreek': 4,
        'Ballarat': 5,
        'Bendigo': 6,
        'Brisbane': 7,
        'Cairns': 8,
        'Canberra': 9,
        'Cobar': 10,
        'CoffsHarbour': 11,
        'Dartmoor': 12,
        'Darwin': 13,
        'GoldCoast': 14,
        'Hobart': 15,
        'Katherine': 16,
        'Launceston': 17,
        'Melbourne': 18,
        'MelbourneAirport': 19,
        'Mildura': 20,
        'Moree': 21,
        'MountGambier': 22,
        'MountGinini': 23,
        'Newcastle': 24,
        'Nhil': 25,
        'NorahHead': 26,
        'NorfolkIsland': 27,
        'Nuriootpa': 28,
        'PearceRAAF': 29,
        'Penrith': 30,
        'Perth': 31,
        'PerthAirport': 32,
        'Portland': 33,
        'Richmond': 34,
        'Sale': 35,
        'SalmonGums': 36,
        'Sydney': 37,
        'SydneyAirport': 38,
        'Townsville': 39,
        'Tuggeranong': 40,
        'Uluru': 41,
        'WaggaWagga': 42,
        'Walpole': 43,
        'Watsonia': 44,
        'Williamtown': 45,
        'Witchcliffe': 46,
        'Wollongong': 47,
        'Woomera': 48
    }
    rain_today = {'No': 0, 'Yes': 1}

    windgustdir = {
        'E': 0, 'ENE': 1, 'ESE': 2, 'N': 3, 'NE': 4, 'NNE': 5, 'NNW': 6, 'NW': 7,
        'S': 8, 'SE': 9, 'SSE': 10, 'SSW': 11, 'SW': 12, 'W': 13, 'WNW': 14, 'WSW': 15
    }

    winddir3pm = {
        'E': 0, 'ENE': 1, 'ESE': 2, 'N': 3, 'NE': 4, 'NNE': 5, 'NNW': 6, 'NW': 7,
        'S': 8, 'SE': 9, 'SSE': 10, 'SSW': 11, 'SW': 12, 'W': 13, 'WNW': 14, 'WSW': 15
    }

    # load the model from model.pkl file
    with open('./model3_4.pkl', 'rb') as file:
        model = pickle.load(file)

    # get the prediction using model
    prediction = model.predict(
        [[loc[Location], MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, windgustdir[WindGustDir],
          WindGustSpeed,  winddir3pm[WindDir3pm],  WindSpeed3pm,
          Humidity3pm,  Pressure3pm,  Cloud3pm,  Temp3pm,
          rain_today[RainToday]]])
    # Interpret the result
    result = "Yes" if prediction[0] == 1 else "No"

    return render_template('result2.html', result=result)


# start the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
