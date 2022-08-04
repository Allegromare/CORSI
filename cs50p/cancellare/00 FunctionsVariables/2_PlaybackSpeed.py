"""
Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

Hints
-----
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.

Example
-------
$ python playback.py
This is CS50.
This...is...CS50.
$
"""

text = input("Immetti una stringa: ")

text = text.strip().replace(" ", "...")

print(text)
