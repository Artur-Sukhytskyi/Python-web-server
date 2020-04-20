import os

import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, MetaData, Table
from bottle import HTTPError

path = "sqlite:///albums.sqlite3"
Base = declarative_base()

class InvalidAlbum(HTTPError):
    pass

class BadRequest(InvalidAlbum):
    """ошибка 400"""
    pass

class Conflict(InvalidAlbum):
    """ошибка 409"""
    pass

class NotFound(InvalidAlbum):
    """ошибка 404"""
    pass

def create_db(path):

    metadata = sql.MetaData()
    artist_table = Table("albums", metadata,
                         sql.Column("id", Integer, primary_key=True),
                         sql.Column("year", Integer),
                         sql.Column("artist", String),
                         sql.Column("genre", String),
                         sql.Column("album", String),
                         )

    metadata.create_all(sql.create_engine(path))

def valid_artist(albums_list):

    if not albums_list:
        raise NotFound()

    return True

def valid_album(album):

    if album.year != None:
        
        if not album.year.isdigit() or len(album.year) > 4 or len(album.year) < 1:
            raise BadRequest(400, "Введите год цифрами, в формате - 2009")

    name = db.query(Albums).filter(Albums.album == album.album).first()
    
    if name:
        raise Conflict(409, "Альбом с таким именем уже существует")

    return True

def con_db(path):
    engine = sql.create_engine(path)
    sessions = sessionmaker(engine)
    session = sessions()
    return session

class Albums(Base):
    
    __tablename__ = "albums"
    id = sql.Column(sql.INTEGER, primary_key=True)

    year = sql.Column(sql.INTEGER)
    artist = sql.Column(sql.TEXT)
    genre = sql.Column(sql.TEXT)
    album = sql.Column(sql.TEXT)

def find(name):
    
    artists = db.query(Albums).filter(Albums.artist == name).all()
    return artists

def commit(album):
   
    db.add(album)
    db.commit()
    b = db.query(Albums).all()
    for i in b:
        print(i.year, i.artist, i.genre, i.album)

db = con_db(path)

if not os.path.exists(path):
    create_db(path)