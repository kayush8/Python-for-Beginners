# Comments in Python

## Why Use Comments?

- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
- Comments can be used to prevent execution when testing code.

## Single-Line Comment

Single-line comments start with the `#` character and continue until the end of the line. These comments are used to annotate a single line of code.

```python
# single_line_comments.py

# This is a single-line comment
print("Hello, World!")
```

In this example, `# This is a single-line comment` is a comment, and it doesn't affect the execution of the code. It's purely for human readers to understand the code better.

## Multi-line Comment

Python doesn't have a specific syntax for multi-line comments like some other programming languages do. However, developers commonly use multi-line strings (enclosed in triple quotes - `'''` or `"""`) as a way to create multi-line comments. These multi-line strings are not assigned to any variable and are essentially ignored by the interpreter.

```python
# multi_line_comments.py

"""
This is a multi-line comment
that spans across multiple lines
"""
print("Hello, Python!")
```

Here, the triple-quoted string `"""This is a multi-line comment that spans across multiple lines"""` acts as a multi-line comment. Python considers it as a string literal but since it's not assigned to any variable or used in the code, it functions effectively as a comment.

### Conclusion

Both single-line and multi-line comments serve the purpose of adding explanations, clarifications, or context to the code, making it more understandable for developers without affecting the program's execution.

## Examples

1. [Single Line Comment](single_line_comments.py)
2. [Multi-line comment](multi_line_comments.py)
