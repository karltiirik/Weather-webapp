__author__ = 'Karl Tiirik'
#!/usr/bin/env python3.4
# App code for pythonanywhere.com
import json
import urllib.request

from bottle import default_app, route, request, template


@route('/')
def display_weather():
    ip = str(request.remote_addr)
    city = get_city(ip)
    weather = get_weather(city)
    output = html_generator(ip, city, weather)
    return output


def get_city(ip):
    api_key = '2dc467de311bfb6ce49234d80bd0b237e02784e4b703365aed3a3cc8e2d31075'
    url = 'http://api.ipinfodb.com/v3/ip-city/?key={0}&ip={1}&format=json'.format(api_key, ip)
    urlobj = urllib.request.urlopen(url)
    data = urlobj.read().decode('utf-8')
    datadict = json.loads(data)
    city = datadict['cityName'].title()
    return city


def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric'.format(city)
    urlobj = urllib.request.urlopen(url)
    data = urlobj.read().decode('utf-8')
    return json.loads(data)


def html_generator(ip, city, weather):
    desc = weather['weather'][0]['description'].lower()
    data = (('Temperature', weather['main']['temp'], 'C'),
            ('Pressure', weather['main']['pressure'], 'hPa'),
            ('Humidity', weather['main']['humidity'], '%'),
            ('Wind speed', weather['wind']['speed'], 'm/s'))
    html = template('main', ip=ip, loc=city, desc=desc, rows=data)
    return html


application = default_app()