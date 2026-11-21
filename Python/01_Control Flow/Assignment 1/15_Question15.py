# **Question 19:** Write a Python program to check if a string is a palindrome.
txt = input("Text : ").lower()

if txt == txt[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")    
    
