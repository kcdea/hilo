import random

secret_num = random.randint(1, 100)
print("Welcome to the HI-LO game!!")
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == secret_num:
        print("You got it! The secret number was {}!".format(secret_num))
        break
    if guess > secret_num:
        print("Too high")
    if guess < secret_num:
        print("Too low")
