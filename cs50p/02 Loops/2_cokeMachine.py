"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only 
accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a 
coin, one at a time, each time informing the user of the amount due. Once the 
user has inputted at least 50 cents, output how many cents in change the user is 
owed. Assume that the user will only input integers, and ignore any integer that 
isn’t an accepted denomination.

Demo
----
Amount Due: 50                                                                  
Insert Coin: 25                                                                 
Amount Due: 25                                                                  
Insert Coin: 10                                                                 
Amount Due: 15                                                                  
Insert Coin: 10                                                                 
Amount Due: 5                                                                   
Insert Coin: 5                                                                  
Change Owed: 0                                                                  
$ 

"""

amount_due = 50
# print(tipe(amount_due))

while amount_due > 0:
    print("Amount due for a coke: ", amount_due)

    try:
        amount_in = int(input("Insert a coin (we accept 25, 10 and 5 cents coin): "))
    except ValueError:
        amount_in = 0

    if amount_in == 25 or amount_in == 10 or amount_in == 25:
        amount_due = amount_due - amount_in

print("Here is your coke")

if amount_due < 0:
    print("Your change is: ", -amount_due)
