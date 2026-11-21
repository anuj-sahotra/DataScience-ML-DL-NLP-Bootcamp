# Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.

num = int(input("Number : "))

if num > 0:
    if num % 2 == 0:
        print(f"{num} ia positive and even.")
    else:
        print(f"{num} is positive and odd.")
elif num < 0:
    print(f"{num} is negative.")
    
else:
    print("Zero")            