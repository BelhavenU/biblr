from collections import OrderedDict

import click

from .app import create_app
from .extensions import db
from . import data
from .blueprints.kjv_api_v1.models import Book, Chapter, Verse

# Create an app context for the database connection.
def get_context():
    app = create_app()
    db.app = app
    return app, db

@click.command()
def init_db():
    app, db = get_context()
    db.drop_all()
    db.create_all()

    book_lut = OrderedDict()
    for short_name, long_name in data.books.short_to_long.items():
        '''
        get this book's testament from data.books.short_to_testament
        set book_lut[short_name] equal to Book(short_name, long_name, testament)
        '''
    
    chapter_lut = OrderedDict()

    verse_data = list(data.verses.get_all_verses())

    verses = []

    for v in verse_data:
        '''
        get the book object from book_lut (using v['b'])
        given a chapter key of (v['b'], v['c']), see if this key is in
          chapter_lut
        if the chapter key is not in chapter_lut:
            create a new chapter object: Chapter(number=v['c'])
            set chapter.book = book
            save this new chapter object to chapter_lut[(v['b'], v['c'])]
        else:
            get the chapter object from chapter_lut
        create a new Verse object: Verse(number=v['v'], text=v['text'])
        set verse.book = book
        set verse.chapter = chapter
        add verse to verses list
        '''

    db.session.add_all(list(zip(*book_lut.items()))[1])
    db.session.add_all(list(zip(*chapter_lut.items()))[1])
    db.session.add_all(verses)
    db.session.commit()

