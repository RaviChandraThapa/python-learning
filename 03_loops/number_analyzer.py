# Empty list to store user inputs from loop.
number_inputs = []

# For loops to collect numbers repeatedly 
for i in range(5):
    user_num = float(input("Please Enter a number: "))
    number_inputs.append(user_num)



# Use a loop to find smallest number
smallest_number = number_inputs[0]
for i in number_inputs:    
    if i < smallest_number:
        smallest_number = i



# Use a loop to find the largest number
largest_number = number_inputs[0]
for i in number_inputs:
    if i > largest_number:
        largest_number = i



# Using For loops to add all the numbers and find out Average
total = 0
count_numbers = 0
for i in number_inputs:
    total += i
    count_numbers += 1

average_of_number_list = total / count_numbers

# Separate the numbers into odd and even lists
odd_numbers = []
even_numbers = []

for i in number_inputs:
    # Only classify if the inputs are whole numbers
    if i.is_integer():
        if int(i) % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

# Formatting Output
print("=" * 30)
print("Analyzed Numbers")
print("=" * 30)
print("\n")
print(f"Numbers Provided: {number_inputs}")
print(f"Smallest Number: {smallest_number}")
print(f"Largest Number: {largest_number}")
print(f"Average: {average_of_number_list}")
print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")
print("\n")
print("=" * 30)