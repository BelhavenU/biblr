import textwrap
from functools import partial
from ...extensions import db

shorten = partial(textwrap.shorten, width=1e300)

class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    chapter_id = db.Column(
        db.Integer, db.ForeignKey('chapter.id'), nullable=False
    )
    chapter = db.relationship(
        'Chapter', backref=db.backref('verses', lazy=True)
    )

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    book = db.relationship('Book', backref=db.backref('verses', lazy=True))

    number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __repr__(self):
        return shorten(f'''
        <Verse b: {self.book.short_name} c: {self.chapter.number}
               v: {self.number} text: "{textwrap.shorten(self.text, 50)}">
        ''')

    def as_dict(self):
        return {
            'b': self.book.short_name,
            'c': self.chapter.number,
            'v': self.number,
            'text': self.text,
        }
    
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
    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    book = db.relationship('Book', backref=db.backref('chapters', lazy=True))

    number = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return shorten(f'''
        <Chapter b: {self.book.short_name} c: {self.number}>
        ''')

    def as_dict(self):
        return {
            'b': self.book.short_name,
            'c': self.number,
        }

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String, unique=True, nullable=False)
    long_name = db.Column(db.String, unique=True, nullable=False)
    testament = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return shorten(f'''
        <Book t: {self.testament} b: {self.short_name}>
        ''')

    def as_dict(self):
        return {
            'b': self.short_name,
            'long_name': self.long_name,
            'testament': self.testament,
        }
