
def empsearchprinter(npos,nlist,nmlist,sposit,retfunc):
    print('This is where you edit employee information, if you re here by mistake type (<) to return to main menu')
    holdinglist = nmlist[::4]
    itsthere = 'false'
    print(nlist)
    searcher= input('employee name:')
    for k in range(len(nlist)):
        # if in input is in the noclist
        if searcher == nlist[k]:
            print('employee found!')
            itsthere = 'true'
            print(itsthere)
            sposit[0] = k
            print(sposit[0])
            npos = k
            print(npos)
        else:
            pass
    if searcher == '<':
        retfunc()
    else:
        pass
    if itsthere == 'true':
        # check the nocmemlist and match input to a name
        for emp in range (len(holdinglist)):
            if searcher == (str(holdinglist[emp][0]))+(str(holdinglist[emp][1])):
                #this is input's position in the nocmemlist
                if emp == 0:
                    sposit[0]=0
                elif emp > 0:
                    sposit[0] = emp*4
                    # remember list1 is basic info + 3 sic per vac dates lists hence position * 4
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
        empsearchprinter(npos,nlist,nmlist,sposit,retfunc)








# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>









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
            sickdayslog(retfunc,nmlist,sposit,mn,dn,yn)
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
            retfunc()
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
                            sickMonth(retfunc)
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        sickMonth(retfunc)
                        break
                    else:
                        break
    sickMonth(retfunc)












# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 







# >>>>>>>>>>>>>>>>>>>>>>>> logs and personal days

def persdayslog(retfunc,nmlist,sposit,mn,dn,yn):
    persdays=[]
    persentries=[0,0,0,0]
    Pcurryr = []
    Ppastyr = []
    yearnowpers = yn
    yearnowperstr = str(yearnowpers-2)
    persdays.clear()    
    Pcurryr.clear()
    Ppastyr.clear()
    currlistp = nmlist[sposit[0]]
    currperslist = nmlist[sposit[0]+2]
# >>>>>>>>>>>>>>>> add more persday entries
    def morepersentries():
        morent= input('would you like to enter more pers days <y for yes OR n for no>: ').lower()
        if morent == 'y':
            for x in range(len(persdays)):
                if persdays[x][-2]+persdays[x][-1] == yearnowperstr or persdays[x][-2]+persdays[x][-1] == str(yearnowpers):
                    Pcurryr.append(persdays[x])
                else:
                    Ppastyr.append(persdays[x])
            print(len(Pcurryr))
            print(Pcurryr)
            print(Ppastyr)
            currlistp[20] = len(Pcurryr) + int(currlistp[20])
            currlistp[21] = int(currlistp[21])-len(Pcurryr)
            for d in range(len(Pcurryr)):
                currperslist.append(Pcurryr[d])
            for e in range(len(Ppastyr)):
                currperslist.append(Ppastyr[e])
            persdayslog(retfunc,nmlist,sposit,mn,dn,yn)
        elif morent == 'n':
            for x in range(len(persdays)):
                if persdays[x][-2]+persdays[x][-1] == yearnowperstr or persdays[x][-2]+persdays[x][-1] == str(yearnowpers):
                    Pcurryr.append(persdays[x])
                else:
                    Ppastyr.append(persdays[x])
            print(len(Pcurryr))
            print(Pcurryr)
            print(Ppastyr)
            currlistp[20] = len(Pcurryr) + int(currlistp[20])
            currlistp[21] = int(currlistp[21])-len(Pcurryr)
            for d in range(len(Pcurryr)):
                currperslist.append(Pcurryr[d])
            for e in range(len(Ppastyr)):
                currperslist.append(Ppastyr[e])
            print('done!')
            retfunc()
        else:
            print('<y for yes OR n for no> is all im taking')
            morepersentries()

#>>>>>>>>>>>>>>>>>pers day setter func  
    def persfiler():
        monthpers=persentries[0]
        date=persentries[1]
        year=persentries[2]
        amt=persentries[3]
        print(f'{monthpers}/{date}/{year}.amt{amt}')
        if monthpers == 2 and year==20 or year==24 or year==28 or year==32 or year==36 or year==40 or year==44 or year==48 or year==52 or year==56 or year==60 or year==64 or year==68 or year==72 or year==76 or year==80 or year==84 or year==88 or year==92 or year==96:
            if date + amt>31:
                amtnew = 31 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    persdays.append(f'{monthpers}/{date+x}/{year}')
                for z in range(amtB):
                    persdays.append(f'{monthpers+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    persdays.append(f'{monthpers}/{date+x}/{year}')                 
        elif monthpers == 2:
            if date + amt>29:
                amtnew = 29 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    persdays.append(f'{monthpers}/{date+x}/{year}')
                for z in range(amtB):
                    persdays.append(f'{monthpers+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    persdays.append(f'{monthpers}/{date+x}/{year}') 
        elif monthpers == 4 or monthpers == 6 or monthpers ==  9 or monthpers ==  11:
            if date + amt>31:
                amtnew = 31 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    persdays.append(f'{monthpers}/{date+x}/{year}')
                for z in range(amtB):
                    persdays.append(f'{monthpers+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    persdays.append(f'{monthpers}/{date+x}/{year}') 
        elif monthpers == 1 or monthpers == 3 or monthpers ==  5 or monthpers ==  7 or monthpers ==  8 or monthpers ==  10:
            if date + amt>32:
                amtnew = 32 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    persdays.append(f'{monthpers}/{date+x}/{year}')
                for z in range(amtB):
                    persdays.append(f'{monthpers+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    persdays.append(f'{monthpers}/{date+x}/{year}')
        elif monthpers == 12:
            if date + amt>32:
                amtnew = 32 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    persdays.append(f'{monthpers}/{date+x}/{year}')
                for z in range(amtB):
                    persdays.append(f'1/{1+z}/{year+1}')
            else:
                for x in range (amt):
                    persdays.append(f'{monthpers}/{date+x}/{year}') 
        print(persdays)
        morepersentries()
        
#>>>>>>>>>>>>>>>>>year entry    
    def persamount():
            persamt = (input('enter no. of days taken: '))
            if persamt == '*':
                persYear()
            else:
                while True:
                    try:
                        persamtnom = int(persamt)
                        if persamtnom > 0:
                            persentries[3]=persamtnom
                            persfiler()
                        else:
                            print('nooooo')
                            persamount()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        persamount()
                        break
                    else:
                        break       
        
    
#>>>>>>>>>>>>>>>>>year entry    
    def persYear():
            persYe = (input('enter 2 digit format of numerical year 00-99 pls: '))
            if persYe == '*':
                persDay()
            else:
                while True:
                    try:
                        month = persentries[0]
                        date = persentries[1]
                        persYenom = int(persYe)
                        persYelist = len(str(persYe))
                        print(persYelist)
                        if persYelist == 2 and  persYenom  <= int(yearnowpers) and month == 2 and date>28:
                            if persYenom==20 or persYenom==24 or persYenom==28 or persYenom==32 or persYenom==36 or persYenom==40 or persYenom==44 or persYenom==48 or persYenom==52 or persYenom==56 or persYenom==60 or persYenom==64 or persYenom==68 or persYenom==72 or persYenom==76 or persYenom==80 or persYenom==84 or persYenom==88 or persYenom==92 or persYenom==96:
                                persentries[2] = persYenom
                                persamount()
                            else:
                                print('not a leap year! enter new date')
                                persDay()
                        elif persYelist == 2 and  persYenom  <= int(yearnowpers):
                            persentries[2] = persYenom
                            persamount()
                        else:
                            print('nooooo')
                            persYear()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        persYear()
                        break
                    else:
                        break    
    
#>>>>>>>>>>>>>>>>>date entry
    def persDay():
            persDa = (input('enter numerical date 1-31 pls: '))
            if persDa == '*':
                persMonth(retfunc)
            else:
                while True:
                    try:
                        month = persentries[0]
                        print(month)
                        persDanom = int(persDa)
                        if month == 2 and yearnowpers==20 or yearnowpers==24 or yearnowpers==28 or yearnowpers==32 or yearnowpers==36 or yearnowpers==40 or yearnowpers==44 or yearnowpers==48 or yearnowpers==52 or yearnowpers==56 or yearnowpers==60 or yearnowpers==64 or yearnowpers==68 or yearnowpers==72 or yearnowpers==76 or yearnowpers==80 or yearnowpers==84 or yearnowpers==88 or yearnowpers==92 or yearnowpers==96:
                            if persDanom  > 0 and persDanom  < 30:
                                persentries[1]=persDanom
                                persYear()
                            else:
                                print('nooooo')
                                persDay()
                        elif month == 2:
                            if persDanom  > 0 and persDanom  < 29:
                                persentries[1]=persDanom
                                persYear()
                            else:
                                print('nooooo')
                                persDay()
                        elif month == 1 or month == 3 or month ==  5 or month ==  7 or month ==  8 or month ==  10 or month ==  12:
                            if persDanom  > 0 and persDanom  < 32:
                                persentries[1]=persDanom
                                persYear()
                            else:
                                print('nooooo')
                                persDay()
                        elif month == 4 or month == 6 or month ==  9 or month ==  11:
                            if persDanom  > 0 and persDanom  < 31:
                                persentries[1]=persDanom
                                persYear()
                            else:
                                print('nooooo')
                                persDay()
                        else:
                            print('nooooo')
                            persDay()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        persDay()
                        break
                    else:
                        break
                    
#>>>>>>>>>>>>>>>>>month entry
    def persMonth(retfunc):
            persMo = (input('enter numerical month 1-12 pls: '))
            if persMo == '*':
                retfunc()
            else:
                while True:
                    try:
                        persMonom = int(persMo)
                        if persMonom> 0 and persMonom < 13:
                            persentries[0]=persMonom
                            print(persentries[0])
                            persDay()
                        else:
                            print('nooooo')
                            persMonth(retfunc)
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        persMonth(retfunc)
                        break
                    else:
                        break
    persMonth(retfunc)    



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 




# >>>>>>>>>>>>>>>>>>>>>>>> logs and vacdays

def vacdayslog(retfunc,nmlist,sposit,mn,dn,yn):
    vacdays=[]
    vacentries=[0,0,0,0]
    toremove=[]
    yearnow = yn
    yearnowvac = int(yearnow)
    vacdays.clear()
    currVlist = nmlist[sposit[0]]
    currvaclist = nmlist[sposit[0]+3]
# >>>>>>>>>>>>>>>> remove more vacday entries
    def removemore():
        vacendchoice = input('would you like to enter another date for removal?<y for yes OR n for no>: ')
        if vacendchoice == 'y':
            dateremover()
        elif vacendchoice == 'n':
            morevacentries()
        else:
            print('sorry does not compute dude.')
            removemore()

    def dateremover():
        remover = input('enter the line no. of the date you wish to remove: ')
        for remo in range(len(vacdays)):
            if str(remo) == remover:
                toremove.append(vacdays[remo])
                print('got it')
            else:
                pass
        if len(toremove)>0:
            vacdays.pop(int(remover))
            removemore()
        elif remover == '*':
            morevacentries()
        else:
            print('sorry that is not on the list:)')
            dateremover()



# >>>>>>>>>>>>>>>> add more vacday entries
    def morevacentries():
        for r in range(len(vacdays)):
            print(f'{r} ......{vacdays[r]}')
        morent= input('would you like to ENTER more vac days <y for yes OR n for no> OR are there dates on this list that need to be removed<type 'r' to REMOVE>: ').lower()
        if morent == 'y':
            currVlist[22] = len(vacdays) + int(currVlist[22])
            currVlist[23] = int(currVlist[23])-len(vacdays)
            for d in range(len(vacdays)):
                currvaclist.append(vacdays[d])
            vacdayslog(retfunc,nmlist,sposit,mn,dn,yn)
        elif morent == 'n':
            currVlist[22] = len(vacdays) + int(currVlist[22])
            currVlist[23] = int(currVlist[23])-len(vacdays)
            for d in range(len(vacdays)):
                currvaclist.append(vacdays[d])
            print('done!')
            retfunc()
        elif morent == 'r':
            dateremover()
        else:
            print('<y for yes OR n for no> is all im taking')
            morevacentries()

#>>>>>>>>>>>>>>>>>vac day setter func  
    def vacfiler():
        monthvac=vacentries[0]
        date=vacentries[1]
        year=vacentries[2]
        amt=vacentries[3]
        print(f'{monthvac}/{date}/{year}.amt{amt}')
        if monthvac == 2 and year==20 or year==24 or year==28 or year==32 or year==36 or year==40 or year==44 or year==48 or year==52 or year==56 or year==60 or year==64 or year==68 or year==72 or year==76 or year==80 or year==84 or year==88 or year==92 or year==96:
            if date + amt>31:
                amtnew = 31 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    vacdays.append(f'{monthvac}/{date+x}/{year}')
                for z in range(amtB):
                    vacdays.append(f'{monthvac+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    vacdays.append(f'{monthvac}/{date+x}/{year}')                 
        elif monthvac == 2:
            if date + amt>29:
                amtnew = 29 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    vacdays.append(f'{monthvac}/{date+x}/{year}')
                for z in range(amtB):
                    vacdays.append(f'{monthvac+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    vacdays.append(f'{monthvac}/{date+x}/{year}') 
        elif monthvac == 4 or monthvac == 6 or monthvac ==  9 or monthvac ==  11:
            if date + amt>31:
                amtnew = 31 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    vacdays.append(f'{monthvac}/{date+x}/{year}')
                for z in range(amtB):
                    vacdays.append(f'{monthvac+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    vacdays.append(f'{monthvac}/{date+x}/{year}') 
        elif monthvac == 1 or monthvac == 3 or monthvac ==  5 or monthvac ==  7 or monthvac ==  8 or monthvac ==  10:
            if date + amt>32:
                amtnew = 32 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    vacdays.append(f'{monthvac}/{date+x}/{year}')
                for z in range(amtB):
                    vacdays.append(f'{monthvac+1}/{1+z}/{year}')
            else:
                for x in range (amt):
                    vacdays.append(f'{monthvac}/{date+x}/{year}')
        elif monthvac == 12:
            if date + amt>32:
                amtnew = 32 - date
                amtB = amt - amtnew
                for x in range(amtnew):
                    vacdays.append(f'{monthvac}/{date+x}/{year}')
                for z in range(amtB):
                    vacdays.append(f'1/{1+z}/{year+1}')
            else:
                for x in range (amt):
                    vacdays.append(f'{monthvac}/{date+x}/{year}') 
        print(vacdays)
        morevacentries()
        
#>>>>>>>>>>>>>>>>>year entry    
    def vacamount():
            vacamt = (input('enter no. of days taken: '))
            if vacamt == '*':
                vacYear()
            elif vacamt == '<':
                pass
            else:
                while True:
                    try:
                        vacamtnom = int(vacamt)
                        if vacamtnom > 0:
                            vacentries[3]=vacamtnom
                            vacfiler()
                        else:
                            print('nooooo')
                            vacamount()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        vacamount()
                        break
                    else:
                        break       
        
    
#>>>>>>>>>>>>>>>>>year entry    
    def vacYear():
            vacYe = (input('enter 2 digit format of numerical year 00-99 pls: '))
            if vacYe == '*':
                retfunc()
            else:
                while True:
                    try:
                        month = vacentries[0]
                        date = vacentries[1]
                        vacYenom = int(vacYe)
                        vacYelist = len(str(vacYe))
                        print(vacYelist)
                        if vacYelist == 2 and  vacYenom  <= int(yearnowvac) and month == 2 and date>28:
                            if vacYenom==20 or vacYenom==24 or vacYenom==28 or vacYenom==32 or vacYenom==36 or vacYenom==40 or vacYenom==44 or vacYenom==48 or vacYenom==52 or vacYenom==56 or vacYenom==60 or vacYenom==64 or vacYenom==68 or vacYenom==72 or vacYenom==76 or vacYenom==80 or vacYenom==84 or vacYenom==88 or vacYenom==92 or vacYenom==96:
                                vacentries[2] = vacYenom
                                vacamount()
                            else:
                                print('not a leap year! enter new date')
                                vacDay()
                        elif vacYelist == 2 and  vacYenom  <= int(yearnowvac):
                            vacentries[2] = vacYenom
                            vacamount()
                        else:
                            print('nooooo')
                            vacYear()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        vacYear()
                        break
                    else:
                        break    
    
#>>>>>>>>>>>>>>>>>date entry
    def vacDay():
            vacDa = (input('enter numerical date 1-31 pls: '))
            if vacDa == '*':
                vacMonth()
            else:
                while True:
                    try:
                        month = vacentries[0]
                        print(month)
                        vacDanom = int(vacDa)
                        if month == 2 and yearnowvac==20 or yearnowvac==24 or yearnowvac==28 or yearnowvac==32 or yearnowvac==36 or yearnowvac==40 or yearnowvac==44 or yearnowvac==48 or yearnowvac==52 or yearnowvac==56 or yearnowvac==60 or yearnowvac==64 or yearnowvac==68 or yearnowvac==72 or yearnowvac==76 or yearnowvac==80 or yearnowvac==84 or yearnowvac==88 or yearnowvac==92 or yearnowvac==96:
                            if vacDanom  > 0 and vacDanom  < 30:
                                vacentries[1]=vacDanom
                                vacYear()
                            else:
                                print('nooooo')
                                vacDay()
                        elif month == 2:
                            if vacDanom  > 0 and vacDanom  < 29:
                                vacentries[1]=vacDanom
                                vacYear()
                            else:
                                print('nooooo')
                                vacDay()
                        elif month == 1 or month == 3 or month ==  5 or month ==  7 or month ==  8 or month ==  10 or month ==  12:
                            if vacDanom  > 0 and vacDanom  < 32:
                                vacentries[1]=vacDanom
                                vacYear()
                            else:
                                print('nooooo')
                                vacDay()
                        elif month == 4 or month == 6 or month ==  9 or month ==  11:
                            if vacDanom  > 0 and vacDanom  < 31:
                                vacentries[1]=vacDanom
                                vacYear()
                            else:
                                print('nooooo')
                                vacDay()
                        else:
                            print('nooooo')
                            vacDay()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        vacDay()
                        break
                    else:
                        break
                    
#>>>>>>>>>>>>>>>>>month entry
    def vacMonth():
            vacMo = (input('enter numerical month 1-12 pls: '))
            if vacMo == '*':
                retfunc()
            else:
                while True:
                    try:
                        vacMonom = int(vacMo)
                        if vacMonom> 0 and vacMonom < 13:
                            vacentries[0]=vacMonom
                            print(vacentries[0])
                            vacDay()
                        else:
                            print('nooooo')
                            vacMonth()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        vacMonth()
                        break
                    else:
                        break
    vacMonth()
























