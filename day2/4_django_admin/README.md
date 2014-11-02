Enabling Django admin 
-----
Try to access <http://localhost:8000/admin/>.

The `DatabaseError` is raised because the database has not been created yet. Create it with `migrate` command

```
python manage.py migrate 
```

Try again <http://localhost:8000/admin/>.

