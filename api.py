import xmltodict
import requests
from requests.auth import HTTPBasicAuth

url = "https://webservices.ns.nl/ns-api-stations-v2"
naamEnWachtwoord = HTTPBasicAuth("richietjin@gmail.com", "JAavldI8fR8iwjT540mjS4TuJ4d4BwFwbDkhV3SVvJZcqa0kX0a3Xg")
response = requests.post(url, auth=naamEnWachtwoord)

print(response)
print(response.content)

xmltodict = xmltodict.parse(response.content)
print(xmltodict)

stationCodes = []

def get_all_stations():
    for stations in xmltodict['Stations']['Station']:
        stations_namen = stations['Namen']['Lang']
        return stations_namen

def beginstation():
    stations = get_all_stations()
    while True:
       beginstation = str(input('Wat is je beginstation? : '))
       if beginstation in stations:
           return beginstation
       else:
           print('Verkeerde invoer')

def eindstation():
    while True:
       eindstation = str(input('Wat is je eindstation? : '))
       for station in xmltodict['Stations']['Station']:
           if eindstation in station['Namen']['Lang']:
               return eindstation
           else:
                print('verkeerde invoer')

def tijden(beginstation, eindstation):
    import xmltodict

    url_tijden = "http://webservices.ns.nl/ns-api-treinplanner?fromStation=" + str(beginstation) + "&toStation=" + str(eindstation) + "&departure=true"

    response = requests.post(url_tijden, auth=naamEnWachtwoord)

    print(response)
    print(response.content)

    xmltodict = xmltodict.parse(response.content)
    print(xmltodict)

# tijden(beginstation(), eindstation())
# beginstation(get_all_stations())
beginstation()