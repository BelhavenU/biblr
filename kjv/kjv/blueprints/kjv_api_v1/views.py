from flask import Blueprint, render_template

from .models import Book, Chapter, Verse

api_v1 = Blueprint('api_v1', __name__, template_folder='templates',
                   url_prefix='/api/v1')

@api_v1.route('/books')
def get_books():
    return {
        'books': [b.as_dict() for b in Book.query.all()]
    }

@api_v1.route('/book/<book_id>')
def get_book(book_id):
    verses = Verse.by_book(book_id)
    if not verses:
        return (
            {'success': False,
             'reason': f'no verses with book id: {book_id}'}, 400
        )
    return {
        'success': True,
        'verses': [v.as_dict() for v in verses],
    }
    
@api_v1.route('/chapter/<book_id>/<chapter_number>')
def get_chapter(book_id, chapter_number):
    verses = Verse.by_book_chapter(book_id, chapter_number)
    if not verses:
        return (
            {'success': False,
             'reason': (f'no verses with book id of {book_id} and'
                        f' chapter number of {chapter_number}')}, 400
        )
        
    return {
        'success': True,
        'verses': [v.as_dict() for v in verses]
    }

@api_v1.route('/verse/<book_id>/<chapter_number>/<verse_number>')
def get_verse(book_id, chapter_number, verse_number):
    verse = Verse.query.filter(
        Verse.book.has(short_name=book_id),
        Verse.chapter.has(number=chapter_number),
        Verse.number == verse_number
    ).first()
    if not verse:
        return (
            {'success': False,
             'reason': (f'no verses with book id of {book_id} and'
                        f' chapter number of {chapter_number} and'
                        f' verse number {verse_number}')}, 400
        )
    return {
        'success': True,
        'verse': verse.as_dict(),
    }
