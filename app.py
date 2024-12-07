import requests
from flask import Flask, request, render_template
import json
import plotly.express as px
import plotly
import calendar as cal


app = Flask(__name__)


@app.route('/')
def home():
    print("status ok")
    return render_template('templates.html')  # rendering template / zobrazenie templatu

@app.route('/main_app', methods = ["POST"])
def main_app():
    try:
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        print(latitude," " ,  longitude)

    except KeyError:
        print("chyba")
        return render_template('templates.html', error="Zadaj správne súradnice / Put right coordinates")


    api_key = 'jDcuI4N5qKw84QKC2LPbZdS1m9q8PNpuvIkBcbCk'        # API parameters for getting data
    url = 'https://developer.nrel.gov/api/pvwatts/v8.json'
    params = {
        'api_key': api_key,
        'lat': latitude,
        'lon': longitude,
        'system_capacity': 8,     #   Nameplate capacity (kW)
        'array_type': 1,          # 	Fixed - Roof Mounted
        'tilt': 20,               #   Tilt angle (degrees)
        'azimuth': 200,           #   Azimuth angle (degrees)
        'dataset': 'intl',        #   PVWatts International station data
        'timeframe': 'hourly',    #   output response
        'module_type': 0,         #   0=Standard
        'losses': 10,             #   System losses (percent)
    }

    # Request to NREL API
    response = requests.get(url, params=params)
    data = response.json()


    if 'outputs' in data:
        city = data['station_info']['city']
        print(city)
        outputs_ac = data['outputs']['ac_monthly']
        outputs_ac = [round(value) for value in outputs_ac]


        x = list(cal.month_name[1:])            # Graph making
        y = outputs_ac

        graph = px.bar(x=x, y=y, labels={'x': '', 'y': 'kWh/h'}, title= f'City: {city}')

        graph.update_layout(
            width=1400,
            height=600,

        )


        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)    # ChatGPT

        return render_template('templates.html', graphJSON=graphJSON)
    else:
        return home()


if __name__ == '__main__':
    app.run(debug=True)



