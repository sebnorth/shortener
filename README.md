# shortener
## aplikacja skracająca adresy URL - ćwiczenie
### w oparciu o 

https://github.com/tehranian/django-url-shortener/tree/master/shortener


mkdir roboczy

cd roboczy

C:\Python34\python -m venv myvenv

myvenv\Scripts\activate

pip install django==1.8

pip install requests

git clone https://github.com/sebnorth/shortener.git

cd shortener

### w katalogu z plikiem manage.py należy wykonać: 

python manage.py syncdb

You have installed Django's auth system, and don't have any superusers defined.
Would you like to create one now? (yes/no): no

python manage.py create_fake_users 10

python manage.py runserver

wpisujemy w adres przeglądarki http://127.0.0.1:8000/

pod http://127.0.0.1:8000/sembed mamy listę aktualnie pobranych fakeusers

SHORT_URL_MAX_LEN = 3

