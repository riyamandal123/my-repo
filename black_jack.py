import random

user_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    user_cards.extend(random.choices(cards, k=2))
    computer_cards.extend(random.choices(cards, k=2))

def calculate_score():
    user_score = sum(user_cards)
    #only the first card of the computer will be displayed.
    computer_score = computer_cards[0]
    
    print(f"user: {user_cards}")
    print(f"user score: {user_score}")
    print(f"computer: {computer_cards[0]}")
    
    #check for blackjack.
    game_over = False
    while not game_over:
        #Blackjack is an Ace(with a value of 11) and a 10-value card (King/Queen/Jack).
        if user_score == 21 and len(user_cards) == 2:
            return 0

        if user_score > 21 and 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            next_card = input("Do you want to get another card? Type 'yes' or 'no': ")
            if next_card == 'yes':
                user_cards.append(random.choice(cards))
                user_score = sum(user_cards)
                print(f"user: {user_cards}")
                print("user final score:", user_score)
            elif next_card == 'no':
                game_over = True

    compare(user_score, computer_score)
#compare the scores of user and the computer.
def compare(user_score, computer_score):
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
        print(f"computer final score: {computer_score}")

    if user_score > 21 and computer_score > 21:
        print("You went over. You lose.")
    elif user_score > computer_score:
        print("You win!")
    elif user_score == computer_score:
        print("It's a draw.")
    elif computer_score == 0:
        print("You lose. Opponent has Blackjack.")
    elif user_score == 0:
        print("You win with a Blackjack!")
    else:
        print("computer wins.")

deal_cards()
calculate_score()

#to play the game once again.
play_again = True
while play_again:
    next_game=input("Type 'yes' to play again else type 'no'  ")
    if next_game == 'yes':
        user_cards.clear()
        computer_cards.clear()
        deal_cards()
        calculate_score()
    else:
        play_again = False









