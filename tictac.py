from IPython.display import clear_output
gboard=['0','1','2','3','4','5','6','7','8','9']
nuboard=['0','1','2','3','4','5','6','7','8','9']
chosen=[]
p1=[]
p2=[]
def funcky():
    def board():
            print('['+gboard[7]+']'+'['+gboard[8]+']'+'['+gboard[9]+']')
            print('['+gboard[4]+']'+'['+gboard[5]+']'+'['+gboard[6]+']')
            print('['+gboard[1]+']'+'['+gboard[2]+']'+'['+gboard[3]+']')

    board()   
    def resetB():
        gboard.clear()
        chosen.clear()
        for k in range (len(nuboard)):
            gboard.append(nuboard[k])
            print('LEt us begin again!!!!')
        funcky()
        
    def winchecker():
        aa = gboard[1],gboard[2],gboard[3]
        bb=gboard[4],gboard[5],gboard[6]
        cc=gboard[7],gboard[8],gboard[9]
        dd=gboard[1],gboard[4],gboard[7]
        ee=gboard[2],gboard[5],gboard[8]
        ff=gboard[3],gboard[6],gboard[9]
        gg=gboard[1],gboard[5],gboard[9]
        hh=gboard[3],gboard[5],gboard[7]
        if (''.join(aa)) =='XXX' or (''.join(aa))== 'OOO':
            print('we have a winner!')
            board()
            resetB()
        elif (''.join(bb)) =='XXX' or (''.join(bb))== 'OOO':
            print('we have a winner!')
            board()
            resetB()        
        elif (''.join(cc)) =='XXX' or (''.join(cc))== 'OOO':
            print('we have a winner!')
            board()
            resetB()  
        elif (''.join(dd)) =='XXX' or (''.join(dd))== 'OOO':
            print('we have a winner!')
            board()
            resetB()
        elif (''.join(ee)) =='XXX' or (''.join(ee))== 'OOO':
            print('we have a winner!')
            board()
            resetB()
        elif (''.join(ff)) =='XXX' or (''.join(ff))== 'OOO':
            print('we have a winner!')
            board()
            resetB()
        elif (''.join(gg)) =='XXX' or (''.join(gg))== 'OOO':
            print('we have a winner!')
            board()
            resetB()
        elif (''.join(hh)) =='XXX' or (''.join(hh))== 'OOO':
            print('we have a winner!')
            board()
            resetB()            
        elif sum(chosen)==45:
            print('Deadlocked!!!')
            resetB() 
        else:
            print(''.join(aa))
            print(chosen)
            clear_output()
            board()
    

    
    def moves2():
        print('your move p2')
        y= input('choose box number')
      
        try:
            val = int(y)
            val1a= int(y)
            for z in range(len(chosen)):
                if int(chosen[z])/val1a == 1:
                    print('spot is taken')
                    moves2()  
            if val > 0 and val < 10:
                gboard[(val)] = p2[0]
                chosen.append(val)
                winchecker()
                moves()
            else:
                print('ffs man! a no. from the board')
                moves2()
        except ValueError:
            try:
                val = float(y)
                print("Input is a float  number.")
                moves2()
            except ValueError:
                    print("Noinput is not a number. It's a string")
                    moves2()
        
    def moves():
        print('your move p1')
        x= input('choose box number')
           
        try:
            val = int(x)
            val1= int(x)
            for z in range(len(chosen)):
                if int(chosen[z])/val1 == 1:
                    print('spot is taken')
                    moves() 
            if val > 0 and val < 10:
                gboard[(val)] = p1[0]
                chosen.append(val)
                print(chosen)
                winchecker()
                moves2()
            else:
                print('ffs man! a no. from the board')
                moves()
        except ValueError:
            try:
                val = float(x)
                print("Input is a float  number.")
                moves()
            except ValueError:
                    print("Noinput is not a number. It's a string")
                    moves()

        
    def p2choose():
        if p1[0]=='X':
            p2.append('O')
            print(f'P2 has been given {p2[0]}!')
            moves()
        elif p1[0]=='O':
            p2.append('X')
            print(f'P2 has been given {p2[0]}!')
            moves()
        else:
            p2.append('X')
            print(f'P2 has been given {p2[0]}!')
            moves()
    def pchoose():
        w=input("P1 choose your weapon X or O : ")
        ww = w.upper()
        if ww =='X':
            p1.append(ww)
            print(f'P1 has chosen {p1[0]}')
            p2choose()
        elif ww =='O':
            p1.append(ww)
            print(f'P1 has chosen {p1[0]}')
            p2choose()
        else:
            print('Steve Harvey heeya ... Lissen playa, this heya is tic tac toe, x or o only!')
            pchoose()
            
    pchoose()
    

funcky()