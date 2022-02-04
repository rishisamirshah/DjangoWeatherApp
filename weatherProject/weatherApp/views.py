from django.shortcuts import render

# Create your views here.

import urllib.request
import json


def index(request):
        if request.method == 'POST':
            city= request.POST['city']
            #Making API CALL
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + 
                                                            city + '&units=metric&appid=c4225a5108f92426e856c7e66445f99f').read()

            #HOLDS API CALL DATA
            list_of_data = json.loads(source)

            #data Parsed from 
            data = {
                "country_code" : str(list_of_data['sys']['country']),
                "temp" : str(list_of_data['main']['temp']) + ' °C',
                "pressure" : str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": list_of_data['weather'][0]['icon'],
            }
            print(data)
    
        else:
            data = {}
    
        return render(request, "main/index.html", data)
        