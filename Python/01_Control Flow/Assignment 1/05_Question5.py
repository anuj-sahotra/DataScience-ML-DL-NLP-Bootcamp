# **Question 5:** Write a Python program to calculate the factorial of a number.

def factorial(num):
    if num == 0:
        return 1
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

try:
    num = int(input("Enter a number : "))
    if num > 0:
        print(f"Factorial of {num} : {factorial(num)}")    
    else:
        print("Enter +ve integer")
        
except ValueError:
    print("Invalid Input")        