
import requests
from PIL import Image
from io import BytesIO

def get_weather(city, api_key):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
 
    response = requests.get(url)
    
    
    if response.status_code == 200:
        data = response.json()
        
        
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        icon_code = data['weather'][0]['icon']  
        
       
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        
        
        icon_response = requests.get(icon_url)
        icon_image = Image.open(BytesIO(icon_response.content))
        
       
        return {
            'city': city_name,
            'country': country,
            'temperature': temp,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'icon': icon_image
        }
    
    else:
        print(f"Error: {response.status_code}")
        return None

def display_weather_data(weather_data):
    if weather_data:
        
        print(f"Weather in {weather_data['city']}, {weather_data['country']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        
        
        weather_data['icon'].show()

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "your_api_key_here"  

    
    weather_data = get_weather(city, api_key)
    
    
    display_weather_data(weather_data)
