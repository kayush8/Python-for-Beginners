x = 10  # Global variable 'x'

def my_function():
    x = 20  # Local variable 'x' inside the function
    print("Local x:", x)  # Output: Local x: 20

my_function()
print("Global x:", x)  # Output: Global x: 10