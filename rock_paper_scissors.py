#ask for users moves
player_1_move = input("Player 1's move: Rock, paper, or scissors? ").lower()
player_2_move = input("Player 2's move: Rock, paper, or scissors? ").lower()

def rock_paper_scissors():
    #while player_1_move == player_2_move:
        #rock_paper_scissors()
    if player_1_move == "rock" and player_2_move == "scissors":
        print("Player 1 wins.")
    elif player_1_move == "scissors" and player_2_move == "paper":
        print("Player 1 wins.")
    elif player_1_move == "paper" and player_2_move == "rock":
        print("Player 1 wins.")
    elif player_2_move == "rock" and player_1_move == "scissors":
        print("Player 2 wins.")
    elif player_2_move == "scissors" and player_1_move == "paper":
        print("Player 2 wins.")
    elif player_2_move == "paper" and player_1_move == "rock":
        print("Player 2 wins.")
rock_paper_scissors()