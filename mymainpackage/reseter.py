def gameboardclear():
    p1.clear()
    p1value.clear()
    dealer.clear()
    dealervalue.clear()
    bets.clear()
    bets.append(100)
    betreturn.clear()
    for r in range(len(usedbox)):
        cut = usedbox[r].replace(usedbox[r][-1],'')
        if int(usedbox[r][-1]) == 1:
            deck1.append(cut)
        elif int(usedbox[r][-1]) == 2:
            deck2.append(cut)
        elif int(usedbox[r][-1]) == 3:
            deck3.append(cut)            
        elif int(usedbox[r][-1]) == 4:
            deck4.append(cut)         
        elif int(usedbox[r][-1]) == 5:
            deck5.append(cut)
        elif int(usedbox[r][-1]) == 6:
            deck6.append(cut) 

def resetgame():
    gameboardclear()
    reseter = str((input('would you like to play again y/n?'))).lower()
    if reseter == 'y':
        playerBal = playerAcct.__int__()
        print(playerBal)
        if playerBal < 100:
            print('call yo mama for some money you do not have enuff! Hang your head in shame and Start A new identity!')
            BLACKJACK()
        else:
            gamestart()
    elif reseter == 'n':
        print('See you later!')
    else:
        print('y or n dude!')
        resetgame()