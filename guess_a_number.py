from guess_no_art import logo
print(logo)

print("Welcome to the number guessing game!")
print("Think a number between 1 and 100")
import random
numbers=list(range(1,101))

def easy_level():
    total_attempts = 10
    print(f"you have {total_attempts} attemts to guess a number.")
    guess_over = False
    while not guess_over:
    
        guess_number=int(input("make a guess : "))
        if guess_number > computer:
            print("Too high")
            print("guess again")
            
        elif guess_number < computer:
            print("Too low")
            print("guess again")
            
        else:
            guess_over = True
            print(f"You gor it! The number is {guess_number}")
        if guess_number != computer:
            total_attempts -= 1
            if total_attempts == 0:
                guess_over = True
                print("You've out of guesses.You lose!")
            else:
                print(f"you have {total_attempts} attemts to guess a number.")
            
def hard_level():
    total_attempts = 5
    print(f"you have {total_attempts} attemts to guess a number.")
    guess_over = False
    while not guess_over:
        guess_number=int(input("make a guess : "))
        if guess_number > computer:
            print("Too high")
            print("guess again")
            
        elif guess_number < computer:
            print("Too low")
            print("guess again")
            
        else:
            guess_over = True
            print(f"You gor it! The number is {guess_number}")
        if guess_number != computer:
            total_attempts -= 1
            if total_attempts == 0:
                guess_over = True
                print("You've out of guesses.You lose!")
            else:
                print(f"you have {total_attempts} attemts to guess a number.")
                

game_over = True
while game_over :
    computer_number = random.choices(numbers)
    computer = computer_number[0]
    level=input("choose a difficulty level. Type 'easy' or 'hard'  ")
    if level == 'easy':
        easy_level()
    else:
        hard_level()
    next_game=input("Want to play again,Type 'yes' or 'no' ")
    if next_game == 'yes':
        computer_number.clear()
        continue
    else:
        game_over = False
        print("Thank you for playing!")

            
