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

    book_lut = OrderedDict([
        (s, Book(
            short_name=s, long_name=l,
            testament=data.books.short_to_testament[s],
        )) for s, l in data.books.short_to_long.items()
    ])

    # db.session.add_all(list(zip(*book_lut.items()))[1])
    # db.session.commit()

    chapter_lut = OrderedDict()

    verse_data = list(data.verses.get_all_verses())

    for v in verse_data:
        book = book_lut[v['b']]
        chapter = chapter_lut.get((v['b'], v['c']))
        if not chapter:
            chapter = Chapter(number=v['c'])
            chapter.book = book
            # chapter.book_id = book.id
        chapter_lut[(v['b'], v['c'])] = chapter

    # db.session.add_all(list(zip(*chapter_lut.items()))[1])
    # db.session.commit()

    verses = []
    for v in verse_data:
        book = book_lut[v['b']]
        chapter = chapter_lut[(v['b'], v['c'])]

        verse = Verse(number=v['v'], text=v['text'])

        verse.book = book
        # verse.book_id = book.id
        verse.chapter = chapter
        # verse.chapter_id = chapter.id
        verses.append(verse)

    db.session.add_all(list(zip(*book_lut.items()))[1])
    db.session.add_all(list(zip(*chapter_lut.items()))[1])
    db.session.add_all(verses)
    db.session.commit()

# @click.group()
# def cli():
#     """ Run PostgreSQL related tasks. """
#     pass


# @click.command()
# @click.option('--with-testdb/--no-with-testdb', default=False,
#               help='Create a test db too?')
# def init(with_testdb):
#     """
#     Initialize the database.

#     :param with_testdb: Create a test database
#     :return: None
#     """
#     db.drop_all()
#     db.create_all()

#     if with_testdb:
#         db_uri = '{0}_test'.format(app.config['SQLALCHEMY_DATABASE_URI'])

#         if not database_exists(db_uri):
#             create_database(db_uri)

#     return None


# @click.command()
# def seed():
#     """
#     Seed the database with an initial user.

#     :return: User instance
#     """
#     if User.find_by_identity(app.config['SEED_ADMIN_EMAIL']) is not None:
#         return None

#     params = {
#         'role': 'admin',
#         'email': app.config['SEED_ADMIN_EMAIL'],
#         'password': app.config['SEED_ADMIN_PASSWORD']
#     }

#     return User(**params).save()


# @click.command()
# @click.option('--with-testdb/--no-with-testdb', default=False,
#               help='Create a test db too?')
# @click.pass_context
# def reset(ctx, with_testdb):
#     """
#     Init and seed automatically.

#     :param with_testdb: Create a test database
#     :return: None
#     """
#     ctx.invoke(init, with_testdb=with_testdb)
#     ctx.invoke(seed)

#     return None


# cli.add_command(init)
# cli.add_command(seed)
# cli.add_command(reset)
