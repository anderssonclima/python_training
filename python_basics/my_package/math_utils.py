"""
math_utils.py

A simple utility module for basic math operations.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
