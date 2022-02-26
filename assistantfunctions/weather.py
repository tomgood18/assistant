import pyowm
token = "f954d3a8e8840be50b3c45c4667d011c"
owm = pyowm.OWM(token).weather_manager()

def get_weather():
    post_code = "2000"
    weather = owm.weather_at_zip_code(post_code, "AU").weather
    temperature = int(round(weather.temperature(unit='celsius')['temp'], 0))
    return f"Currently, the temperature is {temperature} degrees"
