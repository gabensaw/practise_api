from single_city_model import SingleCityModel
import requests


class City:

    def __init__(self, city):
        self.api_key = '6cea00fd3e3a08b1f706493738e21392'
        self.url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}'
        self.request = requests.get(self.url)
        self.response_json = self.request.json()

    def response_data(self):
        return SingleCityModel(self.response_json)
