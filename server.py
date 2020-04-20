import db_injector
from db_injector import valid_album

from bottle import run
from bottle import request
from bottle import route
from bottle import HTTPError

@route('/albums/<artist>')
def albums(artist):
    
    albums_list = db_injector.find(artist.title())
   
    try:
       
        db_injector.valid_artist(albums_list)
    except db_injector.NotFound:
        
        result = HTTPError(404, "Альбомов от исполнителя {} не найдено".format(artist.upper()))
    else:
        albums_names = [album.album for album in albums_list]
        result = "Количество найденныйх альбомов {}: {} <br><br>".format(artist.upper(), len(albums_list))
        result += "<br>".join(albums_names)

    return result

@route('/albums', method="POST")
def add_album():
    
    album = db_injector.Albums(
        year=request.forms.get("year"),
        artist=request.forms.get("artist").title(),
        genre=request.forms.get("genre").title(),
        album=request.forms.get("album").title()
    )

    try:
        valid_album(album)

    except db_injector.BadRequest as err:

        result = HTTPError(400, "Введите год цифрами, в формате - 2009")

    except db_injector.Conflict as err:

        result = HTTPError(409, "Альбом с таким именем уже существует")

    else:
        db_injector.commit(album)
        result = "Был добавлен новый альбом \nГод - {}\nИсполнитель - {} \nЖанр - {} \nАльбом - {}".format(album.year,album.artist,album.genre,album.album)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)