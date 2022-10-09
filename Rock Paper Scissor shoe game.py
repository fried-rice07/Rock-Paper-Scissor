import random
player1=0
player2=0
options=["rock","paper","scissors"]
score=0
computer =0
while True:
    users=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if users=="q":
        break
    if users not in options:
        continue
    random_num= random.randint(0,2)
    #rock 0 ; paper 1; sciccors 2;
    computer_pick=options[random_num]
    print("Player 2 Picked",computer_pick + ".")
    if users == "rock" and computer_pick == "scissors":
        print("Player 1 Win!")
        score+=1
    elif users== "paper" and computer_pick == "rock":
        print("Player 1 Win!")
        score+=1
    elif users == "scissor" and computer_pick == "paper":
        print("Player 1 Win!")
        score+=1
    else:
        print("Player 2 Win!")
        computer+=1
print("Player 1 Won ",score, "times.")
print("Player 2 Won", computer,"times.")






print("GoodBye!")

