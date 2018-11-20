letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_to_points = {key:value for key, value in zip(letters, points)}
#words played by each player
player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}
#print(list(letter_to_points.items()))



#calculate score of given word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter.upper(), 0)
    return point_total

#test score_word function, should return 15
#brownie_points = score_word("brownie")
#print(brownie_points)

player_to_points = {}
#update total points for each player
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
            player_to_points[player] = player_points
    return player_to_points

update_point_totals()
#print(player_to_points)

# a function that would take in a player and a word, and add that word to the list of words they've played
def play_word(player, word):
    player_to_words[player].append(word)
    update_point_totals()

play_word("player1", "test")
print(player_to_words)
print(player_to_points)



