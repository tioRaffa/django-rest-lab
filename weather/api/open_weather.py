import requests
from .geocoding import city_geocoding
from decouple import config
from pprint import pprint


def city_weather(city_name, state_code):
    api_key = config('WEATHER_KEY')

    if not api_key:
        print('Chave API não encontrada no arquivo .env')
        return None
    
    geocode = city_geocoding(city_name, state_code)
    if geocode is not None:
        lat = geocode['latitude']
        lon = geocode['longitude']
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br"
    else:
        print('Não foi possível obter as coordenadas da cidade. Verifique o nome/código.')
        return None
    
    try:
        response = requests.get(url=url)
        data =  response.json()
        if response.status_code != 200:
            print(f"Erro na API do Clima: {data.get('message', 'Erro desconhecido')}")
            return None

        extracted_data = {
            'temperatura_atual': data['main'].get('temp'),
            'sensacao_termica': data['main'].get('feels_like'),
            'descricao': data['weather'][0].get('description'),
            'icone': data['weather'][0].get('icon'),
            'umidade': data['main'].get('humidity'),
            'velocidade_vento': data['wind'].get('speed'),
            'cidade': data.get('name'),
            'pais': data['sys'].get('country'),
        }
        return extracted_data

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
        return None


if __name__ == '__main__':
    data = city_weather('Lages', 'SC')
    pprint(data)
