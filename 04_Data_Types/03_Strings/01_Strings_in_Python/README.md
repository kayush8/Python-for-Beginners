# Strings in Python

Strings in Python are sequences of characters, and they are one of the fundamental data types used to represent text.

## String Creation

Strings can be created using single (`'`) or double (`"`) quotes. Both forms are equivalent, and you can choose the one that fits your preference or use cases.

```python
print("Hello, Python!")
print('Hello, Python!')
```

## Multiline String

You can also create multiline strings using triple quotes (`'''` or `"""`). This is especially useful when dealing with multiline text, such as docstrings or large blocks of text.

```python
multiline_string = '''
This is a
multiline
string.
'''
print(multiline_string)
```

Multiline strings preserve the line breaks and are useful for maintaining the formatting of text over multiple lines.

## Practical Usage:

- `Text Representation`: Strings are fundamental for representing and manipulating text in Python programs.

- `Printing Output`: Strings are often used with the `print()` function to display information to the user or for debugging purposes.

- `Documentation`: Multiline strings, created using triple quotes, are commonly used for docstrings, providing documentation for functions, modules, or classes.

## String Length

The length of a string can be determined using the `len()` function, which is a built-in function in Python.

```python
my_string = "Hello, Python!"
multiline_string = '''
This is a
multiline
string.
'''

print(my_string) # Output: 14
print(multiline_string) # Output: 29
```
