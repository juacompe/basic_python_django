Normal python script
-----
`hello_world1.py` is a normal python script which can be run with `python` command.

```
python hello_world1.py
```

Executable python script
-----
Just execute `hello_world2` in command line.
```
./hello_world2
```

Testable python script
----
The problem with `hello_world1.py` is that the print is executed when import. Try below in `ipython`.
```
import hello_world1

from hello_world3 import hello_world
hello_world()
```
See that hello world is not printed when the module is imported.

The next problem is command line arguments. Try executing `greet` script as below.
```
./greet John
./greet Jack
./greet
```

The problem is `main` in greet is not test-able. Testing greet has to be manually done and it would get harder for complex script. In `greet2` example, `main` is tested to support much more complex options.

```
./greet2 John
echo $?
./greet2
echo $?
./greet2 -nJack
./greet2 -n Jim
./greet2 --name=Joe
./greet2 -nJim --name=Joe Jack
./greet2 -nJim --name=Joe
./greet2 -nJim -nJoe -nJua
```

References:

* [getopt — C-style parser for command line options](http://docs.python.org/2/library/getopt.html)
* [Python main() functions](http://www.artima.com/weblogs/viewpost.jsp?thread=4829)

Python execute command line
----
Use `os.system` to execute command line. The `pip freeze` command returns list of python library that being used.
```
workon basic_python_django
./pip_freeze
deactivate
./pip_freeze
```

