import random


# Initialized variables
deck = []
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0
stay_hit_correct = False
stay_hit = ""
overall_score = []

# functions


def play():
    # variables
    play_correct = False

    while play_correct != True:
        play = input("Would you like to play? yes or no: ").lower()
        if play == "yes" or play == "no":
            play_correct = True
        else:
            print("invalid input. Only input yes or no.")
    if play == "no":
        print("Goodbye.")
    elif play == "yes":
        print("time to play the game.")
        # bj_game()

# functions


play()
