import random


# Initialized variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
overall_score = []

# functions


def check_double_aces(hand):
    if hand == [11, 11]:
        hand[0] = 1
        hand[1] = 1

    return hand


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
        bj_game()


def bj_game():
    stay_hit_correct = False
    player_score = 0
    dealer_score = 0
    player_hand = []
    dealer_hand = []

    for run in range(0, 2):
        player_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))

    player_hand = check_double_aces(player_hand)
    dealer_hand = check_double_aces(dealer_hand)

    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    print(f"dealer hand: {dealer_hand} score: {dealer_score}")

    # players hand section

    while sum(player_hand) <= 21:
        while stay_hit_correct != True:
            print(f"Player hand: {player_hand} score: {player_score}")
            stay_hit = input("Would you like to stay or hit? ").lower()
            if stay_hit == "stay" or stay_hit == "hit":
                stay_hit_correct = True
            else:
                print("invalid input. only input stay or hit.")
        if stay_hit == "hit":
            player_hand.append(random.choice(cards))
            stay_hit_correct = False
            if sum(player_hand) > 21:
                for i in range(len(player_hand)):
                    if player_hand[i] == 11:
                        player_hand[i] = 1
            player_score = sum(player_hand)
        elif stay_hit == "stay":
            break

    print(f"final player's hand: {player_hand} score: {player_score}")
    print("Dealer's turn")

    # dealers section - automated

    while sum(dealer_hand) <= 21:
        if dealer_score < player_score


# Timeline
play()
