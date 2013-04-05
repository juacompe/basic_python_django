Static variable type
-----
```
x = 3
type(x)
x = 'hello world!'
type(x)
x = 3.0
type(x)
```

Heterogeneous array
-----
```
a = [3, 'hello world', 3.0]
a
for element in a:
    print type(element)
```

Object attribute
-----
```
class Student(object):
    def __init__(self):
        self.id = 0
    def set_name(self, name):
        self.name = name


s = Student()
s.id
s.name
s.set_name("John")
s.name
%hist
s.gpa = 3.7
s.gpa


class Teacher(object):
    job = 'teacher' # static member


joey = Teacher()
joey.name = 'Joey'
print joey.name
print joey.job
print Teacher.job
```

