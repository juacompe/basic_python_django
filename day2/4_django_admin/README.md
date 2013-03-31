Enabling Django admin 
-----
Before enabling Django admin, try to access <http://localhost:8000/admin/> first.

To enable django admin, uncomment django `admin` and `admindocs` in `INSTALLED_APPS`. Then do the same in `urls.py`.

Try to access <http://localhost:8000/admin/> again.

The `DatabaseError` is raised because the database has not been created yet. Create it with `syncdb` command
```
python manage.py syncdb
```
Try again <http://localhost:8000/admin/>.

