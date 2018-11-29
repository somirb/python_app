import random
rand_num = random.randint(1, 9)
#print(rand_num)
user_guess = int(input("Guess a number between 1 and 9. \n"))

def guessing_game():
    if user_guess == rand_num:
        print("Amazing! You guessed it!")
    elif user_guess > rand_num:
        print("Too high!")
    elif user_guess < rand_num:
        print("Too low!")
guessing_game()