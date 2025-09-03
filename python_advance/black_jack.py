""" Program to play a simple game of Black Jack """

import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Jacks, Queens, Kings are worth 10; Aces can be worth 11
    return random.choice(cards)


def calculate_score(hand):
    """Calculate the score of a hand"""
    score = sum(hand)
    # Adjust for Aces
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)  # Convert Ace from 11 to 1
        score = sum(hand)
    return score


def compare_scores(player_sore: int, computer_score: int) -> str:
    """Compare player and computer scores and return the result."""
    if player_sore > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif player_sore == computer_score:
        return "It's a draw!"
    elif player_sore == 21:
        return "Blackjack! You win!"
    elif computer_score == 21:
        return "Computer got Blackjack! You lose!"
    elif player_sore > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_blackjack():
    """Main function to play the game"""
    print("Welcome to the balck jack game!")

    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    game_over = False
    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        if player_score == 21 or computer_score == 21 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True
        while computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = calculate_score(computer_hand)
        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
        print(compare_scores(player_score, computer_score))
        if player_score == 21 or computer_score == 21 or player_score > 21:
            game_over = True
        if game_over:
            print("Game over! Thanks for playing!")
            break


if __name__ == "__main__":
    play_blackjack()
    while input("Do you want to play again? Type 'y' or 'n': ") == 'y':
        play_blackjack()
    print("Thanks for playing!")
# End of the Black Jack game code


