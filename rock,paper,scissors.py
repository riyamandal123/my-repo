rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
computer=random.randint(0,2)
user=input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors :")
if user == '0':
    print(rock)
    if computer == 0:
        print(rock)
        print("IT'S A TIE!")
    elif computer == 1:
        print(paper)
        print("COMPUTER WINS!")
    else:
        print(scissors)
        print("YOU WIN!")
elif user == '1':
    print(paper)
    if computer == 0:
        print(rock)
        print("YOU WIN!")
    if computer == 1:
        print(paper)
        print("IT'S A TIE!")
    else:
        print(scissors)
        print("COMPUTER WINS!")
else:
    print(scissors)
    if computer == 0:
        print(rock)
        print("COMPUTER WINS!")
    elif computer == 1:
        print(paper)
        print("YOU WIN!")
    else:
        print(scissors)
        print("IT'S A TIE!")
