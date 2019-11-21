from flask import url_for


class TestBible(object):
    def test_book_page(self, client):
        """ Index page should respond with a success 200. """
        response = client.get(url_for('bible.book_page', book_id='le'))
        assert response.status_code == 200

    def test_chapter_page(self, client):
        """ Index page should respond with a success 200. """
        response = client.get(url_for('bible.chapter_page', book_id='le',
                                      chapter_number=0))
        assert response.status_code == 200

    def test_verse_page(self, client):
        """ Index page should respond with a success 200. """
        response = client.get(url_for('bible.verse_page', book_id='le',
                                      chapter_number=0, verse_number=0))
        assert response.status_code == 200

