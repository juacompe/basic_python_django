Normal python script
-----
`hello_worl1.py` is a normal python script which can be run with `python` command.

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
The problem with `hello_worl1.py` is that the print is executed when import. Try below in `ipython`.
```
import hello_world1

from hello_world3 import hello_world
hello_world()
```
See that hello world is not printed when the module is imported.

