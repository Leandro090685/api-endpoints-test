import requests
from .service_check import CheckService

class RegisterService:

    def register(city):
        if (not city):
            r = requests.get("http://ip-api.com/json/")
            city = r.json()["city"]
            
        CheckService.check(ciudad=city)
        r= requests.get("https://wttr.in/"+ city +"?format=j1&lang=es")

        data= r.json()
        temperature = data["current_condition"][0]["temp_C"]
        humidity = data["current_condition"][0]["humidity"]
        feels_like = data["current_condition"][0]["FeelsLikeC"]
        final_data = {
            "city":city,
            "temperature": temperature,
            "humidity": humidity,
            "feels_like": feels_like,
        }
        return final_data
