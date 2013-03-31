Test with django-nose
-----
`django-nose` helps find all the tests in django project

Once have django-nose in environment add `django_nose` in `INSTALLED_APPS` in `settings` and configure `TEST_RUNNER` to be `django_nose.NoseTestSuiteRunner`.

Run test again.

```
python manage.py test
```

See that Django's tests are excluded. Only tests that we wrote are run.

Reference: [django-nose installation on GitHub](https://github.com/jbalogh/django-nose#installation)

