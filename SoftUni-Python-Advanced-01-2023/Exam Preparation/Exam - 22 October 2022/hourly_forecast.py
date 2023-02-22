def forecast(*args):
    forecast_dictionary = {}

    for location, weather in args:
        forecast_dictionary[location] = weather

    sorted_forecast = {k: v for k,v in sorted(forecast_dictionary.items(), key=lambda x: (x[1], x[0]))}
    sunny = ''
    cloudy = ''
    rainy = ''

    for location, weather in sorted_forecast.items():
        if weather == 'Sunny':
            sunny += f'{location} - {weather}\n'
        elif weather == 'Cloudy':
            cloudy += f'{location} - {weather}\n'
        elif weather == 'Rainy':
            rainy += f'{location} - {weather}\n'

    return sunny + cloudy + rainy

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
