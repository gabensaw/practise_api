class SingleCityModel:

    def __init__(self, city):
        self.http_code = city['cod']
        self.forecasts = city['list']
        self.upcoming_forecast = city['list'][0]
        self.upcoming_temperature = '{:.1f} °C'.format(round(self.upcoming_forecast['main']['temp'] - 273.15, 1))
        self.upcoming_pressure = f"{self.upcoming_forecast['main']['pressure']} hPa"
        self.upcoming_humidity = f"{self.upcoming_forecast['main']['humidity']} %"

    def date_time_list(self):
        date_time_list = []
        for timestamp in self.forecasts:
            date_time_list.append(timestamp['dt_txt'])
        return date_time_list
