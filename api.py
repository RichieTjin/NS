import xmltodict
import requests
from requests.auth import HTTPBasicAuth

url = "https://webservices.ns.nl/ns-api-stations-v2"
naamEnWachtwoord = HTTPBasicAuth("richietjin@gmail.com", "JAavldI8fR8iwjT540mjS4TuJ4d4BwFwbDkhV3SVvJZcqa0kX0a3Xg")
response = requests.post(url, auth=naamEnWachtwoord)

xmltodict = xmltodict.parse(response.content)

stationCodes = []

def beginstation(stations_namen):
    while True:
       beginstation = str(input('Wat is je beginstation? : '))
       if beginstation in stations_namen:
           return beginstation
       else:
           print('Verkeerde invoer')

def eindstation(stations_namen):
    while True:
       eindstation = str(input('Wat is je eindstation? : '))
       if eindstation in stations_namen:
           return eindstation
       else:
            print('verkeerde invoer')

# def tijden(beginstation, eindstation):
#     import xmltodict
#
#
#     response = requests.post(url_tijden, auth=naamEnWachtwoord)
#
#     print(response)
#     print(response.content)
#
#     xmltodict = xmltodict.parse(response.content)
#     print(xmltodict)

def get_result():
    stations_namen = []
    for stations in xmltodict['Stations']['Station']:
        stations_namen.append(stations['Namen']['Lang'])

    url_tijden = "http://webservices.ns.nl/ns-api-treinplanner?fromStation=" + str(beginstation(stations_namen)) + "&toStation=" + str(beginstation(stations_namen)) + "&departure=true"

    print(url_tijden)

get_result()