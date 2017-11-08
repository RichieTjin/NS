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
        stations_namen.append(stations['Namen']['Kort'])
        stations_namen.append(stations['Namen']['Middel'])
        stations_namen.append(stations['Namen']['Lang'])

    woord1 = beginstation(stations_namen).replace(" ", "+")
    woord2 = eindstation(stations_namen).replace(" ", "+")

    url_tijden = "http://webservices.ns.nl/ns-api-treinplanner?fromStation=" + str(woord1) + "&toStation=" + str(
        woord2) + "&departure=true"
    return url_tijden


def get_result():
    import xmltodict
    import requests
    from requests.auth import HTTPBasicAuth

    url = str(get_url())

    naamEnWachtwoord = HTTPBasicAuth("richietjin@gmail.com", "JAavldI8fR8iwjT540mjS4TuJ4d4BwFwbDkhV3SVvJZcqa0kX0a3Xg")
    response = requests.get(url, auth=naamEnWachtwoord)
    xmltodict = xmltodict.parse(response.content)

    for tijden in xmltodict['ReisMogelijkheden']['ReisMogelijkheid']:
        print('AantalOverstappen: ' + tijden['AantalOverstappen'])
        print('GeplandeReisTijd: ' + tijden['GeplandeReisTijd'])
        print('ActueleReisTijd: ' + tijden['ActueleReisTijd'])
        print('GeplandeVertrekTijd: ' + tijden['GeplandeVertrekTijd'][11:16])
        print('ActueleVertrekTijd: ' + tijden['ActueleVertrekTijd'][11:16])
        print('GeplandeAankomstTijd: ' + tijden['GeplandeAankomstTijd'][11:16])
        print('ActueleAankomstTijd: ' + tijden['ActueleAankomstTijd'][11:16])

        if tijden['AantalOverstappen'] > '0':
            for ReisDeel in tijden['ReisDeel']:
                print('Ritnummer: ' + ReisDeel['RitNummer'])
                print('VervoerType: ' + ReisDeel['VervoerType'])
                print('Vervoerder: ' + ReisDeel['Vervoerder'])

                try:
                    for ReisStop in ReisDeel['ReisStop']:
                        print('Station: ' + ReisStop['Naam'])
                        print('Tijd: ' + ReisStop['Tijd'][11:16])
                        if 'Spoor' in ReisStop:
                            print('Spoor: ' + ReisStop['Spoor']['#text'])

                except TypeError:
                    continue
        else:
            print('Ritnummer: ' + tijden['ReisDeel']['RitNummer'])
            print('VervoerType: ' + tijden['ReisDeel']['VervoerType'])
            print('Vervoerder: ' + tijden['ReisDeel']['Vervoerder'])

            try:
                for ReisStop in tijden['ReisDeel']['ReisStop']:
                    print('Station: ' + ReisStop['Naam'])
                    print('Tijd: ' + ReisStop['Tijd'][11:16])
                    if 'Spoor' in ReisStop:
                        print('Spoor: ' + ReisStop['Spoor']['#text'])
            except TypeError:
                continue

        print(' ')


get_result()