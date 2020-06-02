<h2>Парсер для разделов Авито на Python Beautiful Soup</h2>
<h3>с веб-интерфейсом на Python Flask (демо)</h3>

Функционал скрипта:
- Приятный, простой и понятный веб-интерфейс
- Парсинг разделов avito.ru по ссылке
- Получаемые данные: Заголовок, Цена, Адрес (местоположение), Номер телефона
- Преобразование полученных данных в удобочитаемый формат .xlsx
- Отправка итогового документа на введенный e-mail адрес

Установка и использование:<br>
<code>git clone https://github.com/arud3nko/av-parser-demo.git</code><br>
<code>apt-get install tesseract-ocr</code><br>
<code>pip3 install -r requirements.txt</code><br>
<code>python3 start.py</code><br>
<code>http://localhost:5000/</code><br>
<br>
Загрузить chromedriver для вашей системы: <code>https://chromedriver.chromium.org/downloads</code>

Для корректной работы скрипта необходимо настроить <b>options.py</b>:<br>
<code>pytesseract.pytesseract.tesseract_cmd = 'tesseract'</code> - Команда для вызова Tesseract<br>
<code>path_driver = './chromedriver'</code> - Путь к chromedriver<br>
<code>from_mail = 'noreply@your.mail'</code> - Адрес, с которого будем отправлять документ<br>
<code>from_passwd = 'yourcoolpassword'</code> - Пароль<br>
<code>smtp_server = 'smtp.yandex.ru'</code> - SMTP сервер<br>
<code>smtp_port = '465'</code> - Порт<br>

<br>

У проекта огромный todo-лист, буду им заниматься ;)<br>
Благодарю за уделенное время. Мой Telegram: <i>@arud3nko</i>
