import xmltodict
import requests
from requests.auth import HTTPBasicAuth

url = "https://webservices.ns.nl/ns-api-stations-v2"
naamEnWachtwoord = HTTPBasicAuth("richietjin@gmail.com", "JAavldI8fR8iwjT540mjS4TuJ4d4BwFwbDkhV3SVvJZcqa0kX0a3Xg")
response = requests.post(url, auth=naamEnWachtwoord)

xmltodict = xmltodict.parse(response.content)

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

def get_url():
    stations_namen = []
    for stations in xmltodict['Stations']['Station']:
        stations_namen.append(stations['Namen']['Lang'])

    # woord1 = beginstation(stations_namen).replace(" ", "+")
    # woord2 = eindstation(stations_namen).replace(" ", "+")

    # url_tijden = "http://webservices.ns.nl/ns-api-treinplanner?fromStation=" + str(woord1) + "&toStation=" + str(woord2) + "&departure=true"
    url_test = "http://webservices.ns.nl/ns-api-treinplanner?fromStation=Utrecht+Centraal&toStation=Rotterdam+Centraal&departure=true"

    return url_test

def get_result():
    import xmltodict
    import requests
    from requests.auth import HTTPBasicAuth

    url = str(get_url())

    naamEnWachtwoord = HTTPBasicAuth("richietjin@gmail.com", "JAavldI8fR8iwjT540mjS4TuJ4d4BwFwbDkhV3SVvJZcqa0kX0a3Xg")
    response = requests.get(url, auth=naamEnWachtwoord)
    xmltodict = xmltodict.parse(response.content)

    vertrek_tijden = []

    for tijden in xmltodict['ReisMogelijkheden']['ReisMogelijkheid']:
        print('GeplandeReisTijd: ' + tijden['GeplandeReisTijd'])
        print('ActueleReisTijd: ' + tijden['ActueleReisTijd'])
        print('GeplandeVertrekTijd: ' + tijden['GeplandeVertrekTijd'])
        print('ActueleVertrekTijd: ' + tijden['ActueleVertrekTijd'])
        print('GeplandeAankomstTijd: ' + tijden['GeplandeAankomstTijd'])
        print('ActueleAankomstTijd: ' + tijden['ActueleAankomstTijd'])
        print('VervoerType: ' + tijden['ReisDeel']['VervoerType'])
        for ReisStop in tijden['ReisDeel']['ReisStop']:
            print('Naam: ' + ReisStop['Naam'])
            # print('Spoor: ' + ReisStop['Spoor']['#text'])

get_result()