import random

upper = int(input("Give Upper number:\n"))
lower = int(input("Give lower numbe:\n"))
guess_number = random.randint(lower, upper)
count = 0

while count < 7:
    print(f"You have only {7 - count} chances to guess number:")
    user_number = int(input(f"Choose a number from {upper} to {lower}:\n"))
    if user_number == guess_number:
        print("Congratz you guessed the right number :)")
        break
    if user_number != guess_number and count < 6:
        if user_number > guess_number:
            print(f"Sorry, {user_number} is bigger the number, try again.\n")
        else:
            print(f"Sorry, {user_number} is smaller the number, try again.\n")
    else:
        print(f"Right number was {guess_number}.\n")
    count += 1