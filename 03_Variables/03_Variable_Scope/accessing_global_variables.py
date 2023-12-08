x = 10  # Global variable 'x'

def my_function():
    global x  # Accessing the global 'x' within the function
    x = 20  # Modifying the global 'x' value
    print("Local x:", x)  # Output: Local x: 20

my_function()
print("Global x:", x)  # Output: Global x: 20 (value modified by the function)