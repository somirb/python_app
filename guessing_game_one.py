import random
rand_num = random.randint(1, 9)
#print(rand_num)
count = 0
user_guess = 0

while user_guess != rand_num and user_guess != 'exit':
    user_guess = input('Guess a number between 1 and 9. Type "exit" to end at any time. \n')
    count += 1
    if user_guess == 'exit':
        break
    user_guess = int(user_guess)
    if user_guess > rand_num:
         print("Too high!")
    elif user_guess < rand_num:
        print("Too low!")
    else:
        user_guess == rand_num
        print("Amazing! You guessed it! It only took you " + str(count) + " tries.")

    