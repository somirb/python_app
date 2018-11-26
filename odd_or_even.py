number = input("Pick a number and I'll tell you if it's odd or even. ")

def odd_or_even():
    if int(number) % 4 == 0:
        return("Your number is a multiple of 4.")
    elif int(number) % 2 == 0:
        return("Your number is even.")
    else:
        return("Your number is odd.")
print(odd_or_even())

num = input("Pick another number. ")
check = input("Pick one more number, I promise. ")

def check_num():
    if int(num) % int(check) == 0:
        return("Your second number evenly divides into the first number.")
    else:
        return("Your second number does not evenly divide into the first number.")
print(check_num())