from getopt import getopt
from greet import greet
import sys

USAGE = """Usage: greet2 [OPTION]... NAME
Greet NAME.

Mandatory arguments to long options are mandatory for short options too.
  -n, --name=NAME   name to greet

Exit status:
 0  if OK,
 1  if minor problems (e.g., missing argument),
 2  if serious trouble (e.g., machine blows up!).
"""

def greet(name):
    return 'Hi %s!' % name

def echo(message):
    print message

def main(argv=[]):
    arguments = argv[1:] or sys.argv[1:]
    opts, args = getopt(arguments, 'n:', ['name='])
    name = None
    for option, value in opts:
        if option in ('-n', '--name'): 
            name = value 
    if args:
        name = args[0]
    if not name:
        echo(USAGE)
        return 1
    message = greet(name)
    echo(message)
    return 0

