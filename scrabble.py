letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
#print(list(letter_to_points.items()))

#refactor to add in lists above
letter_to_points[" "] = 0
print(list(letter_to_points.items()))

def score_word(word):
  #get some input for a word
  word = input("What is your word? ")
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

#test score_word function
brownie_points = score_word("brownie")
print(brownie_points)