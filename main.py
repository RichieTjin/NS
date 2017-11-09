from classes import Api

api = Api.Api()

stations_names = api.get_station_names()
nameAndPassword = api.get_nameAndPassword()

def get_url():
    """Returns the URL of the API"""
    word1 = startstation(stations_names).replace(" ", "+")
    word2 = endstation(stations_names).replace(" ", "+")

    url_times = "http://webservices.ns.nl/ns-api-treinplanner?fromStation=" + str(word1) + "&toStation=" + str(word2) + "&departure=true"

    return url_times

def startstation(stations_names):
    """User inputs his station where he/she wants to departure"""
    while True:
        startstation = str(input('Wat is je beginstation? : '))
        if startstation in stations_names:
            return startstation
        else:
            print('Verkeerde invoer')

def endstation(stations_names):
    """User inputs his station of destination"""
    while True:
        endstation = str(input('Wat is je eindstation? : '))
        if endstation in stations_names:
            return endstation
        else:
            print('Verkeerde invoer')

def get_result():
    """Using the URL of the API.

    1. Parse into the XML-file
    2. Make use of a for loop
    3. Getting to right data
    4. Print the data for user

    """
    import xmltodict
    import requests

    url = str(get_url())

    naamEnWachtwoord = nameAndPassword
    response = requests.get(url, auth=naamEnWachtwoord)
    xmltodict = xmltodict.parse(response.content)

    for time in xmltodict['ReisMogelijkheden']['ReisMogelijkheid']:
        print('AantalOverstappen: ' + time['AantalOverstappen'])
        print('GeplandeReisTijd: ' + time['GeplandeReisTijd'])
        print('ActueleReisTijd: ' + time['ActueleReisTijd'])
        print('GeplandeVertrekTijd: ' + time['GeplandeVertrekTijd'][11:16])
        print('ActueleVertrekTijd: ' + time['ActueleVertrekTijd'][11:16])
        print('GeplandeAankomstTijd: ' + time['GeplandeAankomstTijd'][11:16])
        print('ActueleAankomstTijd: ' + time['ActueleAankomstTijd'][11:16])

        if time['AantalOverstappen'] > '0':
            for ReisDeel in time['ReisDeel']:
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
            print('Ritnummer: ' + time['ReisDeel']['RitNummer'])
            print('VervoerType: ' + time['ReisDeel']['VervoerType'])
            print('Vervoerder: ' + time['ReisDeel']['Vervoerder'])

            try:
                for ReisStop in time['ReisDeel']['ReisStop']:
                    print('Station: ' + ReisStop['Naam'])
                    print('Tijd: ' + ReisStop['Tijd'][11:16])
                    if 'Spoor' in ReisStop:
                        print('Spoor: ' + ReisStop['Spoor']['#text'])
            except TypeError:
                continue

        print(' ')

get_result()