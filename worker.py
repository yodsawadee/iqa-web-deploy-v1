import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging

from pprint import pprint 

#from keys import api_token
#from keys import db_password

def fetch_data():
    #api_token = '0def10027afaebb7'
    #url = 'http://api.wunderground.com/api/' + api_token + '/conditions/q/CA/San_Francisco.json'

    
    api_key = '32353eaa4108f93bb492c478f11d39dc'
    #url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=' + api_key
    #url = 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=' + api_key

    city = 'Paris'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=32353eaa4108f93bb492c478f11d39dc'.format(city) 

    #url = 'http://api.openweathermap.org/data/2.5/weather?q=Bangkok&appid=32353eaa4108f93bb492c478f11d39dc'

    r = requests.get(url)
    data = r.json()

    #print(r)
    #print("----------------------------------")
    #pprint(data)

    name = data['name']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    
    wind_speed = data['wind']['speed']
    
    weather = data['weather'][0]['description']



    try:
        conn = psycopg2.connect(database='weather', user='postgres', host='localhost', password='1234')
        print("Opened DB successfully")
    except:
        print(datetime.now(), "Unable to connect to the database")
        logging.exception("Unable to open the database")
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    

    cur.execute("""INSERT INTO station_reading(name, latitude, longitude, temp, humidity, pressure, wind_speed, weather)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", (name, latitude, longitude, temp, humidity, pressure, wind_speed, weather))

    conn.commit()
    cur.close()
    conn.close()

    print("Data written", datetime.now())

fetch_data()