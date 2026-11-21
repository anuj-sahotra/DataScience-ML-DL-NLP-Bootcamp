# 1.Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero.

try:
    num = int(input("Number : "))

    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print("Zero")
except ValueError:
    print("Invalid Input")        
        