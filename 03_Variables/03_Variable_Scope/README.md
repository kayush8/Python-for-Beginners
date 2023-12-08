# Variable Scope

Variable scope refers to the accessibility or visibility of variables within different parts of a program. In Python, variables can have different scopes, primarily

### Global Scope

Variables defined outside of all functions or in the global scope can be accessed from anywhere in the code, including inside functions.

```python
# global_scope.py

global_var = 20  # Global variable

def my_function():
    print(global_var)  # Accessing global_var inside the function

my_function()  # Output: 20
print(global_var)  # Output: 20
```

### Local Scope

Variables defined within a function have a local scope. They are accessible only within that function and cannot be accessed from outside.

```python
# local_scope.py

def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
print(x)  # This will raise an error because 'x' is not defined in global scope
```

## Global and Local Variable Scope in Python

When you create a variable with the same name both `globally (outside any function)` and `locally (inside a function)`, Python treats them as two separate and distinct variables due to their different scopes: `global scope` and `local scope`.

```python
# global_local_scopes.py

x = 10  # Global variable 'x'

def my_function():
    x = 20  # Local variable 'x' inside the function
    print("Local x:", x)  # Output: Local x: 20

my_function()
print("Global x:", x)  # Output: Global x: 10
```

In this example:

- `x = 10` creates a global variable named `'x'` with the value `10`.
- `x = 20` inside the function `my_function()` creates a separate local variable `'x'` with the value `20`, limited in scope to the function.

## Accessing Global Variable from Inside the Function

To access the global variable from within the function without creating a new local variable, you can use the `global` keyword

```python
# accessing_global_variables.py

x = 10  # Global variable 'x'

def my_function():
    global x  # Accessing the global 'x' within the function
    x = 20  # Modifying the global 'x' value
    print("Local x:", x)  # Output: Local x: 20

my_function()
print("Global x:", x)  # Output: Global x: 20 (value modified by the function)
```

## Examples

1. [Global Scope](global_scope.py)
2. [Local Scope](local_scope.py)
3. [Global and Local Scope in Python](global_local_scopes.py)
4. [Accessing Global Variable from Inside the Function](accessing_global_variables.py)
