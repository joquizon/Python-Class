
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
                        print(f'[24]>>>sick dates:......{nmlist[sposit[0]+1]}')
                for reader3 in range(len(nmlist[sposit[0]+2])):
                    if reader3==0:
                        print(f'[25]>>>personal dates:......{nmlist[sposit[0]+2]}')
                for reader4 in range(len(nmlist[sposit[0]+3])):
                    if reader4==0:
                        print(f'[26]>>>vacation dates:......{nmlist[sposit[0]+3]}')
            else:
                pass
    else:
        print(f'sorry {searcher} is not listed')
        empsearchprinter(nlist,nmlist,sposit,retfunc)


























def sickdayslog(retfunc,nmlist,sposit,mn,dn,yn):
    sickdays=[]
    sickentries=[0,0,0,0]
    curryr = []
    pastyr = []
    yearnowsick = yn
    yearstr = str(yearnowsick-1)
    sickdays.clear()
    curryr.clear()
    pastyr.clear()
    currlist = nmlist[sposit[0]]
    currsicklist = nmlist[sposit[0]+1]
    # >>>>>>>>>>>>>>>> add more sickday entries
    def moresickentries():
        morent= input('would you like to enter more sick days <y for yes OR n for no>: ').lower()
        if morent == 'y':
            for x in range(len(sickdays)):
                if sickdays[x][-2]+sickdays[x][-1] == yearstr or sickdays[x][-2]+sickdays[x][-1] == str(yearnowsick):
                    curryr.append(sickdays[x])
                else:
                    pastyr.append(sickdays[x])
            print(len(curryr))
            print(curryr)
            print(pastyr)
            currlist[18] = len(curryr) + int(currlist[18])
            currlist[19] = int(currlist[19])-len(curryr)
            for d in range(len(curryr)):
                currsicklist.append(curryr[d])
            for e in range(len(pastyr)):
                currsicklist.append(pastyr[e])
            sickdayslog()
        elif morent == 'n':
            for x in range(len(sickdays)):
                if sickdays[x][-2]+sickdays[x][-1] == yearstr or sickdays[x][-2]+sickdays[x][-1] == str(yearnowsick):
                    curryr.append(sickdays[x])
                else:
                    pastyr.append(sickdays[x])
            print(len(curryr))
            print(curryr)
            print(pastyr)
            currlist[18] = len(curryr) + int(currlist[18])
            currlist[19] = int(currlist[19])-len(curryr)
            for d in range(len(curryr)):
                currsicklist.append(curryr[d])
            for e in range(len(pastyr)):
                currsicklist.append(pastyr[e])
            print('done!')
            EditMenu(retfunc)
        else:
            print('<y for yes OR n for no> is all im taking')
            moresickentries()

#>>>>>>>>>>>>>>>>>sick day setter func  
    def sickfiler():
        monthSick=sickentries[0]
        date=sickentries[1]
        year=sickentries[2]
        amt=sickentries[3]
        print(f'{monthSick}/{date}/{year}.amt{amt}')
        if monthSick == 2 and year==20 or year==24 or year==28 or year==32 or year==36 or year==40 or year==44 or year==48 or year==52 or year==56 or year==60 or year==64 or year==68 or year==72 or year==76 or year==80 or year==84 or year==88 or year==92 or year==96:
            if date + amt>31:
                amtnew = 31 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    sickdays.append(f'{monthSick}/{date+x}/{year}')
                for z in range(amtB):
                    sickdays.append(f'{monthSick+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    sickdays.append(f'{monthSick}/{date+x}/{year}')                 
        elif monthSick == 2:
            if date + amt>29:
                amtnew = 29 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    sickdays.append(f'{monthSick}/{date+x}/{year}')
                for z in range(amtB):
                    sickdays.append(f'{monthSick+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    sickdays.append(f'{monthSick}/{date+x}/{year}') 
        elif monthSick == 4 or monthSick == 6 or monthSick ==  9 or monthSick ==  11:
            if date + amt>31:
                amtnew = 31 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    sickdays.append(f'{monthSick}/{date+x}/{year}')
                for z in range(amtB):
                    sickdays.append(f'{monthSick+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    sickdays.append(f'{monthSick}/{date+x}/{year}') 
        elif monthSick == 1 or monthSick == 3 or monthSick ==  5 or monthSick ==  7 or monthSick ==  8 or monthSick ==  10:
            if date + amt>32:
                amtnew = 32 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    sickdays.append(f'{monthSick}/{date+x}/{year}')
                for z in range(amtB):
                    sickdays.append(f'{monthSick+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    sickdays.append(f'{monthSick}/{date+x}/{year}')
        elif monthSick == 12:
            if date + amt>32:
                amtnew = 32 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    sickdays.append(f'{monthSick}/{date+x}/{year}')
                for z in range(amtB):
                    sickdays.append(f'1/{1+z}/{year+1}')
            else:
                for x in range (amt):
                    sickdays.append(f'{monthSick}/{date+x}/{year}') 
        print(sickdays)
        moresickentries()
        
#>>>>>>>>>>>>>>>>>year entry    
    def sickamount():
            sickamt = (input('enter no. of days taken: '))
            if sickamt == '*':
                sickYear()
            else:
                while True:
                    try:
                        sickamtnom = int(sickamt)
                        if sickamtnom > 0:
                            sickentries[3]=sickamtnom
                            sickfiler()
                        else:
                            print('nooooo')
                            sickamount()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        sickamount()
                        break
                    else:
                        break       
        
    
#>>>>>>>>>>>>>>>>>year entry    
    def sickYear():
            sickYe = (input('enter 2 digit format of numerical year 00-99 pls: '))
            if sickYe == '*':
                sickDay()
            else:
                while True:
                    try:
                        month = sickentries[0]
                        date = sickentries[1]
                        sickYenom = int(sickYe)
                        sickYelist = len(str(sickYe))
                        print(sickYelist)
                        if sickYelist == 2 and  sickYenom  <= int(yearnowsick) and month == 2 and date>28:
                            if sickYenom==20 or sickYenom==24 or sickYenom==28 or sickYenom==32 or sickYenom==36 or sickYenom==40 or sickYenom==44 or sickYenom==48 or sickYenom==52 or sickYenom==56 or sickYenom==60 or sickYenom==64 or sickYenom==68 or sickYenom==72 or sickYenom==76 or sickYenom==80 or sickYenom==84 or sickYenom==88 or sickYenom==92 or sickYenom==96:
                                sickentries[2] = sickYenom
                                sickamount()
                            else:
                                print('not a leap year! enter new date')
                                sickDay()
                        elif sickYelist == 2 and  sickYenom  <= int(yearnowsick):
                            sickentries[2] = sickYenom
                            sickamount()
                        else:
                            print('nooooo')
                            sickYear()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        sickYear()
                        break
                    else:
                        break    
    
#>>>>>>>>>>>>>>>>>date entry
    def sickDay():
            sickDa = (input('enter numerical date 1-31 pls: '))
            if sickDa == '*':
                sickMonth(retfunc)
            else:
                while True:
                    try:
                        month = sickentries[0]
                        print(month)
                        sickDanom = int(sickDa)
                        if month == 2 and yearnowsick==20 or yearnowsick==24 or yearnowsick==28 or yearnowsick==32 or yearnowsick==36 or yearnowsick==40 or yearnowsick==44 or yearnowsick==48 or yearnowsick==52 or yearnowsick==56 or yearnowsick==60 or yearnowsick==64 or yearnowsick==68 or yearnowsick==72 or yearnowsick==76 or yearnowsick==80 or yearnowsick==84 or yearnowsick==88 or yearnowsick==92 or yearnowsick==96:
                            if sickDanom  > 0 and sickDanom  < 30:
                                sickentries[1]=sickDanom
                                sickYear()
                            else:
                                print('nooooo')
                                sickDay()
                        elif month == 2:
                            if sickDanom  > 0 and sickDanom  < 29:
                                sickentries[1]=sickDanom
                                sickYear()
                            else:
                                print('nooooo')
                                sickDay()
                        elif month == 1 or month == 3 or month ==  5 or month ==  7 or month ==  8 or month ==  10 or month ==  12:
                            if sickDanom  > 0 and sickDanom  < 32:
                                sickentries[1]=sickDanom
                                sickYear()
                            else:
                                print('nooooo')
                                sickDay()
                        elif month == 4 or month == 6 or month ==  9 or month ==  11:
                            if sickDanom  > 0 and sickDanom  < 31:
                                sickentries[1]=sickDanom
                                sickYear()
                            else:
                                print('nooooo')
                                sickDay()
                        else:
                            print('nooooo')
                            sickDay()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        sickDay()
                        break
                    else:
                        break
                    
#>>>>>>>>>>>>>>>>>month entry
    def sickMonth(retfunc):
            sickMo = (input('enter numerical month 1-12 pls: '))
            if sickMo == '*':
                retfunc()
            else:
                while True:
                    try:
                        sickMonom = int(sickMo)
                        if sickMonom> 0 and sickMonom < 13:
                            sickentries[0]=sickMonom
                            print(sickentries[0])
                            sickDay()
                        else:
                            print('nooooo')
                            sickMonth()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        sickMonth()
                        break
                    else:
                        break
    sickMonth(retfunc)





























def EditMenu(retfunc,nmlist,sposit,mn,dn,yn):
    wachuwant= input('if you would like to input\nsick days enter (s)\npersonal days enter (p)\nvacation days enter (v)\nIf you would like to edit the list of days taken enter (m)\nOr If you wish to go to the main menu enter (*)\nOR if you wish to save your current changes enter (sv): ').lower()
    if wachuwant == 's':
        sickdayslog(retfunc,nmlist,sposit,mn,dn,yn)
    elif wachuwant == 'p':
        # persdayslog()
        pass
    elif wachuwant == 'v':
        # vacdayslog()
        pass
    elif wachuwant == 'm':
        # Mainsicpervac_Mtn()
        pass
    elif wachuwant == '*':
        retfunc()
    elif wachuwant == 'sv':
        editlist = nmlist[sposit[0]]
        editlistA = nmlist[sposit[0]+1]
        editlistB = nmlist[sposit[0]+2]
        editlistC = nmlist[sposit[0]+3]
        rts(list,list2,list3,list4,confirmfunc,retfunc,savefunc,nlist,mn,dn,yn,ds)
    else:
        print('sorry that was not a choice!')
        EditMenu(retfunc,nmlist,sposit,mn,dn,yn)






