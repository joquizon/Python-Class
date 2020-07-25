
def editinputFo():
    import datetime
    z=datetime.datetime.now()
    monthnow = (z.strftime("%m"))
    daynow = (z.strftime("%d"))
    yearnowactual = (z.strftime("%Y"))
    yearnow = int(yearnowactual) -2000
    hireY=1
    hiredD=1
    hiredM=1
    print(int(monthnow))
    print(int(daynow))
    print(int(yearnow))
    curremp=[0]
    searchlist=[0]
    notsearch=[]
    searchedpos=[0]

    hsk=['*deptmgr','*adeptmgr','*deptsup','hskper','hseman']
    FD=['*deptmgr','*adeptmgr','*ntmgr','deptsup','ntaud','fdagnt','bllmn','drmn']
    eng=['*deptmgr','*adeptmgr','*deptsup','engnr']
    pbx=['*deptmgr','*adeptmgr','*deptsup','oprtr']
    sle=['*deptmgr','*adeptmgr','*deptsup','res']
    acct=['*cntrller','*asscntrller','acctnt']
    department=[hsk,FD,eng,pbx,sle,acct]                
    departmentString = ['hsk','FD','eng','pbx','sle','acct'] 
    depsetedit=[]

    statedictionary = {"DISTRICT OF COLUMBIA":'DC',"ALABAMA":'AL',"ALASKA":'AK',"ARIZONA":'AZ',"ARKANSAS":'AR',"CALIFORNIA":'CA',"COLORADO":'CO',"CONNECTICUT":'CT',"DELAWARE":'DE',"FLORIDA":'FL',"GEORGIA":'GA',"HAWAII":'HI',"IDAHO":'ID',"ILLINOIS":'IL',"INDIANA":'IN',"IOWA":'IA',"KANSAS":'KS',"KENTUCKY":'KY',"LOUISIANA":'LA',"MAINE":'ME',"MARYLAND":'MD',"MASSACHUSETTS":'MA',"MICHIGAN":'MI',"MINNESOTA":'MN',"MISSISSIPPI":'MS',"MISSOURI":'MO',"MONTANA":'MT',"NEBRASKA":'NE',"NEVADA":'NV',"NEW HAMPSHIRE":'NH',"NEW JERSEY":'NJ',"NEW MEXICO":'NM',"NEW YORK":'NY',"NORTH CAROLINA":'NC',"NORTH DAKOTA":'ND',"OHIO":'OH',"OKLAHOMA":'OK',"OREGON":'OR',"PENNSYLVANIA":'PA',"RHODE ISLAND":'RI',"SOUTH CAROLINA":'SC',"SOUTH DAKOTA":'SD',"TENNESSEE":'TN',"TEXAS":'TX',"UTAH":'UT',"VERMONT":'VT',"VIRGINIA":'VA',"WASHINGTON":'WA',"WEST VIRGINIA":'WV',"WISCONSIN":'WI',"WYOMING":'WY'}
    stablist = ['DC','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
    stateverify = []



    def EditFOsavechanges():
        load = curremp[0]
        empnamer = curremp[0][0]+curremp[0][1]
        emplist[int(searchedpos[0])]= empnamer

        with open(f'testdocs\\noclist.night',mode='w')as n:
            for m in range(len(emplist)):
                n.write(f'{emplist[m]}\n')        
        
        with open(f'testdocs\\{empnamer}.night',mode='w')as t:
            for k in range(len(load)):
                t.write(f'{load[k]}\n')
        print('saved')
        
        fkey = open('testdocs/filekey.night','rb')
        key = fkey.read()
        print (key)
        cipher = Fernet(key)
        

    # >>>>>>>>>>>>>>>>>>>>>>>>>    
        Nocfile= 'testdocs/noclist.night'
        with open(Nocfile,'rb')as e:
            Nocfiletoencrypt = e.read()

        Nocencryptedfile = cipher.encrypt(Nocfiletoencrypt) 
        with open(Nocfile,'wb') as ee:
            ee.write(Nocencryptedfile)  
        
        

    # >>>>>>>>>>>>>>>>>>>>>
        infofileN= 'testdocs/'+ empnamer +'.night'
        with open(infofileN,'rb')as f:
            fileNtoencrypt = f.read()


        encryptedfileN = cipher.encrypt(fileNtoencrypt) 
        with open(infofileN,'wb') as ef:
            ef.write(encryptedfileN)

    #/////////////////////////////////////////////////////////////
        with open('testdocs/'+ empnamer +'.night','rb') as df:
            encryptedfileN = df.read()
            print(encryptedfileN)
            print('>>>>>>>>>>>>>>>>>>>>>>>')
        decrypted_fileN = cipher.decrypt(encryptedfileN)
        print(decrypted_fileN.decode())   
        modeset()


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> pay setter edit
    def paysetteredit():    
        payedit = (input('enter rate per hour or enter salary in 00.00 format: '))
        if payedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    paynoedit = float(payedit)
                    paylistedit = len(payedit)
                    print(paynoedit)
                    print(paylistedit)
                    if paylistedit>=5 and payedit[2]=='.':
                        hourlyedit = paynoedit
                        weeklyedit = paynoedit*40
                        monthlyedit = weeklyedit *4
                        yearlyedit = monthlyedit *12
                        print(f'gross pay weekly{hourlyedit}')
                        print(f'gross pay weekly{weeklyedit}')
                        print(f'gross pay monthly{monthlyedit}')
                        print(f'gross pay yearly{yearlyedit}')
                        curremp[0][14] = (hourlyedit)
                        curremp[0][15] = (weeklyedit)
                        curremp[0][16] = (monthlyedit)
                        curremp[0][17] = (yearlyedit)
                        print(curremp)
                        infoeditMenu()
                    elif paylistedit >= 8 and payedit[5]=='.':
                        weeklyedit = paynoedit/52
                        hourlyedit = weeklyedit/40
                        monthlyedit = weeklyedit *4 
                        yearlyedit = paynoedit
                        print(f'gross pay weekly{hourlyedit}')
                        print(f'gross pay weekly{weeklyedit}')
                        print(f'gross pay monthly{monthlyedit}')
                        print(f'gross pay yearly{yearlyedit}')
                        curremp[0][14] = (hourlyedit)
                        curremp[0][15] = (weeklyedit)
                        curremp[0][16] = (monthlyedit)
                        curremp[0][17] = (yearlyedit)                        
                        print(curremp)
                        infoeditMenu()
                    elif paylistedit >= 9 and payedit[6]=='.':
                        weeklyedit = paynoedit/52
                        hourlyedit = weeklyedit/40
                        monthlyedit = weeklyedit *4 
                        yearlyedit = paynoedit
                        print(f'gross pay weekly{hourlyedit}')
                        print(f'gross pay weekly{weeklyedit}')
                        print(f'gross pay monthly{monthlyedit}')
                        print(f'gross pay yearly{yearlyedit}')
                        curremp[0][14] = (hourlyedit)
                        curremp[0][15] = (weeklyedit)
                        curremp[0][16] = (monthlyedit)
                        curremp[0][17] = (yearlyedit)
                        print(curremp)
                        infoeditMenu()
                    else:
                        print('noooooope')
                        paysetter()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    paysetter()
                    break
                else:
                    break         
            
            
            
            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>position setter edit    
    def postsetteredit():            
        deptAedit = depsetedit[0]
        print(len(deptAedit))
        choiceredit = (len(deptAedit))
        positionchooseedit= input("enter no. for position: ")
        if positionchooseedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    positionchooseredit=int(positionchooseedit)
                    if positionchooseredit>=0 and positionchooseredit<choiceredit:
                        positionedit = depsetedit[0][positionchooseredit]
                        curremp[0][13] = positionedit
                        print(positionedit)
                        print(curremp)
                        infoeditMenu()
                    else:
                        print('Please pick a Number from the choices+++++')
                        postsetteredit()
                except ValueError:
                    print('Please pick a Number from the choices')
                    postsetteredit()
                    break
                else:
                    break




    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>department setter edit   
    def depsetteredit():
        deptchooseredit= input("enter no. for dept 0-Hskeeping, 1-Front Office, 2-Engineering, 3-PBX, 4-Sales, 5-Accting: ")
        if deptchooseredit == '*':
            infoeditMenu()
        elif deptchooseredit == '0':
            for h in range (len(hsk)):
                print(f"{h}...{hsk[h]}")

            depsetedit[0]=(department[int(deptchooseredit)])
            curremp[0][11] = departmentString[int(deptchooseredit)]
            postsetteredit()
        elif deptchooseredit == '1':
            for f in range (len(FD)):
                print(f"{f}...{FD[f]}")

            depsetedit[0]=(department[int(deptchooseredit)])
            curremp[0][12] = departmentString[int(deptchooseredit)]
            postsetteredit()
        elif deptchooseredit == '2':        
            for e in range (len(eng)):
                print(f"{e}...{eng[e]}")

            depsetedit[0]=(department[int(deptchooseredit)])
            curremp[0][12] = departmentString[int(deptchooseredit)]
            postsetteredit()
        elif deptchooseredit == '3':
            for p in range (len(pbx)):
                print(f"{p}...{pbx[p]}")

            depsetedit[0]=(department[int(deptchooseredit)])
            curremp[0][12] = departmentString[int(deptchooseredit)]
            postsetteredit()
        elif deptchooseredit == '4':
            for s in range (len(sle)):
                print(f"{s}...{sle[s]}")

            depsetedit[0]=(department[int(deptchooseredit)])
            curremp[0][12] = departmentString[int(deptchooseredit)]
            postsetteredit()
        elif deptchooseredit == '5':
            for a in range (len(acct)):
                print(f"{a}...{acct[a]}")

            depsetedit[0]=(department[int(deptchooseredit)])
            curremp[0][12] = departmentString[int(deptchooseredit)]
            postsetteredit()
        else:
            print('Please pick a Number from the choices***')
            depsetteredit()
        


           
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear editr verif fucn  
    def hireYearedit():
        hireYeedit = (input('enter 2 digit format of numerical year 00-99 pls: '))
        if hireYeedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    hireYenomedit = int(hireYeedit)
                    hireYelistedit = len(str(hireYeedit))
                    print(hireYelistedit)
                    if hireYelistedit == 2 and  hireYenomedit <= int(yearnow):
                        curremp[0][11]=hireYeedit
                        print(curremp)
                        infoeditMenu()  
                    else:
                        print('nooooo')
                        hireYearedit()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    hireYearedit()
                    break
                else:
                    break         
            
            
            
            
            
            
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireday   editrector for verifierfucn       
    def hireDayedit():
        hireDaedit = (input('enter numerical date 1-31 pls: '))
        if hireDaedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    hireDanomedit = int(hireDaedit)
                    if int(curremp[0][11])<int(yearnow) and len(hireDaedit)==2 and hireDanomedit  > 0 and hireDanomedit  < 32:
                        curremp[0][10] = hireDaedit
                        print(curremp)
                        infoeditMenu()
                    elif int(curremp[0][11]) == int(yearnow) and int(curremp[0][9]) < int(monthnow) and len(hireDaedit)==2 and hireDanomedit  > 0 and hireDanomedit  < 32:
                        curremp[0][10] = hireDaedit
                        print(curremp)
                        infoeditMenu()
                    elif int(curremp[0][11]) == int(yearnow) and int(curremp[0][9]) == int(monthnow) and len(hireDaedit)==2 and hireDanomedit  > 0 and hireDanomedit <= int(daynow):
                        curremp[0][10] = hireDaedit
                        print(curremp)
                        infoeditMenu()
                    else:
                        print('nooooo')
                        hireDayedit()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    hireDayedit()
                    break
                else:
                    break          
            
            
            


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth editrector for verifierfucn   
    def hireMonthedit():
        print('if youve entered the wrong no. enter * to choose again')
        hireMoedit = (input('enter 2 digit numerical month 01-12 pls: '))
        if hireMoedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    hireMonomedit = int(hireMoedit)
                    hireMolistedit = len(str(hireMoedit))
                    print(hireMolistedit)
                    if int(curremp[0][11]) < int(yearnow) and hireMolistedit == 2 and hireMonomedit < 13:
                        curremp[0][9] = hireMoedit
                        print(curremp)
                        infoeditMenu()  
                    elif int(curremp[0][11])==int(yearnow) and hireMolistedit == 2 and hireMonomedit <= int(monthnow):
                        curremp[0][9] = hireMoedit
                        print(curremp)
                        infoeditMenu()                        
                    else:
                        print('check your year entry, it may be incorrect i.e. i cannot enter a future month this year')
                        hireMonthedit()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    hireMonthedit()
                    break
                else:
                    break       
            
                            
            
            
            
            
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zip  editrector for verifierfucn    
    def zipnoedit():
        print('if youve entered the wrong no. enter * to choose again')
        zipnomiedit = (input('enter zip code in 12345 format pls: '))
        if zipnomiedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    zipnomedit = int(zipnomiedit)
                    ziplistedit = len(str(zipnomiedit))
                    print(ziplistedit)
                    if ziplistedit == 5:
                        curremp[0][8] = zipnomedit
                        print(curremp)
                        infoeditMenu()
                    else:
                        print('nooooo')
                        zipnoedit()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    zipnoedit()
                    break
                else:
                    break             
            


            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>state editrector for verifierfucn
    def statecheckedit():
        stabedit = input('enter State name or other if not a state: ').upper()
        stateverify.clear()
        if stabedit == '*':
            infoeditMenu()
        elif len(stabedit)>2:
            for key in statedictionary:
                if key == stabedit:
                    print(statedictionary[stabedit])
                else:
                    stateverify.append(1)
            if sum(stateverify)==51:
                print('this aint no state')
                statecheckedit()
            else:
                statentry = statedictionary[stabedit]
                curremp[0][7]=statentry
                print(curremp)
                infoeditMenu() 
        else:
            print(stabedit)
            for z in range(len(stablist)):
                if stablist[z] == stabedit:
                    print(stablist[z])
                else:
                    stateverify.append(1)
            if sum(stateverify)==51:
                print('this aint no state')
                statecheckedit()
            else:
                curremp[0][7]=stabedit
                print(curremp)
                infoeditMenu()        

            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>telno editrector for verifierfucn        
    def telnoedit():
        print('if youve entered the wrong no. enter * to choose again')
        telnomiedit = (input('enter tel no in 1234567890 format pls: '))
        if telnomiedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    telnomedit = int(telnomiedit)
                    telistedit = len(str(telnomiedit))
                    print(telistedit)
                    if telistedit == 10:
                        curremp[0][4]=telnomedit
                        print(curremp)
                        infoeditMenu()
                    else:
                        print('nooooo')
                        telnoedit()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    telnoedit()
                    break
                else:
                    break        
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssno for edit section
    def ssnoedit():
        print('if youve entered the wrong no. enter * to choose again')
        ssnomiedit = (input('enter ss no in 123456789 format pls: '))
        if ssnomiedit == '*':
            infoeditMenu()
        else:
            while True:
                try:
                    ssnomedit = int(ssnomiedit)
                    sslistedit = len(str(ssnomedit))
                    print(sslistedit)
                    if sslistedit == 9:
                        curremp[0][3]=ssnomedit
                        print(curremp)
                        infoeditMenu()
                    else:
                        print('nooooo')
                        ssnoedit()
                except ValueError :
                    print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                    ssnoedit()
                    break
                else:
                    break 






#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>lname for edit section                
    def lnameEdit():
        for xx in range(len(noclist)):
            if str(curremp[0][0]+curremp[0][1]) == noclist[xx]:
                newlname = xx
            else:
                pass
        lastname= input("last name: ")
        if len(lastname) == 0:
            print('cannot leave this blank')
            fnameEdit()
        elif lastname == '*':
                infoeditMenu()
        else:
            curremp[0][1] = lastname
            noclist[int(newlname)] = curremp[0][0] + curremp[0][1]
            print(noclist)
            print(curremp)
            infoeditMenu()







#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>first name for edit section 
    def fnameEdit():
        for x in range(len(noclist)):
            if str(curremp[0][0]+curremp[0][1]) == noclist[x]:
                newname = x
            else:
                pass
        firstname= input("first name: ")
        if len(firstname) == 0:
            print('cannot leave this blank')
            fnameEdit()
        elif firstname == '*':
                infoeditMenu()
        else:
            curremp[0][0] = firstname
            noclist[int(newname)] = curremp[0][0] + curremp[0][1]
            print(noclist)
            print(curremp)
            infoeditMenu()


    def infoeditMenu():
        whicher = input('Enter the line you wish to edit\nor type(*) to return to the previous box\nor (<) to return to the main menu\nor (s) to save your changes: ')
        if  whicher == '2' or whicher == '5' or whicher == '6':
            print('if youve entered the wrong no. enter * to choose again')
            newentry = input('correction: ')
            if newentry == '*':
                infoeditMenu()
            elif len(newentry) == 0:
                print('cannot leave this blank')
                infoeditMenu()
            else:
                curremp[0][int(whicher)] = newentry
                print(f'Info on line {whicher} has now been changed to {newentry}.')
                infoeditMenu()
        elif whicher == '0':
            fnameEdit()
        elif whicher == '1':
            lnameEdit()
        elif whicher == '3':
            ssnomedit()
        elif whicher == '4':
            telnoedit()
        elif whicher == '7':
            statecheckedit()
        elif whicher == '8':
            zipnoedit()
        elif whicher == '9':
            hireMonthedit()
        elif whicher == '10':
            hireDayedit()
        elif whicher == '11':
            hireYearedit()
        elif whicher == '12':
            depsetteredit()  
        elif whicher == '13':
            currdep = depsetedit[0]
            for a in range (len(currdep)):
                print(f"{a}...{currdep[a]}")
            postsetteredit()        
        elif whicher == '14' or whicher == '15' or whicher == '16' or whicher == '17':
            paysetteredit()
        elif whicher == '*':
            editinputFo()
        elif whicher == '<':
            modeset()
        elif whicher =='s':
            EditFOsavechanges()
        else:
            print('incorrect data :(')
            infoeditMenu()




    from cryptography.fernet import Fernet
    fkey = open('testdocs/filekey.night','rb')
    key = fkey.read()
    print (key)
    cipher = Fernet(key)          
    with open('testdocs/noclist.night','rb') as df:
        encryptedfile = df.read()
    decrypted_file = cipher.decrypt(encryptedfile)



    noclist = (decrypted_file.decode()).splitlines() 
    emplist = noclist
    print(emplist)



    print('This is where you edit employee information, if you re here by mistake type (<) to return to main menu')
    searcher= input('employee name:')
    for k in range(len(emplist)):
        if searcher == emplist[k]:
            searchlist[0]=emplist[k]
            searchedpos[0]=k
        else:
            notsearch.append(emplist[k])
    if searchlist[0] == emplist[int(searchedpos[0])]:
        print('employee found!')
        from cryptography.fernet import Fernet
        fkey = open('testdocs/filekey.night','rb')
        key = fkey.read()
        print (key)
        cipher = Fernet(key)   
        search = searchlist[0]
        with open('testdocs/'+search+'.night','rb') as et:
            encryptedfileA = et.read()
        decrypted_fileA = cipher.decrypt(encryptedfileA)

        load = (decrypted_fileA.decode()).splitlines() 
        print(load)
        curremp[0]=load
        
        for reader in range(len(load)):
            if reader==0:
                print(f'{[reader]}>>>firstname:.....{load[reader]}')
            elif reader==1:
                print(f'{[reader]}>>>lastname:......{load[reader]}')
            elif reader==2:
                print(f'{[reader]}>>>nickname:......{load[reader]}')
            elif reader==3:
                print(f'{[reader]}>>>soc no.:......{load[reader]}')
            elif reader==4:
                print(f'{[reader]}>>>tel no.:......{load[reader]}')
            elif reader==5:
                print(f'{[reader]}>>>address:......{load[reader]}')
            elif reader==6:
                print(f'{[reader]}>>>city:......{load[reader]}')
            elif reader==7:
                print(f'{[reader]}>>>state:......{load[reader]}')
            elif reader==8:
                print(f'{[reader]}>>>zip:......{load[reader]}')
            elif reader==9:
                print(f'{[reader]}>>>hire month:......{load[reader]}')
            elif reader==10:
                print(f'{[reader]}>>>hire date:......{load[reader]}')
            elif reader==11:
                print(f'{[reader]}>>>hire year:......{load[reader]}')
            elif reader==12:
                print(f'{[reader]}>>>department:......{load[reader]}')
            elif reader==13:
                print(f'{[reader]}>>>position:......{load[reader]}')
            elif reader==14:
                print(f'{[reader]}>>>hourly pay:......{load[reader]}')
            elif reader==15:
                print(f'{[reader]}>>>weekly pay:......{load[reader]}')
            elif reader==16:
                print(f'{[reader]}>>>monthly pay:......{load[reader]}')
            elif reader==17:
                print(f'{[reader]}>>>yearly pay:......{load[reader]}')
            elif reader==18:
                print(f'{[reader]}>>>sick days taken:......{load[reader]}')
            elif reader==19:
                print(f'{[reader]}>>>sick days remaining:......{load[reader]}')
            elif reader==20:
                print(f'{[reader]}>>>personal days taken:......{load[reader]}')
            elif reader==21:
                print(f'{[reader]}>>>personal days remaining:......{load[reader]}')
            elif reader==22:
                print(f'{[reader]}>>>vacation days taken:......{load[reader]}')
            elif reader==23:
                print(f'{[reader]}>>>vacation days remaining:......{load[reader]}')
        print(curremp)
        for d in range(len(department)):
            if load[12]== departmentString[d]:
                depsetedit.append(department[d])
            else:
                pass
        print(depsetedit)
        print(len(depsetedit[0]))
        infoeditMenu()
    elif searcher == '<':
        modeset()
    else:
        print('employee not found!')
        editinputFo()

