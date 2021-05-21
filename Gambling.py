from random import randint

#set up comp
t = ["Bau", "Cua", "Ca", "Tom", "Ga", "Huou"]
comp = t[randint(0, 5)]

#set up player
player = False
cash = 100

#let's play
while player == False:
    bet = int(input ("How much you want to bet? > "))
    player = input ("Which one will you take? Bau, Cua, Ca, Tom, Ga, Huou? > ")
    if bet > 0 and bet <= cash:
        if player == comp:
            print ("Congrats! You won")
            cash += bet*3
        else:
            print ("You lose!")
            cash -= bet
    else:
        print ("Check your money first!")
    print ("Your balance:", cash)

    #lam giau ko kho
    player = False
    comp = t[randint(0,5)]

