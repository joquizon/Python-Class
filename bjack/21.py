def BLACKJACK():
    from bjmod import Account
    from IPython.display import clear_output
    from mymainpackage import decks
    ##########################################################

    playerName = input('enter your name please:')
    playerAcct = Account(playerName,1000)
    playerBal = playerAcct.__int__()
    p1=[]
    p1value=[]
    dealer=[]
    dealervalue=[]
    addbets=[0]
    bets=[100]
    betreturn=[]
    usedbox = []

    def gameboardclear():
        p1.clear()
        p1value.clear()
        dealer.clear()
        dealervalue.clear()
        bets.clear()
        addbets.clear()
        bets.append(100)
        addbets.append(0)
        betreturn.clear()
        for r in range(len(usedbox)):
            cut = usedbox[r][-1]
            if cut == 'G':
                decks.deckG.append(usedbox[r])
            elif cut == 'B':
                decks.deckB.append(usedbox[r])
            elif cut == 'C':
                decks.deckC.append(usedbox[r])            
            elif cut == 'D':
                decks.deckD.append(usedbox[r])         
            elif cut == 'E':
                decks.deckE.append(usedbox[r])
            elif cut == 'F':
                decks.deckF.append(usedbox[r])
        usedbox.clear()

    def resetgame():
        clear_output()
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


    def staycheck():
        if sum(dealervalue) == 21:
            print('House Wins')
            resetgame()
        elif sum(dealervalue) >21:
            print('XXXBust!XXX Player wins')
            print(bets)
            print(addbets)
            if sum(addbets) == 0:
                playerAcct.dep(sum(bets))
            elif sum(addbets)>0:
                playerAcct.dep(((sum(bets)*2)-200)+(sum(addbets)*2))
            resetgame()
        elif sum(p1value) > sum(dealervalue):
            print(f'{playerName} Wins!')
            print(bets)
            print(addbets)
            if sum(addbets) == 0:
                playerAcct.dep(sum(bets))
            elif sum(addbets)>0:
                playerAcct.dep(((sum(bets)*2)-200)+(sum(addbets)*2))
            resetgame()
        elif sum(p1value) < sum(dealervalue):
            print('House Wins')
            resetgame()
        elif sum(p1value) == sum(dealervalue):
            print("push!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            playerAcct.dep(sum(betreturn))
            resetgame()

    def dealerLOGIC():
        if sum(dealervalue) == 20:
            staycheck()
        elif sum(dealervalue)>sum(p1value):
            staycheck()
        elif sum(dealervalue)<sum(p1value):
            Dcarddeal()
        elif sum(dealervalue) == sum(p1value):
            staycheck()

    def wincheck():
        if sum(p1value) == 21:
            print(f'{playerName} Wins!')
            playerAcct.dep(sum(bets)+(sum(bets)*1.5))
            resetgame()
        elif sum(p1value) >21:
            print('XXXBust!XXX House Wins')
            resetgame()
        else:
            PlayerHitStay()



    def p1stay():
        p1.append('stay')
        print(f'You have {p1}')


    def PlayerHitStay():
        playerBal = playerAcct.__int__()
        try:
            hitstay = int(input("type 1 for hit or 2 for stay"))
            if hitstay == 1:
                carddeal()
            elif hitstay ==2:
                while True:
                    try:
                        betmore = int(input("type additional bet amt"))
                        if betmore > 0 and betmore < playerBal:
                            addbets.append(betmore)
                            betreturn.append(betmore)
                            newbet = sum(bets)+sum(addbets)-100
                            betstay = sum(bets) - 100
                            playerAcct.withd(betmore)
                            print(f'You have now placed a ${newbet} bet')
                            p1stay()
                            Dcarddeal()
                            break
                        elif betmore == 0:
                            betstay = sum(bets) - 100
                            p1stay()
                            print(f'Your bet remains at ${betstay}.')
                            Dcarddeal()
                            break
                        else:
                            print('error bet range')
                    except ValueError:
                        print("Noinput is not a number. It's a string")
            elif hitstay>2 or hitstay<1:
                PlayerHitStay()
            else:
                betstay = sum(bets) - 100
                p1stay()
                print(f'Your bet remains at ${betstay}.')
                Dcarddeal()
        except ValueError:
            print("Noinput is not a number. It's a string")
            PlayerHitStay()

    def carddeal():
        clear_output()
        import random
        decknum = random.randint(1,6)
        if decknum == 1:
            deck = decks.deckG
        elif decknum == 2:
            deck = decks.deckB
        elif decknum == 3:
            deck = decks.deckC
        elif decknum == 4:
            deck = decks.deckD
        elif decknum == 5:
            deck = decks.deckE
        elif decknum == 6:
            deck = decks.deckF
        pick = random.randint(0,len(deck)-1)
        # print(f'{len(deck)} cards remain in deck{decknum}')
        # print(f'{pick} is the random intgr.')
        usedbox.append(deck[pick])
        # print(usedbox)
        # print(deck[pick].replace(deck[pick][-1],''))
        p1.append(deck[pick].replace(deck[pick][-1],''))
        if(deck[pick][0]) == "A":
            if sum(p1value)<11:
                p1value.append(11)
            else:
                p1value.append(1)
        elif(deck[pick][0]) == "1":
            p1value.append(10)    
        elif(deck[pick][0]) == "J":
            p1value.append(10)
        elif(deck[pick][0]) == "Q":
            p1value.append(10)
        elif(deck[pick][0]) == "K":
            p1value.append(10)
        else:
            try:
                v=int(deck[pick][0])
                p1value.append(v)
            except:
                print('no v')
        print(f'{playerName},You have {p1} that is {sum(p1value)} for {playerName}')
        deck.pop(pick)
        # print(f'That card was picked from deck - {decknum}')    
        print(f'Dealer has{dealer} that is {sum(dealervalue)} for the Dealer')
        wincheck()


    def carddealStart():
        clear_output()
        import random
        decknum = random.randint(1,6)
        if decknum == 1:
            deck = decks.deckG
        elif decknum == 2:
            deck = decks.deckB
        elif decknum == 3:
            deck = decks.deckC
        elif decknum == 4:
            deck = decks.deckD
        elif decknum == 5:
            deck = decks.deckE
        elif decknum == 6:
            deck = decks.deckF
        pick = random.randint(0,len(deck)-1)
        # print(len(deck))
        # print(pick)
        usedbox.append(deck[pick])
        # print(deck[pick].replace(deck[pick][-1],''))
        p1.append(deck[pick].replace(deck[pick][-1],''))
        if(deck[pick][0]) == "A":
            if sum(p1value)<11:
                p1value.append(11)
            else:
                p1value.append(1)
        elif(deck[pick][0]) == "1":
            p1value.append(10)    
        elif(deck[pick][0]) == "J":
            p1value.append(10)
        elif(deck[pick][0]) == "Q":
            p1value.append(10)
        elif(deck[pick][0]) == "K":
            p1value.append(10)
        else:
            try:
                v=int(deck[pick][0])
                p1value.append(v)
            except:
                print('no v')
        print(f'{playerName},You have {p1} that is {sum(p1value)} for {playerName}')
        deck.pop(pick)
        # print(decknum)    

        import random
        decknumA = random.randint(1,6)
        if decknumA == 1:
            deckA = decks.deckG
        elif decknumA == 2:
            deckA = decks.deckB
        elif decknumA == 3:
            deckA = decks.deckC
        elif decknumA == 4:
            deckA = decks.deckD
        elif decknumA == 5:
            deckA = decks.deckE
        elif decknumA == 6:
            deckA = decks.deckF
        pickA = random.randint(0,len(deckA)-1)
        # print(len(deckA))
        # print(decknumA)
        usedbox.append(deckA[pickA])
        print(deckA[pickA].replace(deckA[pickA][-1],''))
        dealer.append(deckA[pickA].replace(deckA[pickA][-1],''))
        if(deckA[pickA][0]) == "A":
            if sum(dealervalue)<11:
                dealervalue.append(11)
            else:
                dealervalue.append(1)
        elif(deckA[pickA][0]) == "1":
            dealervalue.append(10)    
        elif(deckA[pickA][0]) == "J":
            dealervalue.append(10)
        elif(deckA[pickA][0]) == "Q":
            dealervalue.append(10)
        elif(deckA[pickA][0]) == "K":
            dealervalue.append(10)
        else:
            try:
                v=int(deckA[pickA][0])
                dealervalue.append(v)
            except:
                print('no v')
        print(f'Dealer has{dealer} that is {sum(dealervalue)} for the Dealer')
        deckA.pop(pickA)
        # print(decknumA)    
        wincheck()


    def Dcarddeal():
        clear_output()
        import random
        decknum = random.randint(1,6)
        if decknum == 1:
            deck = decks.deckG
        elif decknum == 2:
            deck = decks.deckB
        elif decknum == 3:
            deck = decks.deckC
        elif decknum == 4:
            deck = decks.deckD
        elif decknum == 5:
            deck = decks.deckE
        elif decknum == 6:
            deck = decks.deckF
        pick = random.randint(0,len(deck)-1)
        # print(len(deck))
        # print(decknum)
        usedbox.append(deck[pick])
        # print(deck[pick].replace(deck[pick][-1],''))
        dealer.append(deck[pick].replace(deck[pick][-1],''))
        if(deck[pick][0]) == "A":
            if sum(dealervalue)<11:
                dealervalue.append(11)
            else:
                dealervalue.append(1)
        elif(deck[pick][0]) == "1":
            dealervalue.append(10)    
        elif(deck[pick][0]) == "J":
            dealervalue.append(10)
        elif(deck[pick][0]) == "Q":
            dealervalue.append(10)
        elif(deck[pick][0]) == "K":
            dealervalue.append(10)
        else:
            try:
                v=int(deck[pick][0])
                dealervalue.append(v)
            except:
                print('no v')
        print(f'{playerName},You have {p1} that is {sum(p1value)} for {playerName}')
        print(f'Dealer has{dealer} that is {sum(dealervalue)} for the Dealer')
        deck.pop(pick)
        # print(decknum)
        dealerLOGIC()


    def gamestart():
        # print(decks.deckB)
        # print(decks.deckC)
        # print(decks.deckD)
        # print(decks.deckE)
        # print(decks.deckF)
        # print(decks.deckG)
        while True:
            try:
                p1bet = int(input("place your Bet:"))
                playerBal = playerAcct.__int__()
                if p1bet > 99 and p1bet < playerBal:
                    bets.append(p1bet)
                    betreturn.append(p1bet)
                    print(bets)
                    playerAcct.withd(p1bet)
                    print(f"{playerName} has placed a bet of {p1bet}")
                    print(playerBal)
                    carddealStart()
                    break
                else:
                    print("error bet range")
            except ValueError:
                print("Noinput is not a number. It's a string")



    gamestart()

BLACKJACK()