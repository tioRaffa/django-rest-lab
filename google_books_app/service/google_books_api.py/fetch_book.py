import requests
from pprint import pprint
from decouple import config


def fetch_by_id(google_book_id):
    api_key = config('GOOGLE_BOOKS_API_KEY')
    if not api_key:
        print('have Api Key não encontrada no virtual environment.')
        return None
    
    if not google_book_id:
        print('Google Book ID não informado ou invalido.')
        return None
    
    url = f'https://www.googleapis.com/books/v1/volumes/{google_book_id}'
    params = {
        "key": api_key
    }
    
    try:
        response = requests.get(url=url, params=params, timeout=10)
        data = response.json()
        if response.status_code != 200:
            error_message = data.get('error',[]).get('message', 'erro desconhecido')
            print(f'Erro na API: {error_message}')
            return None
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f'erro na requisição da API: {e}')
        return None
    
if __name__ == '__main__':
    info = fetch_by_id('ov8sBgAAQBAJ')
    pprint(info)