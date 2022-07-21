from single_city import City

city_name = input('Provide city to check upcoming weather forecast: ')

city = City(city_name)

message = f'{city_name}, temperature {city.response_data().upcoming_temperature},' \
          f' pressure {city.response_data().upcoming_pressure}, humidity {city.response_data().upcoming_humidity} on ' \
          f'{city.response_data().date_time_list()[0]}'

print(message)

# print(city.response_data().date_time_list())
# print(city.response_data().upcoming_forecast)
#
# print(city.response_data().upcoming_temperature)
# print(city.response_data().upcoming_pressure)
# print(city.response_data().upcoming_humidity)
