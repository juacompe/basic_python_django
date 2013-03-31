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

