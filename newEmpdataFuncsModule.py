statedictionary = {"DISTRICT OF COLUMBIA":'DC',"ALABAMA":'AL',"ALASKA":'AK',"ARIZONA":'AZ',"ARKANSAS":'AR',"CALIFORNIA":'CA',"COLORADO":'CO',"CONNECTICUT":'CT',"DELAWARE":'DE',"FLORIDA":'FL',"GEORGIA":'GA',"HAWAII":'HI',"IDAHO":'ID',"ILLINOIS":'IL',"INDIANA":'IN',"IOWA":'IA',"KANSAS":'KS',"KENTUCKY":'KY',"LOUISIANA":'LA',"MAINE":'ME',"MARYLAND":'MD',"MASSACHUSETTS":'MA',"MICHIGAN":'MI',"MINNESOTA":'MN',"MISSISSIPPI":'MS',"MISSOURI":'MO',"MONTANA":'MT',"NEBRASKA":'NE',"NEVADA":'NV',"NEW HAMPSHIRE":'NH',"NEW JERSEY":'NJ',"NEW MEXICO":'NM',"NEW YORK":'NY',"NORTH CAROLINA":'NC',"NORTH DAKOTA":'ND',"OHIO":'OH',"OKLAHOMA":'OK',"OREGON":'OR',"PENNSYLVANIA":'PA',"RHODE ISLAND":'RI',"SOUTH CAROLINA":'SC',"SOUTH DAKOTA":'SD',"TENNESSEE":'TN',"TEXAS":'TX',"UTAH":'UT',"VERMONT":'VT',"VIRGINIA":'VA',"WASHINGTON":'WA',"WEST VIRGINIA":'WV',"WISCONSIN":'WI',"WYOMING":'WY'}
stablist = ['DC','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
stateverify = []



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>first name
def fnameFunc(list,retfunc):
    firstname= input("first name: ")
    if len(firstname) == 0:
        print('cannot leave this blank')
        fnameFunc(list,retfunc)
    elif firstname == '<':
        print('Are you sure ? Going Back to mode choice will erase all the data you have entered so far.')
        moderet= input('(y) for yes OR (enter) key for no: ')
        if moderet == 'y':
            retfunc()
        else:
            fnameFunc(list,retfunc)
    else:
       list[0]=(firstname)
                   


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>last name
def lnameFunc(list,retfunc):
    print('if you have entered the wrong previous info, enter * to go back')
    lastname= input("last name: ")
    if lastname == '*':
        fnameFunc(list,retfunc)
        lnameFunc(list,retfunc)
    elif len(lastname) == 0:
        print('cannot leave this blank')
        lnameFunc(list,retfunc)
    else:
        list[1]=(lastname)
        


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>nickname       
def nicknameFunc(list,retfunc):
    nickname= input("nickname: ")
    if nickname == '*':
        lnameFunc(list,retfunc)
        nicknameFunc(list,retfunc)
    elif len(nickname) == 0:
        print('cannot leave this blank')
        nicknameFunc(list,retfunc)
    else:
        list[2]=(nickname)
        

 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssno
def ssno(list,retfunc):
        ssnomi = (input('enter ss no in 123456789 format pls: '))
        if ssnomi == '*':
            nicknameFunc(list,retfunc)
            ssno(list,retfunc)
        else:
            while True:
                try:
                    ssnom = int(ssnomi)
                    sslist = len((ssnomi))
                    if sslist == 9:
                        list[3]=(ssnomi)
                    else:
                        print('nooooo')
                        ssno(list,retfunc)
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    ssno(list,retfunc)
                    break
                else:
                    break        


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>telno
def telno(list,retfunc):
    telnomi = (input('enter tel no in 1234567890 format pls: '))
    if telnomi == '*':
        ssno(list,retfunc)
        telno(list,retfunc)
    else:
        while True:
            try:
                telnom = int(telnomi)
                telist = len(str(telnomi))
                if telist == 10:
                    list[4]=(telnomi)
                else:
                    print('nooooo')
                    telno(list,retfunc)
            except ValueError :
                print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                telno(list,retfunc)
                break
            else:
                break        
                

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>street address      
def address1(list,retfunc):
    streetaddress= input("street address: ")    
    if streetaddress == '*':
        telno(list,retfunc)
        address1(list,retfunc)
    elif len(streetaddress) == 0:
        print('cannot leave this blank')
        address1(list,retfunc)
    else:
        list[5]=(streetaddress)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>city    
def cityfunc(list,retfunc):
    city= input("city: ") 
    if city == '*':
        address1(list,retfunc)
        cityfunc(list,retfunc)
    elif len(city) == 0:
        print('cannot leave this blank')
        cityfunc(list,retfunc)    
    else:
        list[6]=(city)




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>state
def statecheck(list,retfunc):
    stab = input('enter State name or other if not a state: ').upper()
    stateverify.clear()
    if stab == '*':
        cityfunc(list,retfunc)
        statecheck(list,retfunc)
    elif len(stab)>2:
        for key in statedictionary:
            if key == stab:
                print(statedictionary[stab])
            else:
                stateverify.append(1)
        if sum(stateverify)==51:
            print('this aint no state')
            statecheck(list,retfunc)
        else:
            statentry = statedictionary[stab]
            list[7]=statentry
    else:
        print(stab)
        for z in range(len(stablist)):
            if stablist[z] == stab:
                print(stablist[z])
            else:
                stateverify.append(1)
        if sum(stateverify)==51:
            print('this aint no state')
            statecheck(list,retfunc)
        else:
            list[7]=stab


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zip
def zipno(list,retfunc):
    zipnomi = (input('enter zip code in 12345 format pls: '))
    if zipnomi == '*':
        statecheck(list,retfunc)
        zipno(list,retfunc)
    else:
        while True:
            try:
                zipnom = int(zipnomi)
                ziplist = len(str(zipnomi))
                if ziplist == 5:
                    list[8]=zipnom
                    print('lets do dates!')
                else:
                    print('nooooo')
                    zipno(list,retfunc)
            except ValueError :
                print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                zipno(list,retfunc)
                break
            else:
                break





def firstset(list,retfuncM):
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>confirmation
    retfunc = retfuncM
    def infoconfirmation(list):
        for num in range(len(list)):
            if list[num]==0:
                pass
            else:
                print(f'{num}....{list[num]}')

        infoconfirm=input('is this info correct?type(y) for yes. If not type the no. of the entry you wish to correct: ')

        if infoconfirm == 'y':
            print('test done')
        elif infoconfirm == '0':
            fnameFunc(list,retfunc)
            infoconfirmation(list)
        elif infoconfirm == '1':
            lnameFunc(list,retfunc) 
            infoconfirmation(list)
        elif infoconfirm == '2':
            nicknameFunc(list,retfunc)
            infoconfirmation(list)
        elif infoconfirm == '3':
            ssno(list,retfunc)
            infoconfirmation(list)
        elif infoconfirm == '4':
            telno(list,retfunc)
            infoconfirmation(list)
        elif infoconfirm == '5':
            address1(list,retfunc)
            infoconfirmation(list)
        elif infoconfirm == '6':
            cityfunc(list,retfunc)
            infoconfirmation(list)
        elif infoconfirm == '7':
            statecheck(list,retfunc)
            infoconfirmation(list)
        elif infoconfirm == '8':
            zipno(list,retfunc)
            infoconfirmation(list)
        else:
            print('does not compute')
            infoconfirmation()

    fnameFunc(list,retfunc)
    lnameFunc(list,retfunc) 
    nicknameFunc(list,retfunc)
    ssno(list,retfunc)
    telno(list,retfunc)
    address1(list,retfunc)
    cityfunc(list,retfunc)
    statecheck(list,retfunc)
    zipno(list,retfunc)
    infoconfirmation(list)






# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>













def hiredate(mn,dn,yn,list):
    
    hiredateset=[0,0,0]
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear
    def hireYear(yn,list):
        hireYe = (input('enter 2 digit format of year 00-99 pls: '))
        if hireYe == '*':
            hiredate(mn,dn,yn,list)
        else:
            while True:
                try:
                    hireYenom = int(hireYe)
                    hireYelist = len(str(hireYe))
                    print(hireYelist)
                    if hireYelist == 2 and  hireYenom  <= yn:
                        hiredateset[2] =hireYe
                        list[11]=hireYe
                    else:
                        print('nooooo')
                        hireYear(yn,list)
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    hireYear(yn,list)
                    break
                else:
                    break


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth     
    def hireMonth(yn,mn,list):
        hireMo = (input('enter 2 digit numerical month 01-12 pls: '))
        if hireMo == '*':
            hireYear(yn,list)
            hireMonth(yn,mn,list)
        else:
            while True:
                try:
                    hireMonom = int(hireMo)
                    if int(hiredateset[2]) < yn and len(hireMo)==2 and hireMonom> 0 and hireMonom < 13:
                        hiredateset[0]=hireMo
                        list[9]= hireMo
                    elif int(hiredateset[2]) == yn and hireMonom<= mn and len(hireMo)==2 and hireMonom> 0:
                        hiredateset[0]=hireMo
                        list[9]=hireMo
                    else:
                        print('nooooo')
                        hireMonth(yn,mn,list)
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    hireMonth(yn,mn,list)
                    break
                else:
                    break

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth
    def hireDay(yn,mn,dn,list):
        hireDa = (input('enter numerical 2 digit date 01-31 pls: '))
        if hireDa == '*':
            hireMonth(yn,mn,list)
            hireDay(yn,mn,dn,list)
        else:
            while True:
                try:
                    hireDanom = int(hireDa)
                    if int(hiredateset[2]) < yn and len(hireDa)==2 and hireDanom  > 0 and hireDanom  < 32:
                        list[10]= hireDa
                    elif int(hiredateset[2]) == yn and int(hiredateset[0]) < mn and len(hireDa)==2 and hireDanom  > 0 and hireDanom  < 32:
                        list[10]= hireDa
                    elif int(hiredateset[2]) == yn and int(hiredateset[0]) == mn and len(hireDa)==2 and hireDanom  > 0 and hireDanom  <= dn:
                        list[10]= hireDa
                    else:
                        print('nooooo')
                        hireDay(yn,mn,dn,list)
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    hireDay(yn,mn,dn,list)
                    break
                else:
                    break  
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>confirmation
    def dateconfirmation():
        print(f'month {str(list[9])} day {str(list[10])} year{str(list[11])}')
        dateconfirm=input('is this date correct?type(y) for yes. If not type\n(m) to fix the month\n(d) to fix the day\n(yr) to fix the year: ')
        if dateconfirm == 'y':
            print('test done')
        elif dateconfirm == 'm':
            hireMonth(yn,mn,list)
            dateconfirmation()
        elif dateconfirm == 'd':
            hireDay(yn,mn,dn,list)
            dateconfirmation()
        elif dateconfirm == 'yr':
            hireYear(yn,list)
            dateconfirmation()
        else:
            print('does not compute')
            print(f'month {str(list[9])} day {str(list[10])} year{str(list[11])}')
            dateconfirmation()

    hirenow = input('is today the hiring day of the employee. y for yes Or any key for no: ')
    if hirenow == 'y':
        hiredM=str(mn)
        hiredD=str(dn)
        hiredY=str(yn)
        currdate = hiredM +' '+ hiredD +' '+ hiredY
        list[9]=(hiredM)
        list[10]=(hiredD)
        list[11]=(hiredY)
        dateconfirmation()
    else:
        hireYear(yn,list)
        hireMonth(yn,mn,list)
        hireDay(yn,mn,dn,list)
        dateconfirmation()

 





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list for dept sets and position sets
hsk=['*deptmgr','*adeptmgr','*deptsup','hskper','hseman']
FD=['*deptmgr','*adeptmgr','*ntmgr','deptsup','ntaud','fdagnt','bllmn','drmn']
eng=['*deptmgr','*adeptmgr','*deptsup','engnr']
pbx=['*deptmgr','*adeptmgr','*deptsup','oprtr']
sle=['*deptmgr','*adeptmgr','*deptsup','res']
acct=['*cntrller','*asscntrller','acctnt']
department=[hsk,FD,eng,pbx,sle,acct]                
departmentString = ['hsk','FD','eng','pbx','sle','acct'] 

def postsetter(list,ds):            
        deptA = ds[0]
        choicer = (len(deptA))
        for h in range (len(deptA)):
            print(f"{h}...{deptA[h]}")
        positionchoose= input("enter no. for position: ")
        if positionchoose == '*':
            depsetter(list,ds)
        else:
            while True:
                try:
                    positionchooser=int(positionchoose)
                    if positionchooser>=0 and positionchooser<choicer:
                        position = ds[0][positionchooser]
                        list[13] =position
                        print(position)
                        print("test done")
                    else:
                        print('Please pick a Number from the choices+++++')
                        postsetter(list,ds)
                except ValueError:
                    print('Please pick a Number from the choices')
                    postsetter(list,ds)
                    break
                else:
                    break



def depsetter(list,ds):
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list for dept sets and position sets
    hsk=['*deptmgr','*adeptmgr','*deptsup','hskper','hseman']
    FD=['*deptmgr','*adeptmgr','*ntmgr','deptsup','ntaud','fdagnt','bllmn','drmn']
    eng=['*deptmgr','*adeptmgr','*deptsup','engnr']
    pbx=['*deptmgr','*adeptmgr','*deptsup','oprtr']
    sle=['*deptmgr','*adeptmgr','*deptsup','res']
    acct=['*cntrller','*asscntrller','acctnt']
    department=[hsk,FD,eng,pbx,sle,acct]                
    departmentString = ['hsk','FD','eng','pbx','sle','acct'] 

    deptchoose= input("enter no. for dept 0-Hskeeping, 1-Front Office, 2-Engineering, 3-PBX, 4-Sales, 5-Accting: ")
    while True:
        try:
            deptchooser=int(deptchoose)
        except:
            print('Please pick a Number from the choices')
            depsetter(list,ds)
            break
        else:
            if deptchooser == 0:
                dept = department[deptchooser]
                ds[0]=dept
                break
            if deptchooser == 1:
                dept = department[deptchooser]
                ds[0]=dept
                break
            if deptchooser == 2:        
                dept = department[deptchooser]
                ds[0]=dept
                break
            if deptchooser == 3:
                dept = department[deptchooser]
                ds[0]=dept
                break
            if deptchooser == 4:
                dept = department[deptchooser]
                ds[0]=dept
                break
            if deptchooser == 5:
                dept = department[deptchooser]
                ds[0]=dept
                break
            else:
                print('Please pick a Number from the choices***')
                depsetter(list,ds)
                break

    def depconfirmation(list):
        print(f'1 dept....{list[12]}')
        print(f'2 position....{list[13]}')
        depconfirm=input('is this info correct?type(y) for yes. If not type the no. of the entry you wish to correct: ')
        if depconfirm  =='y':
            print('test done')
        elif depconfirm == '1':
            depsetter(list,ds)
        elif depconfirm == '2':
            postsetter(list,ds)
            depconfirmation(list)
        else:
            print('does not compute')
            depconfirmation(list)

    deptS = departmentString[int(deptchoose)]
    ds[0]=dept
    list[12]=deptS
    postsetter(list,ds)
    depconfirmation(list)







# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list for dept sets and position sets
def paysetter(list):    
    pay = (input('enter rate per hour or enter salary in 00.00 format: '))
    while True:
        try:
            payno = float(pay)
            paylist = len(pay)
            print(payno)
            print(paylist)
            if paylist>=5 and pay[2]=='.':
                hourly = payno
                weekly = payno*40
                monthly = weekly *4
                yearly = monthly *12
                print(f'gross pay hourly{hourly}')
                print(f'gross pay weekly{weekly}')
                print(f'gross pay monthly{monthly}')
                print(f'gross pay yearly{yearly}')
                list[14]=hourly
                list[15]=weekly
                list[16]=monthly
                list[17]=yearly
            elif paylist>=8 and pay[5]=='.':
                weekly = payno/52
                hourly = weekly/40
                monthly = weekly *4 
                yearly = payno
                print(f'gross pay hourly{hourly}')
                print(f'gross pay weekly{weekly}')
                print(f'gross pay monthly{monthly}')
                print(f'gross pay yearly{yearly}')
                list[14]=hourly
                list[15]=weekly
                list[16]=monthly
                list[17]=yearly                    
            elif paylist>=9 and pay[6]=='.':
                weekly = payno/52
                hourly = weekly/40
                monthly = weekly *4 
                yearly = payno
                print(f'gross pay hourly{hourly}')
                print(f'gross pay weekly{weekly}')
                print(f'gross pay monthly{monthly}')
                print(f'gross pay yearly{yearly}')
                list[14]=hourly                     
                list[15]=weekly
                list[16]=monthly
                list[17]=yearly
            else:
                print('noooooope')
                paysetter(list)
        except ValueError :
            print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
            paysetter(list)
            break
        else:
            break 







def verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds):
        for x in range (len(list)):
            print(f"{x} ... {list[x]}")
        choose = input('enter (y) to confirm data or enter the no. of the line you wish to edit: ')

        if len(choose) == 0:
            print('cannot leave this blank')
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        elif choose.lower() == 'y':
            list.append(0)
            list.append(0)
            list.append(0)
            list.append(0)
            list.append(0)
            list.append(0)
            print('input test done')
            print(list)
            # readytosave()

        # >>>>>>>>>firname edit
        elif choose == '0':
            print(f'current entry: {list[0]}')
            fnameFunc(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)  

        # >>>>>>>>>last name edit
        elif choose == '1':
            print(f'current entry: {list[1]}')
            lnameFunc(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>>nick name edit
        elif choose == '2':
            print(f'current entry: {list[2]}')
            nicknameFunc(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>>ssno edit       
        elif choose == '3':            
            print(f'current entry: {list[3]}')
            ssno(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>>telno edit       
        elif choose == '4':            
            print(f'current entry: {list[4]}')
            telno(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>>telno edit       
        elif choose == '5':            
            print(f'current entry: {list[5]}')
            address1(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>>city edit
        elif choose == '6':            
            print(f'current entry: {list[6]}')
            cityfunc(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>>stte edit
        elif choose == '7':            
            print(f'current entry: {list[7]}')
            statecheck(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>>zip edit
        elif choose == '8':            
            print(f'current entry: {list[8]}')
            zipno(list,retfunc)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>> hire date edit
        elif choose == '9' or choose == '10' or choose == '11':
            print(f'current entry: mont {list[9]} day {list[10]} year {list[11]} ')
            hiredate(mn,dn,yn,list)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>> deprt edit
        elif choose == '12':
            print(f'current entry: {list[12]}')
            depsetter(list,ds)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)

        # >>>>>>>>> position edit
        elif choose == '13':
            print(f'current entry: {list[13]}')
            postsetter(list,ds)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)       

        # >>>>>>>>> pay edit
        elif choose == '14' or choose == '15' or choose == '16' or choose == '17':
            print(f'current entry: hourly {list[14]} weekly {list[15]} monthly {list[16]} yearly {list[17]}')
            paysetter(list)
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds) 

        else:
            print('incorrect data :(')
            verifier(list,list2,list3,list4,retfunc,mn,dn,yn,ds)














