# Python-web-server

Задание будет посвящено разработке веб-приложения для ведения базы музыкальных альбомов.
Требования:
1. Веб-сервер принимает GET-запросы по адресу /albums/<artist> и выводит на экран сообщение с количеством альбомов исполнителя artist и списком названий этих альбомов.
2. Веб-сервер принимает POST-запросы по адресу /albums/ и сохраняет переданные пользователем данные об альбоме.
   Данные передаются в формате веб-формы. Если пользователь пытается передать данные об альбоме, который уже есть в базе данных, обработчик запроса отвечает
   HTTP-ошибкой 409 и выводит соответствующее сообщение.
3. Набор полей в передаваемых данных полностью соответствует схеме таблицы album базы данных.
4. В качестве исходной базы данных использовать файл albums.sqlite3.
5. До попытки сохранить переданные пользователем данные, нужно провалидировать их. Проверить, например, что в поле "год выпуска" передан действительно год.

The task will be devoted to the development of a web application for maintaining a database of music albums.
Requirements:
1. The web server accepts GET requests to the address / albums / <artist> and displays a message on the screen with the number of albums by artist artist and a list of these album titles.
2. The web server accepts POST requests to / albums / and stores the album data submitted by the user.
   The data is transmitted in web form format. If the user tries to pass data about an album that is already in the database, the request handler responds
   HTTP error 409 and displays an appropriate message.
3. The set of fields in the transmitted data fully corresponds to the schema of the album table of the database.
4. Use the albums.sqlite3 file as a source database.
5. Before trying to save the data submitted by the user, you need to validate it. Check, for example, that the year is actually passed in the "year of manufacture" field.
