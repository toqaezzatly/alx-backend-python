
# Type Annotations, Duck Typing, and Code Validation in Python

This project aims to help you understand **type annotations** in Python 3, how to specify **function signatures** and **variable types**, the concept of **duck typing**, and how to validate code using **mypy**. By the end of this, you'll be able to explain these concepts to anyone without external references.

## Table of Contents
1. [Type Annotations in Python 3](#type-annotations-in-python-3)
2. [Using Type Annotations for Function Signatures and Variable Types](#using-type-annotations-for-function-signatures-and-variable-types)
3. [Duck Typing](#duck-typing)
4. [Code Validation with mypy](#code-validation-with-mypy)

---

## 1. Type Annotations in Python 3

Type annotations are a feature introduced in **Python 3.5** that allows developers to hint at the types of variables, function arguments, and return values. While Python remains a dynamically typed language, these annotations make it easier to understand the code and catch type-related bugs during development.

Example of type annotations for variables:
```python
x: int = 5
name: str = "Toqa"
```

## 2. Using Type Annotations for Function Signatures and Variable Types

With function signatures, type annotations allow us to specify the expected types for input parameters and the return type. This improves code readability and makes it easier for tools like `mypy` to validate the code.

Example:
```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```
In this example:
- `a: int` means `a` should be an integer.
- `b: int` means `b` should be an integer.
- `-> int` indicates that the function will return an integer.

### Benefits:
- Enhances code readability
- Helps catch bugs early
- Improves tool support for code validation

## 3. Duck Typing

Python uses a **duck typing** system, where the type of an object is determined by its behavior (methods and properties) rather than its explicit type. If an object "quacks like a duck," then it is treated as a duck.

Example:
```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Outputs: Woof
animal_sound(cat)  # Outputs: Meow
```
Both the `Dog` and `Cat` classes have a `speak()` method. Even though they are different types, they are treated the same because they have the same method signature.

### Key point:
- Duck typing focuses on what an object *can do*, rather than what it *is*.

## 4. Code Validation with mypy

**mypy** is a static type checker for Python that checks your type annotations to catch potential bugs before runtime. It doesn't enforce types at runtime but helps you write cleaner code by validating it.

### Installation:
```bash
pip install mypy
```

### Usage:
Once you've annotated your code, you can run mypy to check for type-related issues.
```bash
mypy your_file.py
```

Example:
```python
def greet(name: str) -> str:
    return "Hello, " + name

greet(123)  # This will raise an error in mypy
```

Running `mypy` on this code will give an error because `greet()` expects a string, but `123` is an integer.

### Benefits of mypy:
- Catches type-related bugs before runtime.
- Improves code safety.
- Works well with large codebases where maintaining types manually is hard.

---

## Summary

By using **type annotations**, you can make your Python code more understandable and easier to maintain. **Duck typing** allows flexibility while coding, and tools like **mypy** help catch errors early by validating your annotations. Together, these concepts can make your code safer and more robust.

---

## Additional Resources
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [mypy Documentation](https://mypy.readthedocs.io/)

