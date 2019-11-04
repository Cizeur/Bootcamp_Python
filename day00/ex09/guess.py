import random
import os

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck""")
random.seed(os.urandom(6000))
attempt = 0
rand_nb = random.randint(1, 99)
while (1):
    attempt += 1
    print("What's your guess between 1 and 99?")
    inval = input(">> ")
    if inval == "exit":
        print("Goodbye !")
        break
    try:
        inval = int(inval)
    except ValueError:
        print("That's not a number.")
        continue
    if inval == rand_nb:
        if inval == 42:
            print("The answer to the ultimate question of life,\
the universe and everything is 42")
        print("Congratulations, you've got it!")
        print("You won in {:d} attempts!".format(attempt))
        break
    elif inval < rand_nb:
        print("Too low!")
    elif inval > rand_nb:
        print("Too high!")
