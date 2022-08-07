"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity 
license plate for your car, with your choice of letters and numbers instead of 
random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and 
a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For 
example, AAA222 would be an acceptable … vanity plate; AAA22A would not be 
acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and 
then output Valid if meets all of the requirements or Invalid if it does not. 
Assume that any letters in the user’s input will be uppercase. Structure your 
program per the below, wherein is_valid returns True if s meets all requirements 
and False if it does not. Assume that s will be a str. You’re welcome to 
implement additional functions for is_valid to call (e.g., one function per 
requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()

Hints
-----
Recall that a str comes with quite a few methods, per 
docs.python.org/3/library/stdtypes.html#string-methods.
Much like a list, a str is a “sequence” (of characters), which means it can be 
“sliced” into shorter strings with syntax like s[i:j]. For instance, if s is 
"CS50", then s[0:2] would be "CS".

Demo
----
$ python plates.py                                                              
Plate: HELLO                                                                    
Valid                                                                           
$ python plates.py                                                              
Plate: HELLO, WORLD                                                             
Invalid 
Plate: GOODBYE                                                                  
Invalid                                                                         
$ python plates.py                                                              
Plate: CS50                                                                     
Valid                                                                           
$ python plates.py                                                              
Plate: CS05                                                                     
Invalid                                                                         
$ python plates.py                                                              
Plate: 50                                                                       
Invalid                                                                         
$                                                                               

How to test
-----------
Here’s how to test your code manually:

Run your program with python plates.py. Type CS50 and press Enter. 
Your program should output:
Valid
Run your program with python plates.py. Type CS05 and press Enter. 
Your program should output:
Invalid
Run your program with python plates.py. Type CS50P and press Enter. 
Your program should output
Invalid
Run your program with python plates.py. Type PI3.14 and press Enter. 
Your program should output
Invalid
Run your program with python plates.py. Type H and press Enter. 
Your program should output
Invalid
Run your program with python plates.py. Type OUTATIME and press Enter. 
Your program should output
Invalid
"""


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    print("right lenght: ", is_right_lenght(plate))
    print("begin with 2 letters: ", is_begin_2letters(plate))
    print("the numbers is only at the end: ", is_numbers_end(plate))
    print("is the first number not a zero: ", is_first_number_not_zero(plate))
    print("è alfanumerica: ", is_alpha_or_number(plate))

    if (
        is_right_lenght(plate)
        and is_begin_2letters(plate)
        and is_numbers_end(plate)
        and is_first_number_not_zero(plate)
        and is_alpha_or_number(plate)
    ):
        return True


def is_right_lenght(s):
    # maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if len(s) > 1 and len(s) < 7:
        return True
    else:
        return False


def is_begin_2letters(s):
    # starts with 2 letters
    if s[0:2].isalpha():
        return True


def is_numbers_end(s):
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate;
    # AAA22A would not be acceptable.
    lenght_plate = len(s)
    number_digit_in_plate = 0

    for c in s:
        if c.isdigit():
            number_digit_in_plate = number_digit_in_plate + 1

    if (
        number_digit_in_plate == 0
        or s[len(s) - number_digit_in_plate : len(s)].isdigit()
    ):
        return True


def is_first_number_not_zero(s):
    # The first number used cannot be a ‘0’.”
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
    return True


def is_alpha_or_number(s):
    # “No periods, spaces, or punctuation marks are allowed.”
    if s.isalnum():
        return True


main()
