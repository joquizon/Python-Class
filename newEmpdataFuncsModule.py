statedictionary = {"DISTRICT OF COLUMBIA":'DC',"ALABAMA":'AL',"ALASKA":'AK',"ARIZONA":'AZ',"ARKANSAS":'AR',"CALIFORNIA":'CA',"COLORADO":'CO',"CONNECTICUT":'CT',"DELAWARE":'DE',"FLORIDA":'FL',"GEORGIA":'GA',"HAWAII":'HI',"IDAHO":'ID',"ILLINOIS":'IL',"INDIANA":'IN',"IOWA":'IA',"KANSAS":'KS',"KENTUCKY":'KY',"LOUISIANA":'LA',"MAINE":'ME',"MARYLAND":'MD',"MASSACHUSETTS":'MA',"MICHIGAN":'MI',"MINNESOTA":'MN',"MISSISSIPPI":'MS',"MISSOURI":'MO',"MONTANA":'MT',"NEBRASKA":'NE',"NEVADA":'NV',"NEW HAMPSHIRE":'NH',"NEW JERSEY":'NJ',"NEW MEXICO":'NM',"NEW YORK":'NY',"NORTH CAROLINA":'NC',"NORTH DAKOTA":'ND',"OHIO":'OH',"OKLAHOMA":'OK',"OREGON":'OR',"PENNSYLVANIA":'PA',"RHODE ISLAND":'RI',"SOUTH CAROLINA":'SC',"SOUTH DAKOTA":'SD',"TENNESSEE":'TN',"TEXAS":'TX',"UTAH":'UT',"VERMONT":'VT',"VIRGINIA":'VA',"WASHINGTON":'WA',"WEST VIRGINIA":'WV',"WISCONSIN":'WI',"WYOMING":'WY'}
stablist = ['DC','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
stateverify = []

def fnameFunc(list,position,list2,retfunc):
        print('if you have entered the wrong mode, enter < to go back to mode select')
        firstname= input("first name: ")
        if len(firstname) == 0:
            print('cannot leave this blank')
            fnameFunc()
        elif firstname == '<':
            print('Are you sure ? Going Back to mode choice will erase all the data you have entered so far.')
            moderet= input('y for yes OR Any key for no: ')
            if moderet == 'y':
                retfunc()
            else:
                fnameFunc(list,position,list2)
        else:
           list[position]=(firstname)
           (list2[1])(list,position+1,list2)     


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>last name
def lnameFunc(list,position,list2):
    print('if you have entered the wrong previous info, enter * to go back')
    lastname= input("last name: ")
    if lastname == '*':
        list2[position-1](list,position-1,list2,retfunc)
    elif len(lastname) == 0:
        print('cannot leave this blank')
    else:
        list[position]=(lastname)
        (list2[position+1])(list,position+1,list2)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>nickname       
def nickname(list,position,list2):
    nickname= input("nickname: ")
    if nickname == '*':
        list2[position-1](list,position-1,list2)
    elif len(nickname) == 0:
        print('cannot leave this blank')
        nicknamefunc(list,position,list2)
    else:
        list[position]=(nickname)
        (list2[position+1])(list,position+1,list2)

 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssno
def ssno(list,position,list2):

        ssnomi = (input('enter ss no in 123456789 format pls: '))
        if ssnomi == '*':
            list2[position-1](list,position-1,list2)
        else:
            while True:
                try:
                    ssnom = int(ssnomi)
                    sslist = len((ssnomi))
                    print(sslist)
                    if sslist == 9:
                        list[position]=(ssnomi)
                        (list2[position+1])(list,position+1,list2)
                    else:
                        print('nooooo')
                        ssno(list,position,list2)
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    ssno(list,position,list2)
                    break
                else:
                    break        


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>telno
def telno(list,position,list2):
    telnomi = (input('enter tel no in 1234567890 format pls: '))
    if telnomi == '*':
        list2[position-1](list,position-1,list2)
    else:
        while True:
            try:
                telnom = int(telnomi)
                telist = len(str(telnomi))
                print(telist)
                if telist == 10:
                    list[position]=(telnomi)
                    (list2[position+1])(list,position+1,list2)
                else:
                    print('nooooo')
                    telno(list,position,list2)
            except ValueError :
                print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                telno(list,position,list2)
                break
            else:
                break        
                

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>street address      
def address1(list,position,list2):
    streetaddress= input("street address: ")    
    if streetaddress == '*':
        list2[position-1](list,position-1,list2)
    elif len(streetaddress) == 0:
        print('cannot leave this blank')
        address1(list,position,list2)
    else:
        list[position]=(streetaddress)
        (list2[position+1])(list,position+1,list2) 



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>city    
def cityfunc(list,position,list2):
    city= input("city: ") 
    if city == '*':
        list2[position-1](list,position-1,list2)
    elif len(city) == 0:
        print('cannot leave this blank')
        cityfunc(list,position,list2)    
    else:
        list[position]=(city)
        (list2[position+1])(list,position+1,list2)




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>state
def statecheck(list,position,list2):
    stab = input('enter State name or other if not a state: ').upper()
    stateverify.clear()
    if stab == '*':
        list2[position-1](list,position-1,list2)
    elif len(stab)>2:
        for key in statedictionary:
            if key == stab:
                print(statedictionary[stab])
            else:
                stateverify.append(1)
        if sum(stateverify)==51:
            print('this aint no state')
            statecheck(list,position,list2)
        else:
            statentry = statedictionary[stab]
            list[position]=statentry
            (list2[position+1])(list,position+1,list2)
    else:
        print(stab)
        for z in range(len(stablist)):
            if stablist[z] == stab:
                print(stablist[z])
            else:
                stateverify.append(1)
        if sum(stateverify)==51:
            print('this aint no state')
            statecheck(list,position,list2)
        else:
            list[position]=stab
            (list2[position+1])(list,position+1,list2)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zip
def zipno(list,position,list2):

        zipnomi = (input('enter zip code in 12345 format pls: '))
        if zipnomi == '*':
            list2[position-1](list,position-1,list2)
        else:
            while True:
                try:
                    zipnom = int(zipnomi)
                    ziplist = len(str(zipnomi))
                    print(ziplist)
                    if ziplist == 5:
                        list[position]=zipnom
                        print('lets do dates!')
                    else:
                        print('nooooo')
                        zipno(list,position,list2)
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    zipno(list,position,list2)
                    break
                else:
                    break   





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













def hiredate(mn,dn,yn,list,positionM,positionD,positionY,list2):
    
    hiredateset=[0,0,0]
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear
    def hireYear(yn,list,positionY):
        hireYe = (input('enter 2 digit format of year 00-99 pls: '))
        if hireYe == '*':
            hiredate(mn,dn,yn,list,positionM,positionD,positionY,list2)
        else:
            while True:
                try:
                    hireYenom = int(hireYe)
                    hireYelist = len(str(hireYe))
                    print(hireYelist)
                    if hireYelist == 2 and  hireYenom  <= yn:
                        hiredateset[2] =hireYe
                        list[positionY]=hireYe
                    else:
                        print('nooooo')
                        hireYear()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    hireYear()
                    break
                else:
                    break


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth     
    def hireMonth(yn,mn,list,positionM):
            hireMo = (input('enter 2 digit numerical month 01-12 pls: '))
            if hireMo == '*':
                hireYear(yn,list,positionY)
                hireMonth(yn,mn,list,positionM)
            else:
                while True:
                    try:
                        hireMonom = int(hireMo)
                        if int(hiredateset[2]) < yn and len(hireMo)==2 and hireMonom> 0 and hireMonom < 13:
                            hiredateset[0]=hireMo
                            list[positionM]= hireMo
                        elif int(hiredateset[2]) == yn and hireMonom<= mn and len(hireMo)==2 and hireMonom> 0:
                            hiredateset[0]=hireMo
                            list[positionM]=hireMo
                        else:
                            print('nooooo')
                            hireMonth(yn,mn,list,positionM)
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireMonth(yn,mn,list,positionM)
                        break
                    else:
                        break

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth
    def hireDay(yn,mn,dn,list,positionD):
            hireDa = (input('enter numerical 2 digit date 01-31 pls: '))
            if hireDa == '*':
                hireMonth(yn,mn,list,positionM)
                hireDay(yn,mn,dn,list,positionD)
            else:
                while True:
                    try:
                        hireDanom = int(hireDa)
                        if int(hiredateset[2]) < yn and len(hireDa)==2 and hireDanom  > 0 and hireDanom  < 32:
                            list[positionD]= hireDa
                        elif int(hiredateset[2]) == yn and int(hiredateset[0]) < mn and len(hireDa)==2 and hireDanom  > 0 and hireDanom  < 32:
                            list[positionD]= hireDa
                        elif int(hiredateset[2]) == yn and int(hiredateset[0]) == mn and len(hireDa)==2 and hireDanom  > 0 and hireDanom  <= dn:
                            list[positionD]= hireDa
                        else:
                            print('nooooo')
                            hireDay(yn,mn,dn,list,positionD)
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireDay(yn,mn,dn,list,positionD)
                        break
                    else:
                        break  
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>confirmation
    def dateconfirmation():
        print(f'month {str(list[positionM])} day {str(list[positionD])} year{str(list[positionY])}')
        dateconfirm=input('is this date correct?type(y) for yes. If not type\n(m) to fix the month\n(d) to fix the day\n(yr) to fix the year: ')
        if dateconfirm == 'y':
            print('test done')
        elif dateconfirm == 'm':
            hireMonth(yn,mn,list,positionM)
            dateconfirmation()
        elif dateconfirm == 'd':
            hireDay(yn,mn,dn,list,positionD)
            dateconfirmation()
        elif dateconfirm == 'yr':
            hireYear(yn,list,positionY)
            dateconfirmation()
        else:
            print('does not compute')
            print(f'month {str(list[positionM])} day {str(list[positionD])} year{str(list[positionY])}')
            dateconfirmation()

    hirenow = input('is today the hiring day of the employee. y for yes Or any key for no: ')
    if hirenow == '*':
        list2[-1](list,positionM-1,list2)
    elif hirenow == 'y':
        hiredM=str(mn)
        hiredD=str(dn)
        hiredY=str(yn)
        currdate = hiredM +' '+ hiredD +' '+ hiredY
        list[positionM]=(hiredM)
        list[positionD]=(hiredD)
        list[positionY]=(hiredY)
        dateconfirmation()
    else:
        hireYear(yn,list,positionY)
        hireMonth(yn,mn,list,positionM)
        hireDay(yn,mn,dn,list,positionD)
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


    def postsetter(list,ds):            
        deptA = ds[0]
        print(len(deptA))
        choicer = (len(deptA))
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
                for h in range (len(hsk)):
                    print(f"{h}...{hsk[h]}")
                    dept = department[deptchooser]
                    ds[0]=dept
                break
            if deptchooser == 1:
                for f in range (len(FD)):
                    print(f"{f}...{FD[f]}")
                    dept = department[deptchooser]
                    ds[0]=dept
                break
            if deptchooser == 2:        
                for e in range (len(eng)):
                    print(f"{e}...{eng[e]}")
                    dept = department[deptchooser]
                    ds[0]=dept
                break
            if deptchooser == 3:
                for p in range (len(pbx)):
                    print(f"{p}...{pbx[p]}")
                    dept = department[deptchooser]
                    ds[0]=dept
                break
            if deptchooser == 4:
                for s in range (len(sle)):
                    print(f"{s}...{sle[s]}")
                    dept = department[deptchooser]
                    ds[0]=dept
                break
            if deptchooser == 5:
                for a in range (len(acct)):
                    print(f"{a}...{acct[a]}")
                    dept = department[deptchooser]
                    ds[0]=dept
                break
            else:
                print('Please pick a Number from the choices***')
                depsetter(list,ds)
                break
    deptS = departmentString[int(deptchoose)]
    ds[0]=dept
    list[12]=deptS
    postsetter(list,ds)