letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_to_points = {key:value for key, value in zip(letters, points)}
#print(list(letter_to_points.items()))

#ask for a word
word = input("What is your word? ")

#calculate score of given word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter.upper(), 0)
    return point_total
print("Your point total for this word was " + str(score_word(word)) + ".")

#test score_word function, should return 15
#brownie_points = score_word("brownie")
#print(brownie_points)

#words played by each player
player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}

#update total points for each player
def update_point_totals():
    player_to_points = {}
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
            player_to_points[player] = player_points
    return player_to_points
print(update_point_totals())



