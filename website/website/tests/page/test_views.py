from flask import url_for


class TestPage(object):
    def test_index_page(self, client):
        """ Index page should respond with a success 200. """
        response = client.get(url_for('page.index'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_faq(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200
