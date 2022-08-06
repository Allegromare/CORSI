"""
When texting or tweeting, it’s not uncommon to shorten words to save time or 
space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str 
of text and then outputs that same text but with all vowels (A, E, I, O, and U) 
omitted, whether inputted in uppercase or lowercase.

Hints
-----
Recall that a str comes with quite a few methods, per 
docs.python.org/3/library/stdtypes.html#string-methods.
Much like a list, a str is “iterable,” which means you can iterate over each of 
its characters in a loop. For instance, if s is a str, you could print each of 
its characters, one at a time, with code like:

for c in s:
    print(c, end="")

Demo
----
$ python twttr.py                                                               
Input: Twitter                                                                  
Output: Twttr                                                                   
$ python twttr.py                                                               
Input: What's your name?                                                        
Output: Wht's yr nm?                                                            
$ python twttr.py                                                               
Input: CS50                                                                     
Output: CS50                                                                    
$

How to test
-----------
Here’s how to test your code manually:

Run your program with python twttr.py. Type Twitter and press Enter. Your program 
should output:
Twttr   
Run your program with python twttr.py. Type What's your name? and press Enter. 
Your program should output:
Wht's yr nm?
Run your program with python twttr.py. Type CS50 and press Enter. Your program 
should output
CS50

"""


def testo_wov(s):
    vowels = ["a", "e", "i", "o", "u"]
    wov = ""

    for c in s:

        if c.lower() in vowels:
            pass
        else:
            wov = wov + c

    return wov


testo = input("Enter a word: ")
print("The word without vovels is: ", testo_wov(testo))
