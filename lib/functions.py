def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

def halve(num):
    result = num / 2
    print(f"Half of {num} is {result}")
    return result