from flask import Flask
from flask import render_template
import json
import os
import logdata.incoming
import logdata.predict
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# Depricated
@app.route('/logdata/<userid>/<float:latitude>/<float:longitude>/<int:weekday>/<int:hour>/<int:minutesQuant>')
def logInputData(userid, latitude, longitude, weekday, hour, minutesQuant):
    # Log the user data
    inputData = logdata.incoming.Data(userid, latitude, longitude, weekday, hour, minutesQuant)
    responseJson = inputData.generateResponseJson()
    return str(responseJson)

# Depricated
@app.route('/logdata/<userid>/predictlocation')
def predictedLocationData(userid):
    responseJson = logdata.predict.locationPredict(userid)
    return str(responseJson)

@app.route('/location-predict/api/v1/logdata/<userid>/<float:latitude>/<float:longitude>/<int:weekday>/<int:hour>/<int:minutesQuant>')
def logInputDataV1(userid, latitude, longitude, weekday, hour, minutesQuant):
    # Log the user data
    inputData = logdata.incoming.Data(userid, latitude, longitude, weekday, hour, minutesQuant)
    responseJson = inputData.generateResponseJson()
    return str(responseJson)

@app.route('/location-predict/api/v1/predict-res/<userid>')
def predictedLocationDataV1(userid):
    responseJson = logdata.predict.locationPredict(userid)
    return str(responseJson)

@app.route('/location-predict/download-sqlite')
def downloadDB():
    uploads = os.path.join(current_app.root_folder, app.config['UPLOAD_FOLDER'])
    print("F-Path: {}".format(uploads))
    return redirect("/location-predict/", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
