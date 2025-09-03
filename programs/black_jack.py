"""Module to automate black jack"""
import random

# Python program that simulates a simple game of Blackjack between a player and the dealer.

blackjack_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                   11]  # Jacks, Queens, Kings are worth 10; Aces can be worth 11


def get_cards():
    """Function to select the cards"""
    return random.choice(blackjack_cards)


def calculate_score(cards: list[int]):
    """Function to calculate the total score"""
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)  # Convert Ace from 11 to 1
        score = sum(cards)
    return score


def compare_score(player_score: int, dealer_score: int):
    """Function to decide who wins"""
    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "dealer went over. You win!"
    elif player_score == 21 and dealer_score == 21:
        return "Match draw"
    elif player_score == 21:
        return "Blackjack ! You win!"
    elif dealer_score == 21:
        return "Computer got Blackjack! You lose!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"


def play_blackjack():
    """Function to play blackjack"""
    player_cards = [get_cards(), get_cards()]
    dealer_cards = [get_cards(), get_cards()]
    player_score = calculate_score(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    dealer_score = calculate_score(dealer_cards)

    hit_or_stand = input("Type 'y' to get another card, type 'n' to hit")
    if hit_or_stand == "n":
        print(compare_score(player_score, dealer_score))
    elif hit_or_stand == "y":
        player_cards.append(get_cards())
        player_score =calculate_score(player_cards)
        while dealer_score < 17:
            dealer_cards.append(get_cards())
            dealer_score = calculate_score(dealer_cards)
        print(f"Your final cards: {player_cards}, final score: {player_score}")
        print(f"dealer final cards: {dealer_cards}, final score: {dealer_score}")
        print(compare_score(player_score, dealer_score))
    else:
        print("Entered a choice")

play_blackjack()