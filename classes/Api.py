class Api:

    def __init__(self):
        from requests.auth import HTTPBasicAuth

        self.nameAndPassword = HTTPBasicAuth('richietjin@gmail.com', 'JAavldI8fR8iwjT540mjS4TuJ4d4BwFwbDkhV3SVvJZcqa0kX0a3Xg')
        self.stationNamesUrl = "https://webservices.ns.nl/ns-api-stations-v2"

    def get_station_names(self):
        import xmltodict
        import requests
        stations_names = []

        response = requests.post(self.stationNamesUrl, auth=self.nameAndPassword)
        xmltodict = xmltodict.parse(response.content)

        for stations in xmltodict['Stations']['Station']:
            stations_names.append(stations['Namen']['Kort'])
            stations_names.append(stations['Namen']['Middel'])
            stations_names.append(stations['Namen']['Lang'])

        return stations_names

    def get_nameAndPassword(self):
        nameAndPassword = self.nameAndPassword

        return nameAndPassword