Firstly, ccreate Django model, myproject>setting.py>installed_apps+'myapp',

myapp(models.py) 3 class

myapp>manament>commands>seed_data.py ＃from myapp.models導入 3 class, import random

myapp>templates>admin>combined_table.html, data_view.html

admin login #Login to the management backend

http://127.0.0.1:8000/admin/myapp/book/combined-view/ ＃View data

python manage.py dumpdata > data.json ＃Copy data Unformatted

cat data.json ＃View

python manage.py dumpdata --indent 2 > data.json ＃Copy data Formatted

cat data.json ＃View

python manage.py flush ＃Clear data

python manage.py loaddata superuser.json ＃Load management user

python manage.py loaddata data.json ＃Load data

admin login #Login to the management backend

http://127.0.0.1:8000/admin/myapp/book/combined-view/ ＃View data
