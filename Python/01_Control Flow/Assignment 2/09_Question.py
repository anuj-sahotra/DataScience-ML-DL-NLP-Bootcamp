# Write a program that checks if a number input by the user is a prime number using a for loop.

def is_prime(num):
    if num < 2:
        return False
        
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

num = int((input("Number : ")))

if is_prime(num): 
    print(f"{num} is a Prime No.")
else:
    print(f"{num} is Non Prime.")    