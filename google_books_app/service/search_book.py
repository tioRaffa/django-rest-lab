import requests
from pprint import pprint
from decouple import config
from rest_framework.exceptions import ValidationError, APIException


def search_by_title(title):
    api_key = config('GOOGLE_BOOKS_API_KEY')
    if not api_key:
        raise APIException('Chave Api Key não encontrada no virtual environment.')
    
    if not title:
        raise ValidationError('Titulo invalido ou não informado')
    
    url = f"https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": title,
        "key": api_key,
        "MaxResults": 1
    }
    
    try:
        response = requests.get(url=url, params=params, timeout=5)
        data = response.json()
        
        if response.status_code != 200:
            error_message = data.get('error', {}).get('message', 'erro desconhecido')
            raise APIException(f'Erro na API: {error_message}')
        
        items = data.get('items', [])
        if not items:
            raise ValidationError('enhum Livro encontrado!')
        
        books = items[:5]        
        formated_data = [
            {
                "google_book_id": book.get('id'),
                "volumeInfo": book.get('volumeInfo')
            } for book in books
        ]
        
        return formated_data
    
    except requests.exceptions.HTTPError as e:
        raise APIException(f'Erro na API: {e}')
    
    except requests.exceptions.RequestException as e:
        raise APIException(f'Erro na requisição: {e}')
    

if __name__ == '__main__':
    books = search_by_title('por lugares incriveis')
    pprint(books)