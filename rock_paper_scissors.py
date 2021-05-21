from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
p_score = 0
c_score = 0

#here is the game
while player == False:
    #case of Tie
    player = input("Rock, Paper, or Scissors?")
    if player == computer:
        print("That's a Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! You got covered by", computer)
            c_score += 1
        else:
            print("You won! Your", player, "smashes", computer)
            p_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! You got cut by", computer)
            c_score += 1
        else:
            print("You won! Your ", player, "covered", computer)
            p_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! You got smashed by", computer)
            c_score += 1
        else:
            print("You won! Your",player, "cut", computer)
            p_score += 1
    
    else:
        print("That's not a valid option! Please choose one three available options.")
    print("You:", p_score, "Computer:", c_score)
    #start the game over
    #set the player to False since it's True after a run
    player = False
    computer = t[randint(0,2)]
