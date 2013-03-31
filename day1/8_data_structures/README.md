List
-----
List can have duplicated items. Try snippet below in `ipython`.
```
a = [1, 2, 3, 4, 5]
a.append(1)
a.append(2)
a.append(3)

a
```
Try removing `1`.
```
a.remove(1)
a
a.remove(1)
a
```
Combine 2 lists.
```
a + [2, 3, 4]
a
```
Iterate through a list.
```
for item in a:
    print item
```
Use `enumerate` for indexes of each item.
```
for index, item in enumerate(['a', 'b', 'c']):
    print '%s) %s' % (index, item)
```
Use `zip` to iterate 2 lists together.
```
warriors = ["Aragon", "Gimli", "Legolas"]
weapons = ["sword", "axe", "bow"]
for warrior, weapon in zip(warriors, weapons):
    print "%s uses %s." % (warrior, weapon)
```
Use `len` to count items in a list
```
len(warriors)
```
List can be multiplied!
```
warriors * 3
```
Indexing item in a list.
```
a = ['apple', 'banana', 'orange', 'grape', 'lemon']
a[0]
a[4]
a[-1]
a[-2]
a[1:3]
a[1:]
a[:3]
```
String is actually a list
```
for char in 'abcdef':
    print '%s %s' % (char, type(char))
```

Stack
-----
Stack is just a list.
```
a = [1,2,3,4]
a.append(5)
a
a.pop()
a
```

Queue
-----
Use `dequeue` to transform a list into queue.
```
from collections import deque
q = deque([1,2,3,4])
q.popleft()
q
```

Range
-----
Range is a list of number. 
```
range(0,10)
range(5,10)
range(1, 10, 2)
range(2, 10, 2)
```

Set
-----
Turn a list into set.
```
set([1,2,3,4,5,4,3,2,1])
```
Set operations:
```
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7, 8])
a - b
a & b # intersection
a | b # union
a.union(b)
a ^ b # XOR
a.isdisjoint(b)
a.issubset(b)
```

Dictionary
-----
Dictionary contains key and value
```
d = { 'name': 'kid', 'age': 8 }
d['name']
d['age']

d = dict()
d['name'] = 'kid'
d['age'] = 8
d['name']
d['age']
```

Functional programming
-----
`reduce` concludes a list into an element
```
def max(x, y):
    return x if x > y else y

a = [3,4,2,1,7,8,29,39,12,11]
max(3,5)
max(7,5)
reduce(max, a)
```

`map` apply a function to all element in a list.
```
def power(x):
    return x*x

map(power, a)
```

`filter` filter elements out of a list according to condition in the given function.
```
def is_even(x):
    return x if x % 2 == 0 else None

is_even(1)
is_even(0)
is_even(2)
is_even(5)
filter(is_even, a)
```

