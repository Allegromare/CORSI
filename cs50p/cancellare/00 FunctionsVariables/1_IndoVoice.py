"""
Implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

Hints
-----
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
"""

messaggio = input("Scrivi un testo:")

print(messaggio.lower())
