#   **Question 15:** Write a Python program to check if a number is even or odd.

num = int(input("Enter a whole number : "))

if num >= 0:
    if num % 2 == 0:
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number.")
        
else:
    print("Enter a positive number.")                
        