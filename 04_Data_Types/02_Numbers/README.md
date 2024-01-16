# Numbers in Python

In Python, numbers are a fundamental data type that allows you to work with numeric values.

## Integer (`int`)

`Integers` are a fundamental data type representing whole numbers without any decimal points. Integers can be positive, negative, or zero.

```python
x = 10
y = -20
z = 0

print(type(x)) # <class 'int'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'int'>
```

## Floating-point Numbers (`float`)

`Floats (floating-point numbers)` are a numeric data type used to represent numbers with decimal points or numbers expressed in scientific notation.

### Characteristics of Floats:

- `Decimal Representation`: Floats can represent real numbers with decimal points, allowing for more precise numeric values.

```python
x = 3.14
y = -5.2

print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
```

- `Scientific Notation`: Floats can also be expressed in scientific notation, making them suitable for very large or very small numbers.

```python
x = 12E4
y = 6.022e23
z = 11e-4

print(x) # 120000.0
print(y) # 6.022e+23
print(z) # 0.0011

print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>
```

## Complex Numbers (`complex`)

Complex numbers are numeric data type used to represent numbers with both a real part and an imaginary part. They are written in the form `a + bj`, where `a` is the real part, `b` is the imaginary part, and `j` is the imaginary unit.

```python
x = 2 + 3j
y = -1 - 2j
z = 7 + 0j

print(type(x))
print(type(y))
print(type(z))
```

### Characteristics of Complex Numbers:

1.  `Real and Imaginary Parts`: Complex numbers consist of two parts:
    - `Real Part (a)`: The part of the complex number that does not involve the imaginary unit.
    - `Imaginary Part (bj)`: The part of the complex number that includes the imaginary unit `(j)`.
2.  `Imaginary Unit (j)`: The imaginary unit, denoted by `j` in Python, is a mathematical concept representing the square root of -1.

## Arithematic Operators

Arithmetic operators in Python are symbols used to perform basic mathematical operations on numeric values, including `integers`, `floats`, and `complex` numbers.

Consider two numeric variables, `a` and `b`, for the examples below

| Name           | Operator | Example | Code                                   |
| -------------- | -------- | ------- | -------------------------------------- |
| Addition       | +        | a + b   | [View Example](code/addition.py)       |
| Subtraction    | -        | a - b   | [View Example](code/subtraction.py)    |
| Multiplication | \*       | a \* b  | [View Example](code/multiplication.py) |
| Division       | /        | a / b   | [View Example](code/division.py)       |
| Floor Division | //       | a // b  | [View Example](code/floor_division.py) |
| Exponentiation | \*\*     | a\*\*b  | [View Example](code/exponentiation.py) |
| Modulus        | %        | a%b     | [View Example](code/modulus.py)        |
