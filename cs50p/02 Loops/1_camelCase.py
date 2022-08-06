"""
Source: en.wikipedia.org/wiki/Camel_case

In some languages, it’s common to use camel case (otherwise 
known as “mixed case”) for variables’ names when those names 
comprise multiple words, whereby the first letter of the first 
word is lowercase but the first letter of each subsequent word 
is uppercase. For instance, whereas a variable for a user’s 
name might be called name, a variable for a user’s first name 
might be called firstName, and a variable for a user’s preferred 
first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are 
instead separated by underscores (_), with all letters in 
lowercase. For instance, those same variables would be called 
name, first_name, and preferred_first_name, respectively, in 
Python.

In a file called camel.py, implement a program that prompts the 
user for the name of a variable in camel case and outputs the 
corresponding name in snake case. Assume that the user’s input 
will indeed be in camel case.

Hits
----
Recall that a str comes with quite a few methods, per 
docs.python.org/3/library/stdtypes.html#string-methods.

Much like a list, a str is “iterable,” which means you can 
iterate over each of its characters in a loop. For instance, 
if s is a str, you could print each of its characters, one at 
a time, with code like:

for c in s:
    print(c, end="")


Demo
----
$ python camel.py                                                               
camelCase: name                                                                 
snake_case: name                                                                
$ python camel.py                                                               
camelCase: firstName                                                            
snake_case: first_name                                                          
$ python camel.py                                                               
camelCase: preferredFirstName                                                   
snake_case: preferred_first_name                                                
$                       

How to test
-----------
Here’s how to test your code manually:

Run your program with python camel.py. Type name and press Enter. 
Your program should output:
name   
Run your program with python camel.py. Type firstName and press 
Enter. Your program should output:
first_name
Run your program with python camel.py. Type preferredFirstName 
and press Enter. Your program should output
preferred_first_name
"""


def main():
    camelCase = input("Please insert a variable name in camelCase: ")

    print("This is the variable name in snake_case: ", from_camel_to_snake(camelCase))


def from_camel_to_snake(camel_string):
    snake_string = ""

    for c in camel_string:
        if c.isupper():
            snake_string = snake_string + "_" + c.lower()
        else:
            snake_string = snake_string + c
    return snake_string


main()
