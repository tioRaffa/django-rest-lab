import requests
from decouple import config
from pprint import pprint

def validate_movie_id(id):
    if not id:
        raise ValueError('Informe um valor do ID movie')
    try:
        return int(id)
    except ValueError:
        raise ValueError('Id invalido, forneça um ID inteiro')



def get_movie_details_by_id(id: int) -> dict:
    api_key = config('TMDB_API_KEY')
    if not api_key:
        print('Chave API não encontrada no arquivo .env')
        return None
    
    try:
        movie_id = validate_movie_id(id)
    except ValueError as e:
        print(f'Erro na validação: {e}')
        return None

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=videos,credits,release_dates"
        
    try:    
        response = requests.get(url=url)
        data = response.json()
        
        if response.status_code != 200:
            print(f'Erro na API: {data.get('status_message', 'Erro desconhecido')}')
            return None
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f'erro na requisição: {e}')
        return None
        
    



if __name__ == '__main__':
    movie = add_movie_by_id(293660)
    pprint(movie)
    