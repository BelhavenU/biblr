from flask import (
    render_template, request, redirect, Blueprint, current_app, url_for,
)

from . import controller

bible = Blueprint('bible', __name__, template_folder='templates')

@bible.route('/search', methods=['post'])
def search():
    current_app.logger.info(request.form['search'])
    return redirect(url_for('page.index'))

@bible.route('/book/<book_id>')
def book_page(book_id):
    success, result = controller.get_book(book_id)
    if success:
        return render_template(
            'bible/book.html.j2',
            verses=result['verses'],
        )
    elif 'reason' in result:
        return result['reason'], 400
    return result['bad-json'], 500

@bible.route('/chapter/<book_id>/<chapter_number>')
def chapter_page(book_id, chapter_number):
    success, result = controller.get_chapter(book_id, chapter_number)
    if success:
        return render_template(
            'bible/chapter.html.j2',
            verses=result['verses'],
        )
    elif 'reason' in result:
        return result['reason'], 400
    return result['bad-json'], 500

@bible.route('/verse/<book_id>/<chapter_number>/<verse_number>')
def verse_page(book_id, chapter_number, verse_number):
    success, result = controller.get_verse(
        book_id, chapter_number, verse_number,
    )
    if success:
        return render_template(
            'bible/verse.html.j2',
            verse=result['verse'],
        )
    elif 'reason' in result:
        return result['reason'], 400
    return result['bad-json'], 500
