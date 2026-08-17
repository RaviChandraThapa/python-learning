# Prompt for user input.
age = int(input("Please enter your age: "))

#1. For impossible ages
if age <= 0:
    print("Error: Age cannot be negative or zero! Please run the program again.")

#2. Check for realistic upper boundaries
elif age > 120:
    print("You are a legendary senior. That's a incredible age!")

#3. Standard Age group
elif age <= 12:
    print("You are a child.")
    print("Enjoy your playtime!")
elif age < 18:
    print("You are a teenager.")
    print("Make the most of your school days!")
elif age < 65:
    print("You are an adult.")
    print("You are eligible to create a primary profile in our platform.")
else:
    print("You are a senior.")
    print("We hope you are enjoying your retirement!")