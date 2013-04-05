List comprehension
-----
List comprehension constructs a conditional list in 1 statement.
```
a = [3, 2, 1, 3, 5, 7, 2, 9, 11, 23, 4, 23]
odd_items = [ element for element in a if element % 2 != 0 ]
odd_items
odd_items = [ element for element in a if element % 2 != 0 ]
odd_items
```
Set comprehension constructs a conditional set in 1 statement.
```
unique_odd_items = { element for element in a if element % 2 != 0 }
unique_odd_items
```

