"""
Suppose that you’re in a country where it’s customary to eat breakfast 
between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 
18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell 
you what to eat when?

In meal.py, implement a program that prompts the user for a time and 
outputs whether it’s breakfast time, lunch time, or dinner time. If it’s 
not time for a meal, don’t output anything at all. Assume that the user’s 
input will be formatted in 24-hour time as #:## or ##:##. And assume that 
each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 
7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be 
called by main) that converts time, a str in 24-hour format, to the corresponding 
number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours 
and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()


Hints
-----
- Recall that a str comes with quite a few methods, per 
docs.python.org/3/library/stdtypes.html#string-methods, 
including split, which separates a str into a sequence of values, all of which 
can be assigned to variables at once. For instance, if time is a str like "7:30", 
then hours, minutes = time.split(":") will assign "7" to hours and "30" to 
minutes.
- Keep in mind that there are 60 minutes in 1 hour.

Demo
----
$ python meal.py                                                                
What time is it? 7:30                                                           
breakfast time                                                                  
$ python meal.py                                                                
What time is it? 8:01                                                           
$ python meal.py                                                                
What time is it? 18:01                                                          
dinner time                                                                     
$ python meal.py                                                                
What time is it? 18:59                                                          
dinner time                                                                     
$                                                                              

Challenge
---------
If up for a challenge, optionally add support for 12-hour times, allowing the 
user to input times in these formats too:

#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.

How to test
-----------
Here’s how to test your code manually:

Run your program with python meal.py. Type 7:00 and press Enter. Your program should output:
breakfast time   
Run your program with python meal.py. Type 7:30 and press Enter. Your program should output:
breakfast time
Run your program with python meal.py. Type 12:42 and press Enter. Your program should output
lunch time
Run your program with python meal.py. Type 18:32 and press Enter. Your program should output
dinner time
Run your program with python meal.py. Type 11:11 and press Enter. Your program should output nothing.

"""


def main():
    # Ask for the time
    time_str = input("What's the time? (hh:mm) ").strip()

    # Check the time
    ore_str, minuti_str = time_str.split(":")

    if isTimeString(ore_str, minuti_str):
        #
        # Say, according to the time, the followings:
        #    7:00 - 8:00 (included) -> Print Breakfast time
        #   12:00 - 13:00 (included) -> Print Lunch time
        #   18:00 - 19:00 (included) -> Print Dimner time
        #   Other -> Noting

        ore = float(ore_str)
        minuti = float(minuti_str)

        if ore == 7 or (ore == 8 and minuti == 0):
            print("It's time for breakfast")
        elif ore == 12 or (ore == 13 and minuti == 0):
            print("It's time for lunch")
        elif ore == 18 or (ore == 19 and minuti == 0):
            print("It's time for dinner")

    else:
        print("inserisci un orario valito nel formato hh:mm.")


def isTimeString(h, min):
    if h.isdigit() and min.isdigit():
        ore = float(h)
        minuti = float(min)
    else:
        return False

    if ore > 24 or minuti > 59:
        return False

    return True


if __name__ == "__main__":
    main()
