# Data Types in Python

Python is dynamically typed, which means you don't explicitly declare the data type of a variable; it's inferred at runtime. Here are the primary built-in data types in Python.

| Category | Data Types                         |
| -------- | ---------------------------------- |
| Numeric  | `int`, `float`, `complex`          |
| Text     | `str`                              |
| Sequence | `list`, `tuple`, `range`           |
| Boolean  | `bool`                             |
| Mapping  | `dict`                             |
| Set      | `set`, `frozenset`                 |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| None     | `None`                             |

## Getting the Data Type

You can easily determine the data type of any object using the `type()` function or the `isinstance()` function.

### Using `type()` function

The `type()` function returns the type of an object.

```python
# type_function.py

x = 5
print(type(x)) # Output: <class 'int'>
```

### Using `isinstance()` function

The `isinstance()` function checks if an object is an instance of a particular class or data type. It allows checking against multiple types as well.

```python
# isinstance_function.py

x = "Hello, Python!"
print(isinstance(x, str)) # Output: True
print(isinstance(x, (int, float))) # Output: False
```

This function takes two parameters: the object you want to check and the type or types (as a tuple) you want to check against. It returns `True` if the object matches the specified type(s) and `False` otherwise.

These methods are helpful when you're working with variables or objects whose type might not be explicitly known or when you need to verify the type of an object before performing specific operations on it.

## Setting a Data Type

In Python, the data type of is set when you assign a value to a variable

| Example                           | Data Type  | Code                               |
| --------------------------------- | ---------- | ---------------------------------- |
| x = "Hello, Python!"              | str        | [View Example](code/str.py)        |
| x = 10                            | int        | [View Example](code/int.py)        |
| x = 3.14                          | float      | [View Example](code/float.py)      |
| x = 2 + 3j                        | complex    | [View Example](code/complex.py)    |
| x = True                          | boolean    | [View Example](code/boolean.py)    |
| x = [1, 2, 3, 4]                  | list       | [View Example](code/list.py)       |
| x = ("apple", "banana", "cherry") | tuple      | [View Example](code/tuple.py)      |
| x = {"name": "John", "age": 25}   | dict       | [View Example](code/dict.py)       |
| x = range(5)                      | range      | [View Example](code/range.py)      |
| x = {1, 2, 3, 4}                  | set        | [View Example](code/set.py)        |
| x = frozenset({1, 2, 3, 4})       | frozenset  | [View Example](code/frozenset.py)  |
| x = b"Hello, Python!"             | bytes      | [View Example](code/bytes.py)      |
| x = bytearray(5)                  | bytearray  | [View Example](code/bytearray.py)  |
| x = memoryview(bytes(5))          | memoryview | [View Example](code/memoryview.py) |
| x = None                          | None Type  | [View Example](code/none.py)       |
