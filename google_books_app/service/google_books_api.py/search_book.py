import requests
from pprint import pprint
from decouple import config


def search_by_title(title):
    api_key = config('GOOGLE_BOOKS_API_KEY')
    if not api_key:
        print('Chave Api Key não encontrada no virtual environment.')
        return
    
    if not title:
        print('Titulo invalido ou não informado')
        return None
    
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
            print(f'Erro na API: {error_message}')
            return None
        
        items = data.get('items', [])
        if not items:
            print('Nenhum Livro encontrado!')
            return None
        
        
        books = items[:5]        
        formated_data = [
            {
                "google_book_id": book.get('id'),
                "volumeInfo": book.get('volumeInfo')
            } for book in books
        ]
        
        return formated_data
            
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
        return None
    

if __name__ == '__main__':
    books = search_by_title('por lugares incriveis')
    pprint(books)