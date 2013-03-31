MVC in Django
-----
To create django project, type the command below
```
django-admin.py startproject my_first_app
```

Run test to check our environment
```
cd my_first_app/
python manage.py test
```

Whoa! That's a hell lot of errors. ;P

Don't worry. Add database configuration in `settings.py` and try again.
```
python manage.py test
```
Yes! You are good to go!

Run server
-----
Simply start server with Django's `runserver` command.
```
python manage.py runserver 0:8000
```
Access <http://localhost:8000/> in your browser.

Start Django App
-----
Start a new app with `startapp` command.
```
python manage.py startapp thestar
```
Find `models.py`, `views.py` and `tests.py` in the app.

**Note** views in Django means Controller in MVC.
