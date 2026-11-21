# **Question 7:** Write a Python program to swap the values of two variables.

num1 = input("Number 1 : ")
num2 = input("Number 2 : ")

print(f"Before Swap : \n Number 1 : {num1} \n Number 2 : {num2}")

num1, num2 = num2, num1

print(f"After Swap : \n Number 1 : {num1} \n Number 2 : {num2}")