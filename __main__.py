from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/logdata/<userid>/<latitude>/<longitude>/<int:weekday>/<int:hour>/<int:minutesQuant>')
def show_user_profile(userid,latitude,longitude,weekday,hour,minutesQuant):
    # Log the user data
    return 'User {}, {}, {}, {}, {}, {}'.format(userid, latitude, longitude, weekday, hour, minutesQuant)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
