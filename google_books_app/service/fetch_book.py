import requests
from pprint import pprint
from decouple import config
from rest_framework.exceptions import ValidationError, APIException


def fetch_by_id(google_book_id):
    api_key = config('GOOGLE_BOOKS_API_KEY')
    if not api_key:
        raise APIException('Chave Api Key não encontrada no virtual environment.')
    
    if not google_book_id:
        raise ValidationError('Google Book ID não informado ou invalido.')
    
    url = f'https://www.googleapis.com/books/v1/volumes/{google_book_id}'
    params = {"key": api_key}
    
    try:
        response = requests.get(url=url, params=params, timeout=10)
        data = response.json()
        if response.status_code != 200:
            error_message = data.get('error',[]).get('message', 'erro desconhecido')
            raise APIException(f'Erro na API: {error_message}')
        
        return data
    
    except requests.exceptions.RequestException as e:
        raise APIException(f'Erro na requisição da API: {e}')
    except requests.exceptions.HTTPError as e:
        raise APIException(f'Erro na API: {e}')
    
if __name__ == '__main__':
    info = fetch_by_id('ov8sBgAAQBAJ')
    pprint(info)