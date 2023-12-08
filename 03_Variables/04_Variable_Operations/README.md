# Variable Operations in Python

## Assigning Many Values to Multiple Variables

Multiple values can be assigned to multiple variables in a single line.

```python
# multiple_values_to_multiple_variables.py

x, y, z = 10, 20, 30

print(x) # 10
print(y) # 20
print(z) # 30
```

<b>`Note:`</b> Make sure the number of variables matches the number of values, or else you will get an error.

## Assigning Same Value to Multiple Variables

You can assign same value to multiple variables in a single line.

```python
# same_value_to_multiple_variables.py

x, y, z = 10

print(x) # 10
print(y) # 10
print(z) # 10
```

## Deleting a Variable

You can delete a variable using the `del` keyword.

```python
# deleting_variable.py

x = 10
del x  # Deletes the variable 'x'

print(x) # After deletion, attempting to access x will result in an error because the variable no longer exists.
```

## Adding two variables

In Python, adding two variables typically involves performing addition using the `+` operator. You are only allowed to add two variables of the same type. Data types which supports addition of two variables are `numbers`, `strings`, `lists` and `tuples`

### Adding two numbers

Addition of two numbers performs a mathematical operation.

```python
a = 10
b = 20

print(a + b)
```

### Adding two strings

Adding two strings concatenates their values together.

```python
a = "Hello, "
b = "World!"

print(a + b) # Output: "Hello, World!"
```

### Adding two variables of different types

You cannot add two variables of different types.

```python
a = 10 # An integer
b = "20" # A string

print(a + b) # Adding variables of different types may result in a Type Error
```

## Examples

1. [Assigning Many Values to Multiple Variables](multiple_values_to_multiple_variables.py)
2. [Assigning Same Value to Multiple Variables](same_value_to_multiple_variables.py)
3. [Deleting a Variable](deleting_variable.py)
