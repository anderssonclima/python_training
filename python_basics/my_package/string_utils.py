"""
string_utils.py

A simple utility module for common string operations.
"""

def capitalize_words(text):
    """Return a string capitalized."""
    return text.upper()

def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]

def count_vowels(text):
    """Return the number of vowels in the given string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if the given string is a palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
