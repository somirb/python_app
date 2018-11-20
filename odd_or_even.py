number = input("Pick a number and I'll tell you if it's odd or even. ")

def odd_or_even():
    if int(number) % 2 == 0:
        return("Your number is even.")
    else:
        return("Your number is odd.")
print(odd_or_even())