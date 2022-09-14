import random
import os


# Initialized variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hit_or_stay = ["hit", "stay"]
overall_score = [0, 0]

# functions


def clear():

    os.system("clear")


def final_score(player_hand, player_score, dealer_hand, dealer_score, overall_score):
    final_choice_correct = False
    print(f"Final player hand: {player_hand} score: {player_score}")
    print(f"Final dealer hand: {dealer_hand} score: {dealer_score}")

    if player_score > 21:
        print("bust! You went over 21, dealer wins")
        overall_score[1] = overall_score[1] + 1
        # exit()
    elif dealer_score > 21:
        print("Birds the word! Dealer went bust! You Win")
        overall_score[0] = overall_score[0] + 1
    else:
        print("Wowzers, Oh My! It's a tie!")

    while final_choice_correct != True:
        again = input("Would you like to play again? yes or no: ")
        if again == "yes" or "no":
            final_choice_correct = True
        else:
            print("invalid input. only input yes or no.")
    if again == "yes":
        clear()
        final_choice_correct = False
        bj_game()
    else:
        print(
            f"Goodbye. Final score was player: {overall_score[0]} dealer: {overall_score[1]}")
        exit()


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
    print(f"dealer hand: {dealer_hand[0]}, X score: X")

    # players hand section

    while player_score <= 21:
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

    if player_score > 21:
        final_score(player_hand, player_score, dealer_hand,
                    dealer_score, overall_score)
    print("Dealer's turn")

    # dealers section - automated

    while dealer_score <= 21:
        print(f"dealer hand: {dealer_hand[0]}, X score: X")
        if dealer_score < player_score:
            dealer_hand.append(random.choice(cards))
            if sum(dealer_hand) > 21:
                for i in range(len(dealer_hand)):
                    if dealer_hand[i] == 11:
                        dealer_hand[i] = 1
            dealer_score = sum(dealer_hand)
        elif dealer_score > player_score:
            break
        elif dealer_score == player_score and dealer_score < 18:
            dealer_choice = random.choice(hit_or_stay)
            if dealer_choice == "hit":
                dealer_hand.append(random.choice(cards))
                if sum(dealer_hand) > 21:
                    for i in range(len(dealer_hand)):
                        if dealer_hand[i] == 11:
                            dealer_hand[i] = 1
                dealer_score = sum(dealer_hand)
            else:
                break
        else:
            break

    final_score(player_hand, player_score, dealer_hand,
                dealer_score, overall_score)


# Timeline
play()
