# Determine the ticket price based on age

age = int(input("Enter your age : "))
is_student = input("You are a student (Yes/No) : ").lower()

if age < 5:
    print("Free")
elif age <= 12:
    print("Ticket price is $10")
elif age <= 18:
    if is_student == 'yes':
        print("Ticket price is $15")
    else:
        print("Ticekt price is $20")
elif age <= 60:
    if is_student == 'yes':
        print("Ticket price is $25")
    else:
        print("Ticket price is $40")
else:
    print("Ticket price is $150")          