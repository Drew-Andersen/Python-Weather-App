from django.shortcuts import render
import requests

# Create your views here.
def index(req):
    api_key = '42eafdedee5b61f0ec122008b3e95a01' 
    weather_data = None
    error_message = None

    if req.method == 'POST':
        city = req.POST.get('city')
        if city:
            geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}'
            response = requests.get(geo_url)
            if response.status_code == 200 and response.json():
                geo_data = response.json()[0]
                state = geo_data.get('state', '')
                country = geo_data.get('country', '')

                weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
                weather_res = requests.get(weather_url)

                if weather_res.status_code == 200:
                    weather_data = weather_res.json()

                    celc_temp = weather_data['main']['temp']
                    fahr_temp = (celc_temp * 9/5) + 32
                    weather_data['main']['temp_f'] = round(fahr_temp, 2)
                else:
                    error_message = 'Weather data not found. Please try again.'
            else:
                error_message = 'City not found. Please try again.'
    return render(req, 'weather_app/index.html', {'weather_data': weather_data, 'error_message': error_message})
