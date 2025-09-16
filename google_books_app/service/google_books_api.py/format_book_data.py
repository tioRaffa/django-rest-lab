from locale import currency
from pprint import pprint
from fetch_book import fetch_by_id

def format_book_data(book):
    book_id = book.get('id')
    sale_info_data = book.get('saleInfo')
    volume_info_data = book.get('volumeInfo')
    
    
    volume_info = {
        'title': volume_info_data.get('title'),
        'publisher': volume_info_data.get('publisher'),
        'published_date': volume_info_data.get('publishedDate'),
        'description': volume_info_data.get('description'),
        'page_count': volume_info_data.get('pageCount'),
        # 'authors': ...,
        # 'categories': ...,
        'thumbnail_url': volume_info_data.get('imageLinks')['extraLarge'],
        # 'isbn_10': ...,
        # 'isbn_13': ...,
    }
    
    list_price = sale_info_data.get('listPrice', {})
    amount = list_price.get('amount', 0.0)
    currency_ = list_price.get('currencyCode', 'BRL')
    
    sale_info = {
        'buyLink': sale_info_data.get('buyLink'),
        'price': amount,
        'currency': currency_,
    }
    
    
    formated_data = {
        'book_id': book_id,
        'volumeInfo': volume_info,
        'saleInfo': sale_info
    }
    
    
    return formated_data


if __name__ == '__main__':
    book = fetch_by_id('ov8sBgAAQBAJ')
    data = format_book_data(book=book)
    pprint(data)