import random
import string
import datetime

all_letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation
  

def password_generators(length, letters = all_letters, digit = digits, character = special_characters):
    num = input("Include numbers? (y/n): ").lower()
    special_character = input("Include special characters? (y/n): ").lower()

    generated_password =[]
    character_pool = letters

    if num == "y":
        generated_password.append(random.choice(digit))
        character_pool += digit
        length -= 1

    if special_character == "y":
        generated_password.append(random.choice(character))
        character_pool += character
        length -= 1

    remaining_chars = random.choices(character_pool, k=length)
    generated_password.extend(remaining_chars)

    
    random.shuffle(generated_password)
    return "".join(generated_password)

password_length = 0

while True:
    try:
        password_length = int(input("How long password do you want?\nNote: Password must have atleast 8 character.: "))
        if password_length >= 8:
            break
        else:
            print("Please input password length 8 or more.")    
    except ValueError:
        print("Please enter number for the password length")

final_password = password_generators(password_length)
formated_time = datetime.datetime.now().strftime("%Y-%m-%d at %H:%M")
print(f"Your password: {final_password}")
print(f"Password Generated on {formated_time}")