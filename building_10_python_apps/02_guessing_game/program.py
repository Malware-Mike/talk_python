import random

print('---------------------------------')
print('      GUESS THE NUMBER APP')
print('---------------------------------')

computer_number = random.randint(1,101)
print(computer_number)
user_guess = int(input("Guess a number between 0 and 100: "))

while True:
    if user_guess < computer_number:
        print('Sorry but {} is LOWER than the number'.format(user_guess))
        user_guess = int(input("Guess a number between 0 and 100: "))
    elif user_guess > computer_number:
        print("Sorry but {} is HIGHER than the number".format(user_guess))
        user_guess = int(input("Guess a number between 0 and 100: "))
    else:
        print("YES! You've got it. The number was {}".format(computer_number))
        break

