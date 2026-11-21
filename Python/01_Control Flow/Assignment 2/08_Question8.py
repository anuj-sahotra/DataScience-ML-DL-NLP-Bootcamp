# Reverse a number 

def reverse_num(num):
    result = 0
    while num > 0:
        digit = num % 10
        result = (result * 10) + digit
        num //= 10
    return result

try:
    num = int(input("Number : "))    
    print(f"Reverse of {num} = {reverse_num(num)}")
except ValueError:
    print("Invalid Input")    
        