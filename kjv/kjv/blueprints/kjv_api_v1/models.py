import textwrap
from functools import partial
from ...extensions import db

shorten = partial(textwrap.shorten, width=1e300)

class Verse(db.Model):
    '''Verse database ORM model
    '''
    # id is an integer column with primary_key set to True

    # number is an integer column that is not nullable

    # text is a string column that is not nullable
    
    # book_id is an integer column that is a db.ForeignKey to
    # 'book.id' that is not nullable

    # book is a db.relationship with the 'Book' object with a
    # backref to db.backref('verses', lazy=True)

    # chapter_id is an integer column that is a db.ForeignKey to
    # 'chapter.id' that is not nullable

    # chapter is a db.relationship with the 'Chapter' object with a
    # backref to db.backref('verses', lazy=True)

    def __repr__(self):
        return shorten(f'''
        <Verse b: {self.book.short_name} c: {self.chapter.number}
               v: {self.number} text: "{textwrap.shorten(self.text, 50)}">
        ''')

    def as_dict(self):
        '''as_dict should return dictionary with the following key, value
        pairs

        - 'b' -> the short_name attribute of self.book
        - 'c' -> the number attribute of self.chapter
        - 'v' -> the number attribute of self
        - 'text' -> the text attribute of self
        '''
    
    @classmethod
    def by_book(cls, book_id):
        return Verse.query.filter(
            Verse.book.has(short_name=book_id)
        ).all()
        
    @classmethod
    def by_book_chapter(cls, book_id, chapter_number):
        return Verse.query.filter(
            Verse.book.has(short_name=book_id),
            Verse.chapter.has(number=chapter_number),
        ).all()
        
    @classmethod
    def by_book_chapter_verse(cls, book_id, chapter_number, verse_number):
        return Verse.query.filter(
            Verse.book.has(short_name=book_id),
            Verse.chapter.has(number=chapter_number),
            Verse.number == verse_number,
        ).first()
        

class Chapter(db.Model):
    '''Chapter database ORM model
    '''
    
    # id is an integer column with primary_key set to True

    # book_id is an integer column that is a db.ForeignKey to
    # 'book.id' that is not nullable

    # book is a db.relationship with the 'Book' object and a
    # backref to db.backref('chapters', lazy=True)

    # number is an integer column that is not nullable
    
    def __repr__(self):
        return shorten(f'''
        <Chapter b: {self.book.short_name} c: {self.number}>
        ''')

    def as_dict(self):
        '''as_dict should return dictionary with the following key, value
        pairs

        - 'b' -> the short_name attribute of self.book
        - 'c' -> the number attribute of self
        '''

class Book(db.Model):
    '''Book database ORM model

    '''
    
    # id is an integer column with primary_key set to True

    # short_name is a string column that is unique and not nullable

    # long_name is a string column that is unique and not nullable

    # testament is a string column that is not nullable
    
    def __repr__(self):
        return shorten(f'''
        <Book t: {self.testament} b: {self.short_name}>
        ''')

    def as_dict(self):
        '''as_dict should return dictionary with the following key, value
        pairs

        - 'b' -> the short_name attribute of self
        - 'l' -> the long_name attribute of self
        - 't' -> the testament attribute of self
        '''
        
