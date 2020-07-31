
def empsearchprinter(nlist,nmlist,sposit,retfunc):
    print('This is where you edit employee information, if you re here by mistake type (<) to return to main menu')
    holdinglist = nmlist[::4]
    print(str(holdinglist[1][0]+holdinglist[1][1]))
    itsthere = 'false'
    print(nlist)
    searcher= input('employee name:')
    for k in range(len(nlist)):
        # if in input is in the noclist
        if searcher == nlist[k]:
            print('employee found!')
            itsthere = 'true'
        else:
            pass
    if searcher == '<':
        retfunc()
    if itsthere == 'true':
        # check the nocmemlist and match input to a name
        for emp in range (len(holdinglist)):
            if searcher == (str(holdinglist[emp][0]))+(str(holdinglist[emp][1])):
                #this is input's position in the nocmemlist
                if emp == 0:
                    sposit[0]=0
                elif emp > 0:
                    sposit[0] = emp*4
                for reader in range(len(holdinglist[emp])):
                    if reader==0:
                        print(f'{[reader]}>>>firstname:.....{holdinglist[emp][reader]}')
                    elif reader==1:
                        print(f'{[reader]}>>>lastname:......{holdinglist[emp][reader]}')
                    elif reader==2:
                        print(f'{[reader]}>>>nickname:......{holdinglist[emp][reader]}')
                    elif reader==3:
                        print(f'{[reader]}>>>soc no.:......{holdinglist[emp][reader]}')
                    elif reader==4:
                        print(f'{[reader]}>>>tel no.:......{holdinglist[emp][reader]}')
                    elif reader==5:
                        print(f'{[reader]}>>>address:......{holdinglist[emp][reader]}')
                    elif reader==6:
                        print(f'{[reader]}>>>city:......{holdinglist[emp][reader]}')
                    elif reader==7:
                        print(f'{[reader]}>>>state:......{holdinglist[emp][reader]}')
                    elif reader==8:
                        print(f'{[reader]}>>>zip:......{holdinglist[emp][reader]}')
                    elif reader==9:
                        print(f'{[reader]}>>>hire month:......{holdinglist[emp][reader]}')
                    elif reader==10:
                        print(f'{[reader]}>>>hire date:......{holdinglist[emp][reader]}')
                    elif reader==11:
                        print(f'{[reader]}>>>hire year:......{holdinglist[emp][reader]}')
                    elif reader==12:
                        print(f'{[reader]}>>>department:......{holdinglist[emp][reader]}')
                    elif reader==13:
                        print(f'{[reader]}>>>position:......{holdinglist[emp][reader]}')
                    elif reader==14:
                        print(f'{[reader]}>>>hourly pay:......{holdinglist[emp][reader]}')
                    elif reader==15:
                        print(f'{[reader]}>>>weekly pay:......{holdinglist[emp][reader]}')
                    elif reader==16:
                        print(f'{[reader]}>>>monthly pay:......{holdinglist[emp][reader]}')
                    elif reader==17:
                        print(f'{[reader]}>>>yearly pay:......{holdinglist[emp][reader]}')
                    elif reader==18:
                        print(f'{[reader]}>>>sick days taken:......{holdinglist[emp][reader]}')
                    elif reader==19:
                        print(f'{[reader]}>>>sick days remaining:......{holdinglist[emp][reader]}')
                    elif reader==20:
                        print(f'{[reader]}>>>personal days taken:......{holdinglist[emp][reader]}')
                    elif reader==21:
                        print(f'{[reader]}>>>personal days remaining:......{holdinglist[emp][reader]}')
                    elif reader==22:
                        print(f'{[reader]}>>>vacation days taken:......{holdinglist[emp][reader]}')
                    elif reader==23:
                        print(f'{[reader]}>>>vacation days remaining:......{holdinglist[emp][reader]}')
                for reader2 in range(len(nmlist[sposit[0]+1])):
                    if reader2==0:
                        print(f'{[reader2]}>>>sick dates:......{nmlist[sposit[0]+1]}')
                for reader3 in range(len(nmlist[sposit[0]+2])):
                    if reader3==0:
                        print(f'{[reader]}>>>personal dates:......{nmlist[sposit[0]+2]}')
                for reader4 in range(len(nmlist[sposit[0]+3])):
                    if reader4==0:
                        print(f'{[reader]}>>>vacation dates:......{nmlist[sposit[0]+3]}')
            else:
                pass
    else:
        print(f'sorry {searcher} is not listed')
        empsearchprinter(nlist,nmlist,sposit,retfunc)






