#password generator

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = ["@", "+", "-", "*", "?", "!", ".", "_", "$"]
def generate_password(letters, numbers, characters, password_length):
    password_characters = []
    final_password = ""
    for i in range(password_length):
        password_characters.append(random.randint(1, 6))

    for i in range(len(password_characters)):
        if password_characters[i] == 1 or password_characters[i] == 2 or password_characters[i] == 3 or password_characters[i] == 4:
            final_password += random.choice(letters)
        if password_characters[i] == 5:
            final_password += str(random.choice(numbers))
        if password_characters[i] == 6:
            final_password += random.choice(characters)

    return final_password

if __name__ == "__main__":
    while True:
        print(generate_password(letters, numbers, characters, int(input("password lenght: "))))



