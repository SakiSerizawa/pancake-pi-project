from flask import Flask, render_template
import json
import turtle
import urllib.request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!!'

# @app.route('/hello/<name>/')
# def hello(name):
#    return render_template('page.html', name=name)

@app.route('/issMap')
def issMap():
    

    url = 'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    str_response = response.read().decode('utf-8')
    result = json.loads(str_response)
    print('People in Space:', result['number'])

    people = result['people']
    for p in people:
        print(p['name'] + ' in ' + p['craft']) 
        

    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    str_response = response.read().decode('utf-8')
    result = json.loads(str_response)
    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('Longitude: ' + lon)
    print('Latitude: ' + lat)

    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.png')

    #screen.register_shape('iss2.png')
    #iss = turtle.Turtle()
    #iss.shape('iss2.png')
    #iss.setheading(90)

    #iss.penup()
    #iss.goto(lon, lat)

    # My house in Burnaby
    lat = 49.2361620
    lon = -123.0195460
    location = turtle.Turtle()
    location.penup()
    location.color('yellow')
    location.goto(lon, lat)
    location.dot(3)
    location.hideturtle()

    url = 'http://api.open-notify.org/iss-pass.json'  
    url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
    response = urllib.request.urlopen(url)
    str_response = response.read().decode('utf-8')
    result = json.loads(str_response)

    over = result['response'][1]['risetime']
    #print(over)

    style = ('Arial', 5, 'bold')
    location.write(time.ctime(over),font =style)

    #Johanasburg
    lat1 = -26.204103
    lon1= 28.047304 
    location.penup()
    location.color('blue')
    location.goto(lon1, lat1)
    location.dot(3)
    location.hideturtle()

    url = 'http://api.open-notify.org/iss-pass.json'  
    url = url + '?lat=' + str(lat1) + '&lon=' + str(lon1)
    response = urllib.request.urlopen(url)
    str_response = response.read().decode('utf-8')
    result = json.loads(str_response)

    over1 = result['response'][2]['risetime']

    style = ('Arial', 5, 'bold')
    location.write(time.ctime(over1),font =style)
    return;


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    
