from flask import Flask
import json
import logdata.incoming
import logdata.predict
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/logdata/<userid>/<float:latitude>/<float:longitude>/<int:weekday>/<int:hour>/<int:minutesQuant>')
def logInputData(userid, latitude, longitude, weekday, hour, minutesQuant):
    # Log the user data
    inputData = logdata.incoming.Data(userid, latitude, longitude, weekday, hour, minutesQuant)
    responseJson = inputData.generateResponseJson()
    return str(responseJson)

@app.route('/logdata/<userid>/predictlocation')
def predictedLocationData(userid):
    responseJson = logdata.predict.locationPredict(userid)
    return str(responseJson)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
