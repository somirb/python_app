user_name = input("What is your name? ")
current_age = int(input("What is your current age? "))

def years_until():
    try:
        if current_age >= 0 and current_age <= 99:
            year = (100 - current_age) + 2018
            return("Hi " + user_name + ", you will turn 100 years old in " + str(year))
        elif current_age >= 100:
            return("You're already 100!")
        elif current_age < 0:
            return("That's not funny.")
    except ValueError:
        return("Oops, that's not a valid entry.")
print(years_until())