from higher_lower_game_data import data
from higher_lower_art import logo,vs
import random

print(logo)

game_over=False
current_score = 0
while not game_over:
    first_person = random.choices(data)
    second_person = random.choices(data)
    
    for items in first_person:
        name=items['name']
        followers_A=items['follower_count']
        description=items['description']
        country=items['country']
        print(f"Compare A: {name}, a {description}, from {country}")

    print(vs)
       
    for item in second_person:
        name=item['name']
        followers_B=item['follower_count']
        description=item['description']
        country=item['country']
        print(f"Compare B: {name}, a {description}, from {country}")

  
    user_guess=input("Who has more followers? Type 'A' or 'B' : ")
    if user_guess == 'A':
        if followers_A > followers_B:
            current_score += 1
            print(f"You got it! Current score : {current_score}.")
    
        else:
            final_score = current_score
            print(f"Sorry, that's wrong. Final score: { final_score}")
            game_over = True
    elif user_guess == 'B':
        if followers_B > followers_A:
            current_score += 1
            print(f"You got it! Current score : {current_score}.")

        else:
            final_score = current_score
            print(f"Sorry, that's wrong. Final score: { final_score}")
            game_over = True
  
   
      
            
        
