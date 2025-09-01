import requests 
from decouple import config
from pprint import pprint

def city_geocoding(city_name, state_code):
    api_key = config("WEATHER_KEY")
    if not api_key:
        print('Chave API não encontrada no arquivo .env')
        return None

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},BR&limit=1&appid={api_key}"

    try:
        response = requests.get(url=url)
        data =  response.json() if response.status_code == 200 else None
        
        if data and len(data) > 0:
            geocode = {}
            geocode['latitude'] = data[0].get('lat')
            geocode['longitude'] = data[0].get('lon')

            return geocode
        else:
            print('Nenhum dado encontrado para a cidade especificada!')
            return None
    
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
        return None
    

if __name__ == "__main__":
    weather_in_lages = city_geocoding('Lages', 'SC')
    pprint(weather_in_lages)