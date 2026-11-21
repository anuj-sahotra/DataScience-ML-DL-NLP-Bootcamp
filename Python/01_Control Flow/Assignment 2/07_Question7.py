# Write a program that calculates the sum of the digits of a number input by the user using a while loop.

def sum_digits(num):
    result = 0
    while num > 0:
        digit = num % 10
        result += digit
        num //= 10
    return result
num = int(input("Number : "))
print(f"Sum of digits of {num} = {sum_digits(num)}")    