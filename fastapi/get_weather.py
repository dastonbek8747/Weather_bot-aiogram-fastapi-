import requests
from typing import Dict, Union
import os
from dotenv import load_dotenv
from typing import Dict, Union

load_dotenv()

API_KEY = os.getenv("WEATHER_API")
BASE_URL = os.getenv("BASE_URL")


def get_current_weather(city_name: str, country_code: str = None, lang: str = 'en') -> Dict[str, Union[float, str]]:
    location = f"{city_name},{country_code}" if country_code else city_name
    url = f"{BASE_URL}/weather?q={location}&appid={API_KEY}&units=metric&lang={lang}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'icon': data['weather'][0]['icon']
        }
    except requests.exceptions.RequestException as e:
        return {'error': f"So'rovda xato: {str(e)}"}
    except KeyError as e:
        return {'error': f"Ma'lumotlarni tahlil qilishda xato: {str(e)}"}


def get_weekly_forecast(city_name: str, country_code: str = None, lang: str = 'en') -> Dict[str, Union[list, str]]:
    location = f"{city_name},{country_code}" if country_code else city_name
    url = f"{BASE_URL}/forecast?q={location}&appid={API_KEY}&units=metric&lang={lang}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        daily_forecasts = {}
        for entry in data['list']:
            date = entry['dt_txt'].split(' ')[0]
            temp = entry['main']['temp']
            if date not in daily_forecasts:
                daily_forecasts[date] = {
                    'temps': [],
                    'descriptions': [],
                    'icons': []
                }
            daily_forecasts[date]['temps'].append(temp)
            daily_forecasts[date]['descriptions'].append(entry['weather'][0]['description'])
            daily_forecasts[date]['icons'].append(entry['weather'][0]['icon'])

        forecast_list = []
        for date, info in daily_forecasts.items():
            forecast_list.append({
                'date': date,
                'min_temp': min(info['temps']),
                'max_temp': max(info['temps']),
                'description': max(set(info['descriptions']), key=info['descriptions'].count),  # eng ko‘p uchragan
                'icon': info['icons'][0]  # birinchi ikonani olamiz
            })

        return {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'forecast': forecast_list[:7]  # faqat 7 kunlik
        }
    except requests.exceptions.RequestException as e:
        return {'error': f"So'rovda xato: {str(e)}"}
    except KeyError as e:
        return {'error': f"Ma'lumotlarni tahlil qilishda xato: {str(e)}"}

# get_weather.py
import requests
from typing import Dict, Union
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API")
BASE_URL = os.getenv("BASE_URL")


def get_current_weather(city_name: str, country_code: str = None, lang: str = 'en') -> Dict[str, Union[float, str]]:
    location = f"{city_name},{country_code}" if country_code else city_name
    url = f"{BASE_URL}/weather?q={location}&appid={API_KEY}&units=metric&lang={lang}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'icon': data['weather'][0]['icon']
        }
    except requests.exceptions.RequestException as e:
        return {'error': f"So'rovda xato: {str(e)}"}
    except KeyError as e:
        return {'error': f"Ma'lumotlarni tahlil qilishda xato: {str(e)}"}


def get_weekly_forecast(city_name: str, country_code: str = None, lang: str = 'en') -> Dict[str, Union[list, str]]:
    location = f"{city_name},{country_code}" if country_code else city_name
    url = f"{BASE_URL}/forecast?q={location}&appid={API_KEY}&units=metric&lang={lang}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        daily_forecasts = {}
        for entry in data['list']:
            date = entry['dt_txt'].split(' ')[0]
            temp = entry['main']['temp']
            if date not in daily_forecasts:
                daily_forecasts[date] = {
                    'temps': [],
                    'descriptions': [],
                    'icons': []
                }
            daily_forecasts[date]['temps'].append(temp)
            daily_forecasts[date]['descriptions'].append(entry['weather'][0]['description'])
            daily_forecasts[date]['icons'].append(entry['weather'][0]['icon'])

        forecast_list = []
        for date, info in daily_forecasts.items():
            forecast_list.append({
                'date': date,
                'min_temp': min(info['temps']),
                'max_temp': max(info['temps']),
                'description': max(set(info['descriptions']), key=info['descriptions'].count),
                'icon': info['icons'][0]
            })

        return {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'forecast': forecast_list[:7]
        }
    except requests.exceptions.RequestException as e:
        return {'error': f"So'rovda xato: {str(e)}"}
    except KeyError as e:
        return {'error': f"Ma'lumotlarni tahlil qilishda xato: {str(e)}"}


# 🔄 Qilinadigan asyncron wrapperlar
async def get_date_day(city_name: str):
    return get_current_weather(city_name, "UZ", "uz")


async def get_date_week(city_name: str):
    return get_weekly_forecast(city_name, "UZ", "uz")
