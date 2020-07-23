
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
                dataentered[7]=statentry
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
        editinFo()
    elif mission == '4':
        quit()
    else:
        print('boopbeep Error!')
        modeset()