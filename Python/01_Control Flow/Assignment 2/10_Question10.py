# Write a program that prints the first n Fibonacci numbers, where n is input by the user.

def fibonacci(num):
    a, b = 0, 1
    count = 0
    while count < num:
        print(a)
        a, b = b, a + b
        count += 1
        
num = int(input("Enter range : "))
if num < 0:
    print("Invalid Input.")
else:
    print("Fibonacci Series")
    fibonacci(num)
    