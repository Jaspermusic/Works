# Rock Paper Scissor
import random


def choice():
    a = input("Enter your choice: [R]ock [P]aper [S]cissor: ")
    if a == 'r' or a == 'R':
        b = "Rock"
    elif a == 'p' or a == 'P':
        b = "Paper"
    elif a == 's' or a == 'S':
        b = "Scissor"
    else:
        print("Wrong I/P")
        return choice()
    return b


def game(user_score, comp_score):
    user_value = choice()
    values = ["Rock", "Paper", "Scissor"]
    comp_value = random.choice(values)
    print("Computer Choice: ", comp_value)
    if comp_value == user_value:
        print("tie")
    elif (comp_value == "Paper" and user_value == "Scissor") or \
        (comp_value == "Rock" and user_value == "Paper") or \
            (comp_value == "Scissor" and user_value == "Rock"):
        print("User Wins")
        user_score = user_score+1
    elif (user_value == "Paper" and comp_value == "Scissor") or \
         (user_value == "Rock" and comp_value == "Paper") or \
         (user_value == "Scissor" and comp_value == "Rock"):
        print("Computer Wins")
        comp_score = comp_score+1
    else:
        pass
    return user_score, comp_score


user_score = 0
comp_score = 0
round = 1

while True:
    print("Round No: ", round)
    round = round+1
    user_score, comp_score = game(user_score, comp_score)
    print("User score: ", user_score)
    print("Computer score: ", comp_score)
    print("\n")
    yn = input("Press any key to continue and [x] for exit: ")
    print("\n")
    if yn == 'x' or yn == "X":
        print("Thanks for playing")
        break
    else:
        continue
