# Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.

total = 0
while True:
    num = float(input("Number : "))
    if num == 0:
        break
    total += num
print(f"Sum of all numbers = {total}")    