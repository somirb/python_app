def check_primality():
    user_num = int(input("Enter a number and I'll check if it's prime. \n"))
    if user_num % 2 != 0:
        print("Your number is not prime.")
    else:
        print("Your number is prime!")
check_primality()