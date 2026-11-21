# **Question 3:** Write a Python program to check if a number is positive, negative, or zero.

num = float(input("Number : "))

if num > 0:
    print(f"{num} is Positive.")
elif num < 0:
    print(f"{num} is Negative.")
else:    
    print("Zero")