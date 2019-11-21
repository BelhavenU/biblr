import requests

def get_books():
    return requests.get('http://kjv:5000/api/v1/books').json()

def book_lut():
    return dict(get_books()['books'])

def get_api_response(result):
    try:
        data = result.json()
        return data.get('success', False), data
    except ValueError:
        return False, {'bad-json': result.content.decode()}

def get_book(book_id):
    return get_api_response(
        requests.get(
            f'http://kjv:5000/api/v1/book/{book_id}'
        )
    )

def get_chapter(book_id, chapter_number):
    return get_api_response(
        requests.get(
            f'http://kjv:5000/api/v1/chapter/{book_id}/{chapter_number}'
        )
    )

def get_verse(book_id, chapter_number, verse_number):
    return get_api_response(
        requests.get(
            f'http://kjv:5000/api/v1/verse/'
            f'{book_id}/{chapter_number}/{verse_number}'
        )
    )

