Create virtual environment
--------------------------
Use `mkvirtualenv` command to create a virtual environment named `basic_python_django`.

```
mkvirtualenv basic_python_django
```

Install required python libraries
---------------------------------
Use `pip` command to install all libraries listed in `setup.pip`.

```
pip install -r setup.pip
```

Check environment
-----------------
Use `pip freeze` command to list libraries installed in the current environment.

```
pip freeze
```

If `ipython` and `nose` are in the list, you are good to go.
