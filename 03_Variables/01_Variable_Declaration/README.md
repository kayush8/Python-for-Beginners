# Variable Declaration in Python

In Python, variable declaration is a process of assigning a name (identifier) to a value. Unlike some other programming languages, Python doesn’t require explicit declaration to reserve memory space for variables. Instead, variables are created the moment you assign a value to them.

## Syntax for Variable Declaration

```
variable_name = value
```

- `variable_name`: It's the name given to the variable.
- `value`: It's the data that the variable holds. It can be a number, string, boolean, list, etc.

### Examples:

```python
# variable_declaration.py

# A String
name = "John"

# An Integer
age = 23

# Float data type
salary = 5932.42

print("Name:", name) # John
print("Age:", age)  # 23
print("Salary:", salary)  # 5932.42
```

`Dynamic Typing in Python`: Python is dynamically typed, meaning you don't have to declare the data type explicitly. The interpreter automatically identifies the data type based on the value assigned to the variable.

## Reassigning Variables

Variables in Python can be reassigned to new values of different types without explicit type declaration.

```python
# reassigning_variable.py

x = 5  # x is an integer
x = "Hello!"  # x is now a string

print(x) # Hello!
```

This flexibility allows for easy manipulation and handling of variables in Python.

## Examples

1. [Variable Declaration](variable_declaration.py)
2. [Reassigning Variable](reassigning_variable.py)
