import urllib
import os
import geocoder
import requests
from django.http import JsonResponse
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json

def client_ip(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for is not None:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def location(request):

        get_ip = client_ip(request)
        # Assign IP address to a variable
        ip = geocoder.ip('67.158.116.255')
        # Obtain the city
        region = ip.city
        print(region)
        # Obtain the coordinates:
        print(ip.latlng)
        return region

def get_weather(request):

        city = location(request)
        # retreive the information using api
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=94ec71a38ab41b61960291f63e3871c1').read()

        # convert json data file into python dictionary
        list_of_data = json.loads(source)

        context =  str(list_of_data['main']['temp'])

        return context



@api_view(['GET'])
def hello(request):
    name = request.GET.get('visitor_name', 'Mark')
    ip = client_ip(request)
    client_location = location(request)
    weather = get_weather(request)

    api = {
            "client_ip": ip,
            "location": client_location,
            "greeting": f'Hello, {name}!, the temperature is {weather} degrees celcius in {client_location}'

           }
    return Response(api)