def greet_user(name):
   return f"Hello {name.capitalize()}!" # Returns the string to the caller

# Call the function, capture the returned string, and then print it
greeting = greet_user("ravi")
print(greeting)

greet_user("ravi")

def calculate_tax(price, tax):
    total_tax = price * tax / 100
    total_price = price + total_tax
    return total_tax, total_price

total_tax, total_price = calculate_tax(5000, 15)
print(f"Total price of the product is Rs.{total_price:.2f} including tax Rs.{total_tax:.2f}.")

def is_even(number):
   return number % 2 == 0 # Since number % 2 == 0 already returns True or False no need to do if else.


print(is_even(5))
print(is_even(4))

def calculate_average(number_list):
    total = 0
    count = 0    
    for number in number_list:
        total += number
        count += 1
    average = total / count
    return average
list_of_numbers = [4, 3, 10, 93, 58, 5]
average = calculate_average(list_of_numbers)
print(f"Average: {average:.2f}")

def find_max(number_list):
    highest_num = number_list[0]
    for number in number_list:
        if number > highest_num:
            highest_num = number
    return highest_num
highest_number = find_max(list_of_numbers)
print(highest_number)

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
fahrenheit = convert_celsius_to_fahrenheit(37)
print(fahrenheit)

def count_vowels(text):
    total_vowels = 0
    for letter in text:
        # Lowercase the letter, then check if it exists in our vowel list
        if letter.lower() in "aeiou":
            total_vowels += 1
    return total_vowels

total_vowels = count_vowels("This is example sentence. From this sentence vowels will be counted.")
print(f"Number of vowels: {total_vowels}")

def is_prime(number):
    if number < 2:
        return False
    for num in range(2, int((number**0.5) + 1)):
        if number % num == 0:
            return False
        
    return True

prime_check = is_prime(47)
print(prime_check)

def reverse_string(text):
    reversed_string = text[::-1]
    return reversed_string

print(reverse_string("Hello"))

def filter_short_words(words_list, max_len):
    short_words_list = []
    for word in words_list:
        if len(word) < max_len:
            short_words_list.append(word)

    return short_words_list

words_list = ["apple", "aeroplane", "shool", "friend", "upset", "entertainment", "cat", "dog", "pen"]
list_short_words = filter_short_words(words_list, 5)
print(list_short_words)


