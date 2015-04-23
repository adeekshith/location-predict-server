from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/logdata/<userid>/<float:latitude>/<float:longitude>/<int:weekday>/<int:hour>/<int:minutesQuant>')
def show_user_profile(userid,latitude,longitude,weekday,hour,minutesQuant):
    # Log the user data
    responseData = {}
    responseData['prediction'] = {}
    responseData['prediction']['latitude'] = latitude
    responseData['prediction']['longitude'] = longitude
    responseData['status'] = {}
    responseData['status']['situation'] = 'normal'
    responseData['status']['action'] = 'none'
    responseJson = json.dumps(responseData)
    print "responseJson: {}".format(responseJson)
    return str(responseJson)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
