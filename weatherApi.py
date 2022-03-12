from urllib import response
import requests
import json_loader
import json
import datetime

CONFIG_DATA = json_loader.get_config()

def get_location(location_name, country_code = 'MY'):
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={},{}&limit=5&appid={}'
        .format(location_name, country_code, CONFIG_DATA['WEATHER_TOKEN']))
    
    data = json.loads(response.text)[0]

    res = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric'
        .format(data['lat'], data['lon'], CONFIG_DATA['WEATHER_TOKEN']))
    
    data = json.loads(res.text)
    
    bot_response = 'weather in ' + location_name + ' is ' + data['weather'][0]['main'] + ' with ' + data['weather'][0]['description'] + ' and temperature of ' + str(data['main']['temp']) + 'C'

    return bot_response

def next_5_days(location_name, country_code = 'MY'):
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={},{}&limit=5&appid={}'
        .format(location_name, country_code, CONFIG_DATA['WEATHER_TOKEN']))
    
    data = json.loads(response.text)[0]

    res = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}&units=metric'
        .format(data['lat'], data['lon'], CONFIG_DATA['WEATHER_TOKEN']))

    data = json.loads(res.text)['list']
    base = datetime.datetime.today()
    bot_response = ''

    for idx, val in enumerate(data):
        weather = val['weather'][0]['main']
        day = base + datetime.timedelta(days=idx)
        x = datetime.datetime.strptime(val['dt_txt'], '%Y-%m-%d %H:%M:%S')
        if(x.strftime('%A') == day.strftime('%A')):
            bot_response += ' weather for: ' + day.strftime('%A') + ' is ' + weather + '\n'
    return bot_response 





def init_location(location_name, country_code = 'MY'):

    response = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={},{}&limit=5&appid={}'
        .format(location_name, country_code, CONFIG_DATA['WEATHER_TOKEN']))

    user_location = {
        'lat': json.loads(response.text)[0]['lat'],
        'lon': json.loads(response.text)[0]['lon']
    }

    json_loader.save_personal(user_location)

