class SingleCityModel:

    def __init__(self, city):
        self.http_code = city['cod']
        self.forecasts = city['list']

    def date_time_list(self):
        date_time_list = []
        for timestamp in self.forecasts:
            date_time_list.append(timestamp['dt_txt'])
        return date_time_list
