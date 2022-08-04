"""
In deep.py, implement a program that prompts the user for the 
answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) 
forty-two or forty two. Otherwise output No.

Hints
-----
No need to convert the user’s input to an int if you check for 
equality with "42", a str, rather than 42, an int!
It’s okay if your output or the user’s wraps onto multiple lines.

Example
-------
$ python deep.py                                                                                    
What is the Answer to the Great Question of Life, the Universe, and Everything? 42                  
Yes                                                                                                 
$ python deep.py                                                                                    
What is the Answer to the Great Question of Life, the Universe, and Everything? forty-two           
Yes                                                                                                 
$ python deep.py                                                                                    
What is the Answer to the Great Question of Life, the Universe, and Everything? forty two           
Yes                                                                                                 
$ python deep.py                                                                                    
What is the Answer to the Great Question of Life, the Universe, and Everything? 1           
No                                                                                                 
$       
"""

response = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

if (
    response == "42"
    or response.casefold() == "forty-two"
    or response.casefold() == "forty two"
    or response.casefold() == "fortytwo"
):
    print("Yes")
else:
    print("No")
