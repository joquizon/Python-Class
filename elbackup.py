def Ndataenter():
    ### # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sets variable func for input funcs to return to mode select
    currfunc=['0']

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> state verfication dict and list and utility list for loops
    statedictionary = {"DISTRICT OF COLUMBIA":'DC',"ALABAMA":'AL',"ALASKA":'AK',"ARIZONA":'AZ',"ARKANSAS":'AR',"CALIFORNIA":'CA',"COLORADO":'CO',"CONNECTICUT":'CT',"DELAWARE":'DE',"FLORIDA":'FL',"GEORGIA":'GA',"HAWAII":'HI',"IDAHO":'ID',"ILLINOIS":'IL',"INDIANA":'IN',"IOWA":'IA',"KANSAS":'KS',"KENTUCKY":'KY',"LOUISIANA":'LA',"MAINE":'ME',"MARYLAND":'MD',"MASSACHUSETTS":'MA',"MICHIGAN":'MI',"MINNESOTA":'MN',"MISSISSIPPI":'MS',"MISSOURI":'MO',"MONTANA":'MT',"NEBRASKA":'NE',"NEVADA":'NV',"NEW HAMPSHIRE":'NH',"NEW JERSEY":'NJ',"NEW MEXICO":'NM',"NEW YORK":'NY',"NORTH CAROLINA":'NC',"NORTH DAKOTA":'ND',"OHIO":'OH',"OKLAHOMA":'OK',"OREGON":'OR',"PENNSYLVANIA":'PA',"RHODE ISLAND":'RI',"SOUTH CAROLINA":'SC',"SOUTH DAKOTA":'SD',"TENNESSEE":'TN',"TEXAS":'TX',"UTAH":'UT',"VERMONT":'VT',"VIRGINIA":'VA',"WASHINGTON":'WA',"WEST VIRGINIA":'WV',"WISCONSIN":'WI',"WYOMING":'WY'}
    stablist = ['DC','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
    stateverify = []

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list that collects input data
    dataentered=[]

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>time variables for time based funcs
    import datetime
    z=datetime.datetime.now()
    monthnow = (z.strftime("%m"))
    daynow = (z.strftime("%d"))
    yearnow = (z.strftime("%Y"))
    hireY=1
    hiredD=1
    hiredM=1
    x=datetime.datetime(hireY,hiredD,hiredM)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list for dept sets and position sets
    hsk=['*deptmgr','*adeptmgr','*deptsup','hskper','hseman']
    FD=['*deptmgr','*adeptmgr','*ntmgr','deptsup','ntaud','fdagnt','bllmn','drmn']
    eng=['*deptmgr','*adeptmgr','*deptsup','engnr']
    pbx=['*deptmgr','*adeptmgr','*deptsup','oprtr']
    sle=['*deptmgr','*adeptmgr','*deptsup','res']
    acct=['*cntrller','*asscntrller','acctnt']
    department=[hsk,FD,eng,pbx,sle,acct]                
    departmentString = ['hsk','FD','eng','pbx','sle','acct'] 
    depset=[]

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sickday persday vacday listcreator
    sickdatestart =[]
    persdatestart =[]
    vacdatestart =[]



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> master employee listcreator
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







#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> creates data encryption key

    def newempfilesaver():
        from cryptography.fernet import Fernet
        # def keycreate():
        #     key = Fernet.generate_key()
        #     fkey = open('testdocs/filekey.txt','wb')
        #     fkey.write(key)
        #     print (key)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> employee name creator
        empname = dataentered[0]+dataentered[1]
            
            
        def filencrypter():  
        #         from cryptography.fernet import Fernet
        #         key = Fernet.generate_key()
        #         fkey = open('testdocs/filekey.night','wb')
        #         fkey.write(key)
        #         print (key)
            #     this open encrypter key created by keycreate() as variable

                fkey = open('testdocs/filekey.night','rb')
                key = fkey.read()
                print (key)
                cipher = Fernet(key)
            
            #     opens created files to be encrypted and encrypts


            # >>>>>>>>>>>>>>>>>>>>>
                infofile= 'testdocs/'+ empname +'.night'
                with open(infofile,'rb')as f:
                    filetoencrypt = f.read()


                encryptedfile = cipher.encrypt(filetoencrypt) 
                with open(infofile,'wb') as ef:
                    ef.write(encryptedfile)


            # >>>>>>>>>>>>>>>>>>>>>          
                sickfile= 'testdocs/'+ empname +'sickdates.night'
                with open(sickfile,'rb')as ff:
                    sickfiletoencrypt = ff.read()

                sickencryptedfile = cipher.encrypt(sickfiletoencrypt) 
                with open(sickfile,'wb') as eff:
                    eff.write(sickencryptedfile)


            # >>>>>>>>>>>>>>>>>>>>>          
                persfile= 'testdocs/'+ empname +'persdates.night'
                with open(persfile,'rb')as fff:
                    persfiletoencrypt = fff.read()

                persencryptedfile = cipher.encrypt(persfiletoencrypt) 
                with open(persfile,'wb') as efff:
                    efff.write(persencryptedfile)


            # >>>>>>>>>>>>>>>>>>>>>      
                vacfile= 'testdocs/'+ empname +'vacdates.night'
                with open(vacfile,'rb')as ffff:
                    vacfiletoencrypt = ffff.read()

                vacencryptedfile = cipher.encrypt(vacfiletoencrypt) 
                with open(vacfile,'wb') as effff:
                    effff.write(vacencryptedfile)

                    
                with open('testdocs/'+ empname +'.night','rb') as df:
                    encryptedfile = df.read()
                    print(encryptedfile)
                    print('>>>>>>>>>>>>>>>>>>>>>>>')
                decrypted_file = cipher.decrypt(encryptedfile)
                print(decrypted_file.decode())           
                modeset()


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>encrypts noclist
        def noclistencrypt():    
            #     this open encrypter key created by keycreate() as variable
                fkey = open('testdocs/filekey.night','rb')
                key = fkey.read()
                print (key)
                cipher = Fernet(key)
            
            #     opens created files to be encrypted and encrypts
            
            # >>>>>>>>>>>>>>>>>>>>>
                Nocfile= 'testdocs/noclist.night'
                with open(Nocfile,'rb')as e:
                    Nocfiletoencrypt = e.read()

                    
                Nocencryptedfile = cipher.encrypt(Nocfiletoencrypt) 
                with open(Nocfile,'wb') as ee:
                    ee.write(Nocencryptedfile)

                with open('testdocs/noclist.night','rb') as df:
                    encryptedfile = df.read()
                    print(encryptedfile)
                    print('>>>>>>>>>>>>>>>>>>>>>>>')
                decrypted_file = cipher.decrypt(encryptedfile)
                print(decrypted_file.decode())  
                filencrypter()



        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> creates data list file
        def listcreate():
        #     this creates txt files from list
            emplist.append(empname)

            with open(f'testdocs\\noclist.night',mode='w')as n:
                for m in range(len(emplist)):
                    n.write(f'{emplist[m]}\n')    
            with open(f'testdocs\\{empname}.night',mode='w')as t:
                for k in range(len(dataentered)):
                    t.write(f'{dataentered[k]}\n')
            with open(f'testdocs\\{empname}sickdates.night',mode='w')as q:
                for r in range(len(sickdatestart)):
                    q.write(f'{sickdatestart[r]}\n')
            with open(f'testdocs\\{empname}persdates.night',mode='w')as s:
                for y in range(len(persdatestart)):
                    s.write(f'{persdatestart[y]}\n')
            with open(f'testdocs\\{empname}vacdates.night',mode='w')as h:
                for j in range(len(vacdatestart)):
                    h.write(f'{vacdatestart[j]}\n')
            print('files created!')
            noclistencrypt()
        listcreate()





            
            
            
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> pay setter correction
    def paysettercorr():    
            paycorr = (input('enter rate per hour or enter salary in 00.00 format: '))
            if paycorr == '*':
                verifier()
            else:
                while True:
                    try:
                        paynocorr = float(paycorr)
                        paylistcorr = len(paycorr)
                        print(paynocorr)
                        print(paylistcorr)
                        if paylistcorr>=5 and paycorr[2]=='.':
                            hourlycorr = paynocorr
                            weeklycorr = paynocorr*40
                            monthlycorr = weeklycorr *4
                            yearlycorr = monthlycorr *12
                            print(f'gross pay weekly{hourlycorr}')
                            print(f'gross pay weekly{weeklycorr}')
                            print(f'gross pay monthly{monthlycorr}')
                            print(f'gross pay yearly{yearlycorr}')
                            dataentered[14] = (hourlycorr)
                            dataentered[15] = (weeklycorr)
                            dataentered[16] = (monthlycorr)
                            dataentered[17] = (yearlycorr)
                            verifier()
                        elif paylistcorr >= 8 and paycorr[5]=='.':
                            weeklycorr = paynocorr/52
                            hourlycorr = weeklycorr/40
                            monthlycorr = weeklycorr *4 
                            yearlycorr = paynocorr
                            print(f'gross pay weekly{hourlycorr}')
                            print(f'gross pay weekly{weeklycorr}')
                            print(f'gross pay monthly{monthlycorr}')
                            print(f'gross pay yearly{yearlycorr}')
                            dataentered[14] = (hourlycorr)
                            dataentered[15] = (weeklycorr)
                            dataentered[16] = (monthlycorr)
                            dataentered[17] = (yearlycorr)                        
                            verifier()
                        elif paylistcorr >= 9 and paycorr[6]=='.':
                            weeklycorr = paynocorr/52
                            hourlycorr = weeklycorr/40
                            monthlycorr = weeklycorr *4 
                            yearlycorr = paynocorr
                            print(f'gross pay weekly{hourlycorr}')
                            print(f'gross pay weekly{weeklycorr}')
                            print(f'gross pay monthly{monthlycorr}')
                            print(f'gross pay yearly{yearlycorr}')
                            dataentered[14] = (hourlycorr)
                            dataentered[15] = (weeklycorr)
                            dataentered[16] = (monthlycorr)
                            dataentered[17] = (yearlycorr)
                            verifier()
                        else:
                            print('noooooope')
                            paysetter()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        paysetter()
                        break
                    else:
                        break         
            
            
            
            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>position setter correction    
    def postsettercorr():            
        deptAcorr = depset[0]
        print(len(deptAcorr))
        choicercorr = (len(deptAcorr))
        positionchoosecorr= input("enter no. for position: ")
        if positionchoosecorr == '*':
            verifier()
        else:
            while True:
                try:
                    positionchoosercorr=int(positionchoosecorr)
                    if positionchoosercorr>=0 and positionchoosercorr<choicercorr:
                        positioncorr = depset[0][positionchoosercorr]
                        dataentered[13] = positioncorr
                        print(positioncorr)
                        verifier()
                    else:
                        print('Please pick a Number from the choices+++++')
                        postsettercorr()
                except ValueError:
                    print('Please pick a Number from the choices')
                    postsettercorr()
                    break
                else:
                    break




    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>department setter corrector    
    def depsettercorr():
        depset.clear()
        deptchoosecorr= input("enter no. for dept 0-Hskeeping, 1-Front Office, 2-Engineering, 3-PBX, 4-Sales, 5-Accting: ")
        if deptchoosecorr == '*':
            verifier()
        else:
            while True:
                try:
                    deptchoosercorr=int(deptchoosecorr)
                except:
                    print('Please pick a Number from the choices')
                    depsetter()
                    break
                else:
                    if deptchoosercorr == 0:
                        for h in range (len(hsk)):
                            print(f"{h}...{hsk[h]}")
                            dept = department[deptchoosercorr]
                            dataentered[11] = dept
                        break
                    if deptchoosercorr == 1:
                        for f in range (len(FD)):
                            print(f"{f}...{FD[f]}")
                            dept = department[deptchoosercorr]
                            dataentered[12] = dept
                        break
                    if deptchoosercorr == 2:        
                        for e in range (len(eng)):
                            print(f"{e}...{eng[e]}")
                            dept = department[deptchoosercorr]
                            dataentered[12] = dept
                        break
                    if deptchoosercorr == 3:
                        for p in range (len(pbx)):
                            print(f"{p}...{pbx[p]}")
                            dept = department[deptchoosercorr]
                            dataentered[12] = dept
                        break
                    if deptchoosercorr == 4:
                        for s in range (len(sle)):
                            print(f"{s}...{sle[s]}")
                            dept = department[deptchoosercorr]
                            dataentered[12] = dept
                        break
                    if deptchoosercorr == 5:
                        for a in range (len(acct)):
                            print(f"{a}...{acct[a]}")
                            dept = department[deptchoosercorr]
                            dataentered[12] = dept
                        break
                    else:
                        print('Please pick a Number from the choices***')
                        depsettercorr()
                        break
            deptS = departmentString[int(deptchoosecorr)]
            depset.append(dept)
            dataentered.append(deptS)
            postsettercorr()


           
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear correct for verif fucn  
    def hireYearcorr():
            hireYecorr = (input('enter 2 digit format of numerical year 00-99 pls: '))
            if hireYecorr == '*':
                verifier()
            else:
                while True:
                    try:
                        hireYenomcorr = int(hireYecorr) +2000
                        hireYelistcorr = len(str(hireYecorr))
                        print(hireYelistcorr)
                        if hireYelistcorr == 2 and  hireYenomcorr  <= int(yearnow):
                            dataentered[11]=hireYecorr
                            verifier()  
                        else:
                            print('nooooo')
                            hireYearcorr()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireYearcorr()
                        break
                    else:
                        break         
            
            
            
            
            
            
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireday   corrrector for verifierfucn       
    def hireDaycorr():
            hireDacorr = (input('enter numerical date 1-31 pls: '))
            if hireDacorr == '*':
                verifier()
            else:
                while True:
                    try:
                        hireDanomcorr = int(hireDacorr)
                        if len(hireDacorr)==2 and hireDanomcorr  > 0 and hireDanomcorr  < 32:
                            dataentered[10] = hireDacorr
                            verifier()
                        else:
                            print('nooooo')
                            hireDaycorr()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireDaycorr()
                        break
                    else:
                        break          
            
            
            


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth corrrector for verifierfucn   
    def hireMonthcorr():
            print('if youve entered the wrong no. enter * to choose again')
            hireMocorr = (input('enter 2 digit numerical month 01-12 pls: '))
            if hireMocorr == '*':
                verifier()
            else:
                while True:
                    try:
                        hireMonomcorr = int(hireMocorr)
                        hireMolistcorr = len(str(hireMocorr))
                        print(hireMolistcorr)
                        if hireMolistcorr == 2 and hireMonomcorr < 13:
                            dataentered[9] = hireMocorr
                            verifier()                        
                        else:
                            print('nooooo')
                            hireMonthcorr()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireMonthcorr()
                        break
                    else:
                        break       
            
                            
            
            
            
            
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zip  corrrector for verifierfucn    
    def zipnocorr():
            print('if youve entered the wrong no. enter * to choose again')
            zipnomicorr = (input('enter zip code in 12345 format pls: '))
            if zipnomicorr == '*':
                verifier()
            else:
                while True:
                    try:
                        zipnomcorr = int(zipnomicorr)
                        ziplistcorr = len(str(zipnomicorr))
                        print(ziplistcorr)
                        if ziplistcorr == 5:
                            dataentered[8] = zipnomcorr
                            verifier()
                        else:
                            print('nooooo')
                            zipnocorr()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        zipnocorr()
                        break
                    else:
                        break             
            


            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>state corrrector for verifierfucn
    def statecheckcorr():
        stabcorr = input('enter State name or other if not a state: ').upper()
        stateverify.clear()
        if stabcorr == '*':
            verifier()
        elif len(stabcorr)>2:
            for key in statedictionary:
                if key == stabcorr:
                    print(statedictionary[stabcorr])
                else:
                    stateverify.append(1)
            if sum(stateverify)==51:
                print('this aint no state')
                statecheckcorr()
            else:
                statentry = statedictionary[stabcorr]
                dataentered[7]=stabcorr
                verifier() 
        else:
            print(stabcorr)
            for z in range(len(stablist)):
                if stablist[z] == stabcorr:
                    print(stablist[z])
                else:
                    stateverify.append(1)
            if sum(stateverify)==51:
                print('this aint no state')
                statecheckcorr()
            else:
                dataentered[7]=stabcorr
                verifier()        

            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>telno corrrector for verifierfucn        
    def telnocorr():
            print('if youve entered the wrong no. enter * to choose again')
            telnomicorr = (input('enter tel no in 1234567890 format pls: '))
            if telnomicorr == '*':
                verifier()
            else:
                while True:
                    try:
                        telnomcorr = int(telnomicorr)
                        telistcorr = len(str(telnomicorr))
                        print(telistcorr)
                        if telistcorr == 10:
                            dataentered[4]=telnomcorr
                            verifier()
                        else:
                            print('nooooo')
                            telnocorr()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        telnocorr()
                        break
                    else:
                        break        
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssno for correction section
    def ssnocorr():
            print('if youve entered the wrong no. enter * to choose again')
            ssnomicorr = (input('enter ss no in 123456789 format pls: '))
            if ssnomicorr == '*':
                verifier()
            else:
                while True:
                    try:
                        ssnomcorr = int(ssnomicorr)
                        sslistcorr = len(str(ssnomcorr))
                        print(sslistcorr)
                        if sslistcorr == 9:
                            dataentered[3]=ssnomcorr
                            verifier()
                        else:
                            print('nooooo')
                            ssnocorr()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        ssnocorr()
                        break
                    else:
                        break           
            
            
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Verifier for Dataentered
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>correction entry
    def subverif():
        chooser = chosen[0]
        print("ok great let's edit!")
        print(f'{dataentered[chooser]} will now be edited. Enter new Info below')
        newentry = input('correction: ')
        dataentered[chooser] = newentry
        print(f'Info on line {chooser} has now been changed to {newentry}.')
        verifier()
     
    def readytosave():
        saver = input('save your entries enter (y) to save enter (n) to go back(<): ')
        if saver == 'y':
            newempfilesaver()
        elif saver == 'n':
            verifier
        else:
            readytosave()    
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>initial ask 
    def verifier():
        for x in range (len(dataentered)):
            print(f"{x} ... {dataentered[x]}")
        choose = input('enter (y) to confirm data or enter the no. of the line you wish to edit: ')
        if choose.lower() == 'y':
            dataentered.append(0)
            dataentered.append(0)
            dataentered.append(0)
            dataentered.append(0)
            dataentered.append(0)
            dataentered.append(0)
            print('input test done')
            print(dataentered)
            readytosave()

        elif choose == '0' or choose == '1' or choose == '2' or choose == '5' or choose == '6':
            print('if youve entered the wrong no. enter * to choose again')
            newentry = input('correction: ')
            if newentry == '*':
                verifier()
            elif len(newentry) == 0:
                print('cannot leave this blank')
                verifier()
            else:
                dataentered[int(choose)] = newentry
                print(f'Info on line {choose} has now been changed to {newentry}.')
                verifier()
        elif choose == '3':
            ssnocorr()
        elif choose == '4':
            telnocorr()
        elif choose == '7':
            statecheckcorr()
        elif choose == '8':
            zipnocorr()
        elif choose == '9':
            hireMonthcorr()
        elif choose == '10':
            hireDaycorr()
        elif choose == '11':
            hireYearcorr()
        elif choose == '12':
            depsettercorr()  
        elif choose == '13':
            currdep = depset[0]
            for a in range (len(currdep)):
                print(f"{a}...{currdep[a]}")
            postsettercorr()        
        elif choose == '14' or choose == '15' or choose == '16' or choose == '17':
            paysettercorr()
        else:
            print('incorrect data :(')
            verifier()
        
         
                 

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets pay    
    def paysetter():    
            pay = (input('enter rate per hour or enter salary in 00.00 format: '))
            if pay == '*':
                del dataentered[-1]
                postsetter()
            else:
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
                            dataentered.append(hourly)
                            dataentered.append(weekly)
                            dataentered.append(monthly)
                            dataentered.append(yearly)
                            verifier()
                        elif paylist>=8 and pay[5]=='.':
                            weekly = payno/52
                            hourly = weekly/40
                            monthly = weekly *4 
                            yearly = payno
                            print(f'gross pay hourly{hourly}')
                            print(f'gross pay weekly{weekly}')
                            print(f'gross pay monthly{monthly}')
                            print(f'gross pay yearly{yearly}')
                            dataentered.append(hourly)
                            dataentered.append(weekly)
                            dataentered.append(monthly)
                            dataentered.append(yearly)                        
                            verifier()
                        elif paylist>=9 and pay[6]=='.':
                            weekly = payno/52
                            hourly = weekly/40
                            monthly = weekly *4 
                            yearly = payno
                            print(f'gross pay hourly{hourly}')
                            print(f'gross pay weekly{weekly}')
                            print(f'gross pay monthly{monthly}')
                            print(f'gross pay yearly{yearly}')
                            dataentered.append(hourly)                        
                            dataentered.append(weekly)
                            dataentered.append(monthly)
                            dataentered.append(yearly)
                            verifier()
                        else:
                            print('noooooope')
                            paysetter()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        paysetter()
                        break
                    else:
                        break 
         
        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets position     
    def postsetter():            
        deptA = depset[0]
        print(len(deptA))
        choicer = (len(deptA))
        positionchoose= input("enter no. for position: ")
        if positionchoose == '*':
            del dataentered[-1]
            depsetter()
        else:
            while True:
                try:
                    positionchooser=int(positionchoose)
                    if positionchooser>=0 and positionchooser<choicer:
                        position = depset[0][positionchooser]
                        dataentered.append(position)
                        print(position)
                        paysetter()
                    else:
                        print('Please pick a Number from the choices+++++')
                        postsetter()
                except ValueError:
                    print('Please pick a Number from the choices')
                    postsetter()
                    break
                else:
                    break
        

                
        

        
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets department    
    def depsetter():
        depset.clear()
        deptchoose= input("enter no. for dept 0-Hskeeping, 1-Front Office, 2-Engineering, 3-PBX, 4-Sales, 5-Accting: ")
        if deptchoose == '*':
            del dataentered[-1]
            hiredate()
        else:
            while True:
                try:
                    deptchooser=int(deptchoose)
                except:
                    print('Please pick a Number from the choices')
                    depsetter()
                    break
                else:
                    if deptchooser == 0:
                        for h in range (len(hsk)):
                            print(f"{h}...{hsk[h]}")
                            dept = department[deptchooser]
                            depset.append(dept)
                        break
                    if deptchooser == 1:
                        for f in range (len(FD)):
                            print(f"{f}...{FD[f]}")
                            dept = department[deptchooser]
                            depset.append(dept)
                        break
                    if deptchooser == 2:        
                        for e in range (len(eng)):
                            print(f"{e}...{eng[e]}")
                            dept = department[deptchooser]
                            depset.append(dept)
                        break
                    if deptchooser == 3:
                        for p in range (len(pbx)):
                            print(f"{p}...{pbx[p]}")
                            dept = department[deptchooser]
                            depset.append(dept)
                        break
                    if deptchooser == 4:
                        for s in range (len(sle)):
                            print(f"{s}...{sle[s]}")
                            dept = department[deptchooser]
                            depset.append(dept)
                        break
                    if deptchooser == 5:
                        for a in range (len(acct)):
                            print(f"{a}...{acct[a]}")
                            dept = department[deptchooser]
                            depset.append(dept)
                        break
                    else:
                        print('Please pick a Number from the choices***')
                        depsetter()
                        break
            deptS = departmentString[int(deptchoose)]
            depset.append(dept)
            dataentered.append(deptS)
            postsetter()
            
              
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear    
    def hireYear():

            hireYe = (input('enter 2 digit format of year 00-99 pls: '))
            if hireYe == '*':
                del dataentered[-1]
                hireDay() 
            else:
                while True:
                    try:
                        hireYenom = int(hireYe) +2000
                        hireYelist = len(str(hireYe))
                        print(hireYelist)
                        if hireYelist == 2 and  hireYenom  <= int(yearnow):
                            dataentered.append(hireYe)
                            depsetter() 
                        else:
                            print('nooooo')
                            hireYear()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireYear()
                        break
                    else:
                        break         
         
        
        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireday     
    def hireDay():

            hireDa = (input('enter numerical 2 digit date 01-31 pls: '))
            if hireDa == '*':
                del dataentered[-1]
                hireMonth()
            else:
                while True:
                    try:
                        hireDanom = int(hireDa)
                        if len(hireDa)==2 and hireDanom  > 0 and hireDanom  < 32:
                            dataentered.append(hireDa)
                            hireYear()
                        else:
                            print('nooooo')
                            hireDay()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireDay()
                        break
                    else:
                        break     
        
        
        
        
        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth     
    def hireMonth():

            hireMo = (input('enter 2 digit numerical month 01-12 pls: '))
            if hireMo == '*':
                del dataentered[-1]
                hiredate()
            else:
                while True:
                    try:
                        hireMonom = int(hireMo)
                        if len(hireMo)==2 and hireMonom> 0 and hireMonom < 13:
                            dataentered.append(hireMo)
                            hireDay()
                        else:
                            print('nooooo')
                            hireMonth()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        hireMonth()
                        break
                    else:
                        break       
            
            
        
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiredate
    def hiredate():
        hirenow = input('is today the hiring day of the employee. 1 for yes Or any key for no: ')
        if hirenow == '*':
            del dataentered[-1]
            zipno()
        elif hirenow == '1':
            hiredM=str(monthnow)
            hiredD=str(daynow)
            hiredY=str(yearnow)
            currdate = hiredM +' '+ hiredD +' '+ hiredY
            dataentered.append(hiredM)
            dataentered.append(hiredD)
            dataentered.append(hiredY)
            print(currdate)
            depsetter() 
        else:
            hireMonth()
            


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zip      
    def zipno():

            zipnomi = (input('enter zip code in 12345 format pls: '))
            if zipnomi == '*':
                del dataentered[-1]
                statecheck()
            else:
                while True:
                    try:
                        zipnom = int(zipnomi)
                        ziplist = len(str(zipnomi))
                        print(ziplist)
                        if ziplist == 5:
                            dataentered.append(zipnom)
                            hiredate()
                        else:
                            print('nooooo')
                            zipno()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        zipno()
                        break
                    else:
                        break        
            
            
            
            

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>state
    def statecheck():
        stab = input('enter State name or other if not a state: ').upper()
        stateverify.clear()
        if stab == '*':
            del dataentered[-1]
            cityfun
        elif len(stab)>2:
            for key in statedictionary:
                if key == stab:
                    print(statedictionary[stab])
                else:
                    stateverify.append(1)
            if sum(stateverify)==51:
                print('this aint no state')
                statecheck()
            else:
                statentry = statedictionary[stab]
                dataentered.append(statentry)
                zipno()
        else:
            print(stab)
            for z in range(len(stablist)):
                if stablist[z] == stab:
                    print(stablist[z])
                else:
                    stateverify.append(1)
            if sum(stateverify)==51:
                print('this aint no state')
                statecheck()
            else:
                dataentered.append(stab)
                zipno()
                      
            
            


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>city    
    def cityfunc():
        city= input("city: ") 
        if city == '*':
            del dataentered[-1]
            address
        elif len(city) == 0:
            print('cannot leave this blank')
            cityfunc()    
        else:
            dataentered.append(city)
            statecheck()       
        
        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>street address      
    def address1():
        streetaddress= input("street address: ")    
        if streetaddress == '*':
            del dataentered[-1]
            telno()
     
        elif len(streetaddress) == 0:
            print('cannot leave this blank')
            address1()
        else:
            dataentered.append(streetaddress)
            cityfunc()  
                
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>telno
    def telno():

            telnomi = (input('enter tel no in 1234567890 format pls: '))
            if telnomi == '*':
                del dataentered[-1]
                ssno()
            else:
                while True:
                    try:
                        telnom = int(telnomi)
                        telist = len(str(telnomi))
                        print(telist)
                        if telist == 10:
                            dataentered.append(telnom)
                            address1()
                        else:
                            print('nooooo')
                            telno()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        telno()
                        break
                    else:
                        break        
                    
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssno
    def ssno():

            ssnomi = (input('enter ss no in 123456789 format pls: '))
            if ssnomi == '*':
                del dataentered[-1]
                nickname()

            else:
                while True:
                    try:
                        ssnom = int(ssnomi)
                        sslist = len(str(ssnom))
                        print(sslist)
                        if sslist == 9:
                            dataentered.append(ssnom)
                            telno()
                        else:
                            print('nooooo')
                            ssno()
                    except ValueError :
                        print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                        ssno()
                        break
                    else:
                        break        
            
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>nickname       
    def nickname():
        nickname= input("nickname: ")
        if nickname == '*':
            del dataentered[-1]
            lnameFunc()

        elif len(nickname) == 0:
            print('cannot leave this blank')
            nicknamefunc()
        else:
            dataentered.append(nickname)
            ssno()          
            
            
            
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>last name        
    def lnameFunc():
        print('if you have entered the wrong previous info, enter * to go back')
        lastname= input("last name: ")
        if lastname == '*':
            del dataentered[-1]
            fnameFunc()
        elif len(lastname) == 0:
            print('cannot leave this blank')
        else:
            dataentered.append(lastname)
            nickname()
            
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>first name       
    def fnameFunc():
        print('if you have entered the wrong mode, enter < to go back to mode select')
        firstname= input("first name: ")
        if len(firstname) == 0:
            print('cannot leave this blank')
            fnameFunc()
        elif firstname == '<':
            print('Are you sure ? Going Back to mode choice will erase all the data you have entered so far.')
            moderet= input('y for yes OR Any key for no: ')
            if moderet == 'y':
                modeset()
            else:
                fnameFunc()
        else:
            dataentered.append(firstname)
            lnameFunc()
    fnameFunc()
        


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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Bigeditinput():
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


    curremp=[]
    searchlist=[]
    notsearch=[]
    searchedpos=[]


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Editsavechanges():
        load = curremp[0]
        load2 = curremp[1]
        load3 = curremp[2]
        load4 = curremp[3]
        
        empnamer = curremp[0][0]+curremp[0][1]
        emplist[int(searchedpos[0])]= empnamer
        with open(f'testdocs\\noclist.night',mode='w')as n:
            for m in range(len(emplist)):
                n.write(f'{emplist[m]}\n')        
        
        with open(f'testdocs\\{empnamer}.night',mode='w')as t:
            for k in range(len(load)):
                t.write(f'{load[k]}\n')
        with open(f'testdocs\\{empnamer}sickdates.night',mode='w')as q:
            for r in range(len(load2)):
                q.write(f'{load2[r]}\n')
        with open(f'testdocs\\{empnamer}persdates.night',mode='w')as s:
            for y in range(len(load3)):
                s.write(f'{load3[y]}\n')
        with open(f'testdocs\\{empnamer}vacdates.night',mode='w')as h:
            for j in range(len(load4)):
                h.write(f'{load4[j]}\n')         
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


    # >>>>>>>>>>>>>>>>>>>>>          
        sickfileN= 'testdocs/'+ empnamer +'sickdates.night'
        with open(sickfileN,'rb')as ff:
            sickfileNtoencrypt = ff.read()

        sickencryptedfileN = cipher.encrypt(sickfileNtoencrypt) 
        with open(sickfileN,'wb') as eff:
            eff.write(sickencryptedfileN)


    # >>>>>>>>>>>>>>>>>>>>>          
        persfileN= 'testdocs/'+ empnamer +'persdates.night'
        with open(persfileN,'rb')as fff:
            persfileNtoencrypt = fff.read()

        persencryptedfileN = cipher.encrypt(persfileNtoencrypt) 
        with open(persfileN,'wb') as efff:
            efff.write(persencryptedfileN)


    # >>>>>>>>>>>>>>>>>>>>>      
        vacfileN= 'testdocs/'+ empnamer +'vacdates.night'
        with open(vacfileN,'rb')as ffff:
            vacfileNtoencrypt = ffff.read()

        vacencryptedfileN = cipher.encrypt(vacfileNtoencrypt) 
        with open(vacfileN,'wb') as effff:
            effff.write(vacencryptedfileN)

    #/////////////////////////////////////////////////////////////
        with open('testdocs/'+ empnamer +'.night','rb') as df:
            encryptedfileN = df.read()
            print(encryptedfileN)
            print('>>>>>>>>>>>>>>>>>>>>>>>')
        decrypted_fileN = cipher.decrypt(encryptedfileN)
        print(decrypted_fileN.decode())   
        EditMenu()

        
        

        





    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



    # >>>>>>>>>>>>>>>>>>>>>>>> logs and sickdays
    sickdays=[]
    sickentries=[0,0,0,0]
    curryr = []
    pastyr = []
    import datetime
    z=datetime.datetime.now()
    yearnow = (z.strftime("%Y"))

    def sickdayslog():
        yearnowsick = int(yearnow) - 2000
        yearstr = str(yearnowsick-1)
        sickdays.clear()
        curryr.clear()
        pastyr.clear()
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
                curremp[0][18] = len(curryr) + int(curremp[0][18])
                curremp[0][19] = int(curremp[0][19])-len(curryr)
                for d in range(len(curryr)):
                    curremp[1].append(curryr[d])
                for e in range(len(pastyr)):
                    curremp[1].append(pastyr[e])
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
                curremp[0][18] = len(curryr) + int(curremp[0][18])
                curremp[0][19] = int(curremp[0][19])-len(curryr)
                for d in range(len(curryr)):
                    curremp[1].append(curryr[d])
                for e in range(len(pastyr)):
                    curremp[1].append(pastyr[e])
                print('done!')
                Seditsaver = input('save your entries enter (y) to save enter (n) to go back to main menu: ')
                if Seditsaver == 'y':
                    Editsavechanges()
                elif Seditsaver == 'n':
                    EditMenu()
                else:
                    moresickentries() 
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
                elif sickamt == '<':
                    pass
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
                elif sickYe == '<':
                    EditMenu()
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
                    sickMonth()
                elif sickDa == '<':
                    EditMenu()
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
        def sickMonth():
                sickMo = (input('enter numerical month 1-12 pls: '))
                if sickMo == '*':
                    EditMenu()
                elif sickMo == '<':
                    modeset()
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
        sickMonth()










    # >>>>>>>>>>>>>>>>>>>>>>>> logs and personal days

    def persdayslog():
        persdays=[]
        persentries=[0,0,0,0]
        Pcurryr = []
        Ppastyr = []
        import datetime
        z=datetime.datetime.now()
        yearnow = (z.strftime("%Y"))
        yearnowpers = int(yearnow) - 2000
        yearnowperstr = str(yearnowpers-2)
        persdays.clear()    
        Pcurryr.clear()
        Ppastyr.clear()
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
                curremp[0][20] = len(Pcurryr) + int(curremp[0][20])
                curremp[0][21] = int(curremp[0][21])-len(Pcurryr)
                for d in range(len(Pcurryr)):
                    curremp[2].append(Pcurryr[d])
                for e in range(len(Ppastyr)):
                    curremp[2].append(Ppastyr[e])
                persdayslog()
            elif morent == 'n':
                for x in range(len(persdays)):
                    if persdays[x][-2]+persdays[x][-1] == yearnowperstr or persdays[x][-2]+persdays[x][-1] == str(yearnowpers):
                        Pcurryr.append(persdays[x])
                    else:
                        Ppastyr.append(persdays[x])
                print(len(Pcurryr))
                print(Pcurryr)
                print(Ppastyr)
                curremp[0][20] = len(Pcurryr) + int(curremp[0][20])
                curremp[0][21] = int(curremp[0][21])-len(Pcurryr)
                for d in range(len(Pcurryr)):
                    curremp[2].append(Pcurryr[d])
                for e in range(len(Ppastyr)):
                    curremp[2].append(Ppastyr[e])
                print('done!')
                Peditsaver = input('save your entries enter (y) to save enter (n) to go back to main menu: ')
                if Peditsaver == 'y':
                    Editsavechanges()
                elif Peditsaver == 'n':
                    EditMenu()
                else:
                    morepersentries() 
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
                elif persamt == '<':
                    pass
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
                elif persYe == '<':
                    pass
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
                    persMonth()
                elif persDa == '<':
                    pass
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
        def persMonth():
                persMo = (input('enter numerical month 1-12 pls: '))
                if persMo == '*':
                    EditMenu()
                elif persMo == '<':
                    modeset()
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
                                persMonth()
                        except ValueError :
                            print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                            persMonth()
                            break
                        else:
                            break
        persMonth()    



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




    # >>>>>>>>>>>>>>>>>>>>>>>> logs and vacdays

    def vacdayslog():
        vacdays=[]
        vacentries=[0,0,0,0]
        toremove=[]
        import datetime
        z=datetime.datetime.now()
        yearnow = (z.strftime("%Y"))
        yearnowvac = int(yearnow) - 2000
        vacdays.clear()
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
                curremp[0][22] = len(vacdays) + int(curremp[0][22])
                curremp[0][23] = int(curremp[0][23])-len(vacdays)
                for d in range(len(vacdays)):
                    curremp[3].append(vacdays[d])
                vacdayslog()
            elif morent == 'n':
                curremp[0][22] = len(vacdays) + int(curremp[0][22])
                curremp[0][23] = int(curremp[0][23])-len(vacdays)
                for d in range(len(vacdays)):
                    curremp[3].append(vacdays[d])
                print('done!')
                Veditsaver = input('save your entries enter (y) to save enter (n) to go back to main menu: ')
                if Veditsaver == 'y':
                    Editsavechanges()
                elif Veditsaver == 'n':
                    EditMenu()
                else:
                    morevacentries() 
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
                    vacDay()
                elif vacYe == '<':
                    pass
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
                elif vacDa == '<':
                    pass
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
                    EditMenu()
                elif vacMo == '<':
                    modeset()
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








    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







    def Mainsicpervac_Mtn():
        sickremove=[]
        PerPremove=[]
        Vacremove=[]

        sicdates=curremp[1]
        perdates=curremp[2]
        vacdates=curremp[3]   

        Sictoremove=[]
        Perstoremove=[]
        Vactoremove=[]

        def Vacdateremover():
            Vremover = input('enter the year of the dates you wish to remove: ')
            if Vremover == '*':
                sicpervac_mtn()
            elif (len(Vremover)) == 2:
                for Vremo in range(len(vacdates)):
                    if vacdates[Vremo][-2]+vacdates[Vremo][-1] == Vremover:
                        Vacremove.append(vacdates[Vremo])
                    else:
                        pass
                if (len(Vacremove)) > 0:
                    print('these are the dates you chose to remove')
                    for x in range(len(Vacremove)):
                        print(f'date to be removed .....{Vacremove[x]}')
                    
                    fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                    
                    if fwarn == 'y':
                        for Vlisted in range (len(Vacremove)):
                            vacdates.remove(Vacremove[Vlisted])
                        print(vacdates)
                        print('alldone! :)')
                        Editsavechanges()
                    elif fwarn =='n':
                        print('cool cool lets try again or you can type (*) to go back to the previous menu')
                        Vacdateremover()
                else:
                    print('sorry i did not find that year!Try again')
                    Vacdateremover()
            elif (len(Vremover)) == 1:
                Vremover1= '/'+Vremover
                for Vremo in range(len(vacdates)):
                    if vacdates[Vremo][-2]+vacdates[Vremo][-1] == Vremover1:
                        Vacremove.append(vacdates[Vremo])
                    else:
                        pass
                if (len(Vacremove)) > 0:
                    print('these are the dates you chose to remove')
                    for x in range(len(Vacremove)):
                        print(f'date to be removed .....{Vacremove[x]}')
                    
                    fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                    
                    if fwarn == 'y':
                        for Vlisted in range (len(Vacremove)):
                            vacdates.remove(Vacremove[Vlisted])
                        print(vacdates)
                    elif fwarn =='n':
                        print('cool cool lets try again or you can type (*) to go back to the previous menu')
                        Vacdateremover()
                else:
                    print('sorry i did not find that year!Try again')
                    Vacdateremover()
            elif remover == '*':
                morevacentries()
            else:
                print('sorry that is not on the list:)')
                dateremover()

                
                
        def specVac():
                Vactoremove.clear()
                datepicker = input('type the line no. of the date you wish to remove').lower()
                for dp in range(len(vacdates)):
                    if str(dp) == datepicker:
                        Vactoremove.append(vacdates[dp])
                        print('got it')
                    else:
                        pass
                if len(Vactoremove)>0:
                    ffwarn = input(f' the  date {Vactoremove} will now be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ').lower()
                    if ffwarn == 'y':
                        vacdates.pop(int(datepicker))
                        for sd in range(len(vacdates)):
                            print(f'{sd}.....{vacdates[sd]}')
                        curremp[0][22] = int(curremp[0][22]) - 1
                        curremp[0][23] = int(curremp[0][23]) + 1
                        print(f'{curremp[0][0]} {curremp[0][1]} has regained 1 Vacday')
                        print('great! that is done you can enter another date or type (*) to go back to the previous menu or type (s) to save your changes')
                        specVac()
                    elif ffwarn == 'n':
                        print('ok cool you can enter another date or type (*) to go back to the previous menu')
                        specVac()
                elif datepicker == '*':
                    Vacdatechoice()
                elif datepicker == 's':        
                    Editsavechanges()
                else:
                    print('sorry I could not find the date let me try another date or type (*) to go back to the previous menu')
                    specVac()    
                        
                
                
        def Vacdatechoice():
            for sd in range(len(vacdates)):
                print(f'{sd}.....{vacdates[sd]}')
            schoice= input('type (1) to remove a specific date or type (2) to remove all dates from a specific year or  type (*) to go back to the previous menu: ')
            if schoice == '1':
                specVac()
            elif schoice =='2':
                Vacdateremover()
            elif schoice == '*':
                sicpervac_mtn()
            else:
                print('beep boop beep does not compute beep boop beep try again!')
                Vacdatechoice()
        def Persdateremover():
            Premover = input('enter the year of the dates you wish to remove: ')
            if Premover == '*':
                sicpervac_mtn()
            elif (len(Premover)) == 2:
                for Premo in range(len(perdates)):
                    if perdates[Premo][-2]+perdates[Premo][-1] == Premover:
                        PerPremove.append(perdates[Premo])
                    else:
                        pass
                if (len(PerPremove)) > 0:
                    print('these are the dates you chose to remove')
                    for x in range(len(PerPremove)):
                        print(f'date to be removed .....{PerPremove[x]}')
                    
                    fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                    
                    if fwarn == 'y':
                        for Plisted in range (len(PerPremove)):
                            perdates.remove(PerPremove[Plisted])
                        print(perdates)
                        print('alldone! :)')
                        Editsavechanges()
                    elif fwarn =='n':
                        print('cool cool lets try again or you can type (*) to go back to the previous menu')
                        Persdateremover()
                else:
                    print('sorry i did not find that year!Try again')
                    Persdateremover()
            elif (len(Premover)) == 1:
                Premover1= '/'+Premover
                for Premo in range(len(perdates)):
                    if perdates[Premo][-2]+perdates[Premo][-1] == Premover1:
                        PerPremove.append(perdates[Premo])
                    else:
                        pass
                if (len(PerPremove)) > 0:
                    print('these are the dates you chose to remove')
                    for x in range(len(PerPremove)):
                        print(f'date to be removed .....{PerPremove[x]}')
                    
                    fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                    
                    if fwarn == 'y':
                        for Plisted in range (len(PerPremove)):
                            perdates.remove(PerPremove[Plisted])
                        print(perdates)
                    elif fwarn =='n':
                        print('cool cool lets try again or you can type (*) to go back to the previous menu')
                        Persdateremover()
                else:
                    print('sorry i did not find that year!Try again')
                    Persdateremover()
            elif remover == '*':
                morevacentries()
            else:
                print('sorry that is not on the list:)')
                dateremover()

                
                
        def specPers():
                Perstoremove.clear()
                datepicker = input('type the line no. of the date you wish to remove').lower()
                for dp in range(len(perdates)):
                    if str(dp) == datepicker:
                        Perstoremove.append(perdates[dp])
                        print('got it')
                    else:
                        pass
                if len(Perstoremove)>0:
                    ffwarn = input(f' the  date {Perstoremove} will now be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ').lower()
                    if ffwarn == 'y':
                        perdates.pop(int(datepicker))
                        for sd in range(len(perdates)):
                            print(f'{sd}.....{perdates[sd]}')
                        curremp[0][20] = int(curremp[0][20]) - 1
                        curremp[0][21] = int(curremp[0][21]) + 1
                        print(f'{curremp[0][0]} {curremp[0][1]} has regained 1 Persday')
                        print('great! that is done you can enter another date or type (*) to go back to the previous menu or type (s) to save your changes')
                        specPers()
                    elif ffwarn == 'n':
                        print('ok cool you can enter another date or type (*) to go back to the previous menu')
                        specPers()
                elif datepicker == '*':
                    Persdatechoice()
                elif datepicker == 's':        
                    Editsavechanges()
                else:
                    print('sorry I could not find the date let me try another date or type (*) to go back to the previous menu')
                    specPers()    
                        
                
                
        def Persdatechoice():
            for sd in range(len(perdates)):
                print(f'{sd}.....{perdates[sd]}')
            schoice= input('type (1) to remove a specific date or type (2) to remove all dates from a specific year or  type (*) to go back to the previous menu: ')
            if schoice == '1':
                specPers()
            elif schoice =='2':
                Persdateremover()
            elif schoice == '*':
                sicpervac_mtn()
            else:
                print('beep boop beep does not compute beep boop beep try again!')
                Persdatechoice()
        def sickdateremover():
            Sremover = input('enter the year of the dates you wish to remove: ')
            if Sremover == '*':
                sicpervac_mtn()
            elif (len(Sremover)) == 2:
                for Sremo in range(len(sicdates)):
                    if sicdates[Sremo][-2]+sicdates[Sremo][-1] == Sremover:
                        sickremove.append(sicdates[Sremo])
                    else:
                        pass
                if (len(sickremove)) > 0:
                    print('these are the dates you chose to remove')
                    for x in range(len(sickremove)):
                        print(f'date to be removed .....{sickremove[x]}')
                    
                    fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                    
                    if fwarn == 'y':
                        for Slisted in range (len(sickremove)):
                            sicdates.remove(sickremove[Slisted])
                        print(sicdates)
                        print('alldone! :)')
                        Editsavechanges()
                    elif fwarn =='n':
                        print('cool cool lets try again or you can type (*) to go back to the previous menu')
                        sickdateremover()
                else:
                    print('sorry i did not find that year!Try again')
                    sickdateremover()
            elif (len(Sremover)) == 1:
                Sremover1= '/'+Sremover
                for Sremo in range(len(sicdates)):
                    if sicdates[Sremo][-2]+sicdates[Sremo][-1] == Sremover1:
                        sickremove.append(sicdates[Sremo])
                    else:
                        pass
                if (len(sickremove)) > 0:
                    print('these are the dates you chose to remove')
                    for x in range(len(sickremove)):
                        print(f'date to be removed .....{sickremove[x]}')
                    
                    fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                    
                    if fwarn == 'y':
                        for Slisted in range (len(sickremove)):
                            sicdates.remove(sickremove[Slisted])
                        print(sicdates)
                    elif fwarn =='n':
                        print('cool cool lets try again or you can type (*) to go back to the previous menu')
                        sickdateremover()
                else:
                    print('sorry i did not find that year!Try again')
                    sickdateremover()
            elif remover == '*':
                morevacentries()
            else:
                print('sorry that is not on the list:)')
                dateremover()

                
                
        def specsick():
                Sictoremove.clear()
                datepicker = input('type the line no. of the date you wish to remove').lower()
                for dp in range(len(sicdates)):
                    if str(dp) == datepicker:
                        Sictoremove.append(sicdates[dp])
                        print('got it')
                    else:
                        pass
                if len(Sictoremove)>0:
                    ffwarn = input(f' the  date {Sictoremove} will now be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ').lower()
                    if ffwarn == 'y':
                        sicdates.pop(int(datepicker))
                        for sd in range(len(sicdates)):
                            print(f'{sd}.....{sicdates[sd]}')
                        curremp[0][18] = int(curremp[0][18]) - 1
                        curremp[0][19] = int(curremp[0][19]) + 1
                        print(f'{curremp[0][0]} {curremp[0][1]} has regained 1 sickday')
                        print('great! that is done you can enter another date or type (*) to go back to the previous menu or type (s) to save your changes')
                        specsick()
                    elif ffwarn == 'n':
                        print('ok cool you can enter another date or type (*) to go back to the previous menu')
                        specsick()
                elif datepicker == '*':
                    sickdatechoice()
                elif datepicker == 's':        
                    Editsavechanges()
                else:
                    print('sorry I could not find the date let me try another date or type (*) to go back to the previous menu')
                    specsick()    
                        
                
                
        def sickdatechoice():
            for sd in range(len(sicdates)):
                print(f'{sd}.....{sicdates[sd]}')
            schoice= input('type (1) to remove a specific date or type (2) to remove all dates from a specific year or  type (*) to go back to the previous menu: ')
            if schoice == '1':
                specsick()
            elif schoice =='2':
                sickdateremover()
            elif schoice == '*':
                sicpervac_mtn()
            else:
                print('beep boop beep does not compute beep boop beep try again!')
                sickdatechoice()


                
        def sicpervac_mtn():
            for s in range(len(sicdates)):
                print(f'Sick date: {sicdates[s]}')
            for p in range(len(perdates)):
                print(f'Personal date: {perdates[p]}')
            for v in range(len(vacdates)):
                print(f'Vacation date: {vacdates[v]}')
            
            mtnchoice = input('pls choose which set you would like to edit.\nEnter: (1) for sickdates (2) for personal dates (3) for vacation dates: ')
            if mtnchoice == '*':
                EditMenu()
            elif mtnchoice == '1':
                sickdatechoice()
            elif mtnchoice == '2':
                Persdatechoice()
            elif mtnchoice == '3':
                Vacdatechoice()
            else:
                print('that is not on the list')
                sicpervac_mtn()
        sicpervac_mtn()


    def EditMenu():
        wachuwant= input('if you would like to edit the employee information enter (i)\nif you would like to input\nsick days enter (s)\npersonal days enter (p)\nvacation days enter (v)\nIf you would like to edit the list of days taken enter (m)\nOr If you wish to go to the main menu enter (*)\nOR if you wish to save your current changes enter (sv): ').lower()
        if wachuwant == 'i':
            infolog()
        if wachuwant == 's':
            sickdayslog()
        elif wachuwant == 'p':
            persdayslog()
        elif wachuwant == 'v':
            vacdayslog()
        elif wachuwant == 'm':
            Mainsicpervac_Mtn()
        elif wachuwant == '*':
            modeset()
        elif wachuwant == 'sv':
            Editsavechanges()
        else:
            print('sorry that was not a choice!')
            EditMenu()





    def editinput():
        searcher= input('employee name:')
        for k in range(len(emplist)):
            if searcher == emplist[k]:
                searchlist.append(emplist[k])
                searchedpos.append(k)
            else:
                notsearch.append(emplist[k])
        if len(searchlist) == 1:
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

            with open('testdocs/'+search+'sickdates.night','rb') as ms:
                encryptedfileB = ms.read()
            decrypted_fileB = cipher.decrypt(encryptedfileB)

            with open('testdocs/'+search+'persdates.night','rb') as lm:
                encryptedfileC = lm.read()
            decrypted_fileC = cipher.decrypt(encryptedfileC)

            with open('testdocs/'+search+'vacdates.night','rb') as nh:
                encryptedfileD = nh.read()
            decrypted_fileD = cipher.decrypt(encryptedfileD)

            load = (decrypted_fileA.decode()).splitlines() 
            load2 = (decrypted_fileB.decode()).splitlines() 
            load3 = (decrypted_fileC.decode()).splitlines() 
            load4 = (decrypted_fileD.decode()).splitlines() 
            print(load)
            curremp.append(load)
            print(load2)
            curremp.append(load2)
            print(load3)
            curremp.append(load3)
            print(load4)
            curremp.append(load4)
            for reader in range(len(load)):
                if reader==0:
                    print(f'{[reader]}>>>firstname:.....{load[reader]}')
                elif reader==1:
                    print(f'{[reader]}>>>lastname:......{load[reader]}')
                elif reader==2:
                    print(f'{[reader]}>>>socno:......{load[reader]}')
                elif reader==3:
                    print(f'{[reader]}>>>telno:......{load[reader]}')
                elif reader==4:
                    print(f'{[reader]}>>>email:......{load[reader]}')
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
            for reader in range(len(load2)):
                if reader==0:
                    print(f'{[reader]}>>>sick dates:......{load2}')
            for reader in range(len(load3)):
                if reader==0:
                    print(f'{[reader]}>>>personal dates:......{load3}')
            for reader in range(len(load4)):
                if reader==0:
                    print(f'{[reader]}>>>vacation dates:......{load4}')
            print(curremp)
            EditMenu()
        elif searcher == '*':
            modeset()
        else:
            print('employee not found!')
            editinput()
    editinput()        
        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    



#_____________________________________________________________________________________________________________

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>mode select
def modeset():
    mission = input("1 for entry or 2 for output: ")
    if mission== '1':
        print("A new employee! coo'coo :)")
        Ndataenter()
    elif mission== '2':
        Bigeditinput()
        #run search function for editing employee info
    elif mission == '3':
        quit()
    else:
        print('boopbeep Error!')
        modeset()

modeset()