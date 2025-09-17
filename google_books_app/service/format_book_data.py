from pprint import pprint
from .fetch_book import fetch_by_id

def format_book_data(book):
    book_id = book.get('id')
    sale_info_data = book.get('saleInfo')
    volume_info_data = book.get('volumeInfo')
    
    authors_data = [
        {
            "name": name
        } for name in volume_info_data.get('authors')
    ]
    
    categories_data = [
        {"name": name.strip(),}
        for category in volume_info_data.get('categories', [])
        for name in category.split('/')
    ]
    
    isbn_10 = None
    isbn_13 = None
    
    for item in volume_info_data.get('industryIdentifiers'):
        if item['type'] == 'ISBN_10':
            isbn_10 = item['identifier']
        elif item['type'] == 'ISBN_13':
            isbn_13 = item['identifier']
    
    list_price = sale_info_data.get('listPrice', {})
    amount = list_price.get('amount', 0.0)
    currency_ = list_price.get('currencyCode', 'BRL')
    
    volume_info = {
        'google_book_id': book_id,
        'title': volume_info_data.get('title'),
        'publisher': volume_info_data.get('publisher'),
        'published_date': volume_info_data.get('publishedDate'),
        'description': volume_info_data.get('description'),
        'page_count': volume_info_data.get('pageCount'),
        'authors': authors_data,
        'categories': categories_data,
        'thumbnail_url': volume_info_data.get('imageLinks')['extraLarge'],
        'isbn_10': isbn_10,
        'isbn_13': isbn_13,
        'buy_link': sale_info_data.get('buyLink'),
        'price': amount,
        'currency': currency_
   }
    
    return volume_info


if __name__ == '__main__':
    book = fetch_by_id('ov8sBgAAQBAJ')
    data = format_book_data(book=book)
    pprint(data)