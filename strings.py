#slice and concatonate end of strings
first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)

#slice and concatonate beginning of strings
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account = first_name[0:3] + last_name[0:3]
  return account
new_account = account_generator("Julie", "Blevins")

#easier string slicing for the end of strings
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]

#iterate through a string and count the letters of the string
def gen_length(i):
  counter = 0
  for letter in i:
    counter += 1

#return a list with all of the letters two string have in common
def common_letters(string_one, string_two):
  lst = []
  for letter in string_one:
    if letter in string_two and letter not in lst:
      lst.append(letter)
  return lst