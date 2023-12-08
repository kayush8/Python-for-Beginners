# Rules for naming a variable

When it comes to naming variables in Python, there are certain rules and conventions to follow to ensure clarity and consistency in your code. Here are the key rules for naming variables in Python

- Variable names can consist of `alpha-numeric characters and underscores (\_)`. They must start with a letter or an underscore.
- Python is case-sensitive, meaning `my_var`, `My_Var`, and `MY_VAR` would be considered as three different variables.
- Avoid using Python keywords as variable names. Keywords are reserved words in Python that have specific meanings and cannot be used as identifiers. Examples of keywords: `if`, `else`, `for`, `while`, `import`, `def`, etc.

### Valid variable names

```python
# Valid variable names
first_name = "John"
total_count = 100
is_logged_in = True
```

### Invalid variable names

```python
# Invalid variable names

1st_name = "Alice"  # Starts with a digit
for = 10            # Reserved keyword 'for'
my-variable = 5      # Contains invalid character '-'
```

## Variable naming convention

Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable

### Snake Case (Recommended for python)

All lowercase letters with words separated by underscores

```python
# Snake Case

my_variable_name = "John"
total_count = 100
is_logged_in = False
```

### Camel Case

The first word starts with a lowercase letter, and subsequent words are capitalized without spaces.

```python
# Camel Case

myVariableName = "John"
totalCount = 100
isLoggedIn = False
```

### Pascal Case

Each word starts with a capital letter

```python
# Pascal case

MyVariableName = "John"
TotalCount = 100
IsLoggedIn = False
```
