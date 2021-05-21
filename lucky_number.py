from random import randrange

#set player to False
player = False
p_cash = 100


#set up the machine player

pc = randrange(1,6)

#game start
while player == False:
    if p_cash > 0:
        ask = input("Shall we start? Yes or No ")
        if ask == "Yes":
            player = randrange(1, 6)
            if player == pc:
                print("It's a tie!")
            elif player > pc:
                print ("You won", player, ">", pc)
                p_cash += 10
            else:
                print ("You lose!", player, "<", pc)
                p_cash -= 10
        else:
            print("Ok, come again.")
    else:
        print ("You have run out of cash!")

    print("Remaining:",p_cash)

    #keep the game going
    player = False
    pc = randrange(1,6)
