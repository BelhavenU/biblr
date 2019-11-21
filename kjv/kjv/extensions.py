from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def all_extensions():
    return [
        db,
    ]
