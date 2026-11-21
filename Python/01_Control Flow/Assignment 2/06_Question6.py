# Write a program that calculates the factorial of a number input by the user using a while loop.

num = int(input("Number : "))

if num >= 0:
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"Factorial of {num} = {factorial}")
        
else:
    print("Enter a Positive number.")        
        