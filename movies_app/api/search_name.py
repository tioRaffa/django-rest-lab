import requests
from pprint import pprint
from decouple import config

def search_movie_by_name(movie_name: str):
    api_key = config('TMDB_API_KEY')
    if not api_key:
        print('Chave API não encontrada no arquivo .env')
        return None
    
    if not movie_name:
        print('Nome do Filme não informado')
        return None
        
        
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
    try:
        response = requests.get(url=url)
        data = response.json()
        if response.status_code != 200:
           print(f"Erro na API: {data.get('status_message', 'Error desconhecido')}")    
           return None
       
        list_films = data.get('results', [])
        if not list_films:
            print('error.. nenhum filme encontrado com este nome')
            return None
        
        filter_films = []
        for film in list_films:
            info = {
                'movie_id': film.get('id'),
                'backdrop_path': film.get('backdrop_path'),
                'title': film.get('original_title'),
                'genre_ids': film.get('genre_ids'),
                'overview': film.get('overview')
            }
            filter_films.append(info)
        
        return filter_films

    except requests.exceptions.RequestException as e:
       print(f'Erro na requisição: {e}')
       return None
    
        
if __name__ == '__main__':
    info = search_movie_by_name('batman')
    pprint(info)