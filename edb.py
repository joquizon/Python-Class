from newEmpdataFuncsModule import fnameFunc
from newEmpdataFuncsModule import lnameFunc
from newEmpdataFuncsModule import nickname
from newEmpdataFuncsModule import ssno
from newEmpdataFuncsModule import telno
from newEmpdataFuncsModule import address1
from newEmpdataFuncsModule import statedictionary
from newEmpdataFuncsModule import stablist
from newEmpdataFuncsModule import stateverify
from newEmpdataFuncsModule import cityfunc
from newEmpdataFuncsModule import statecheck
from newEmpdataFuncsModule import zipno
from newEmpdataFuncsModule import hiredate
from newEmpdataFuncsModule import depsetter
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> state verfication dict and list and utility list for loops
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list that collects input data
dataentered=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
NdataFunclist = [fnameFunc,lnameFunc,nickname,ssno,telno,address1,cityfunc,statecheck,zipno]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>time variables for time based funcs
import datetime
z=datetime.datetime.now()
monthnow = int((z.strftime("%m")))
daynow = int((z.strftime("%d")))
yearnow = int((z.strftime("%Y")))-2000
print(monthnow)
print(daynow)
print(yearnow)
hireY=1
hiredD=1
hiredM=1
x=datetime.datetime(hireY,hiredD,hiredM)


depset=[0]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sickday persday vacday listcreator
sickdatestart =[]
persdatestart =[]
vacdatestart =[]

def Ndataenter():
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
                with open('el.py') as infile:
                    exec(infile.read())


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
                        hireYenomcorr = int(hireYecorr)
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
                        if int(dataentered[11]) < yearnow and len(hireDacorr)==2 and hireDanomcorr  > 0 and hireDanomcorr  < 32:
                            dataentered[10] = hireDacorr
                            verifier()
                        elif int(dataentered[11]) == yearnow and int(dataentered[9])< int(monthnow) and len(hireDacorr)==2 and hireDanomcorr  > 0 and hireDanomcorr  < 32:
                            dataentered[10] = hireDacorr
                            verifier()
                        elif int(dataentered[11]) == yearnow and int(dataentered[9])== int(monthnow) and len(hireDacorr)==2 and hireDanomcorr  > 0 and hireDanomcorr <= int(daynow):
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
                        if int(dataentered[11]) < yearnow and hireMolistcorr == 2 and hireMonomcorr < 13:
                            dataentered[9] = hireMocorr
                            verifier() 
                        elif int(dataentered[11]) == yearnow and hireMonomcorr<= int(monthnow) and hireMolistcorr == 2 and hireMonomcorr < 13:
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
            verifier()
        elif saver =='<':
            print('going back to the main menu will erase all the data you have entered!!! Are you sure?')
            returner = input('type (y) for yes or (n) for no: ')
            if returner == "y":
                with open('el.py') as infile:
                    exec(infile.read())
            elif returner == 'n':
                readytosave()
            else:
                print('let us try that again')
                readytosave()
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
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>first name     
    fnameFunc(dataentered,0,NdataFunclist,modeset)        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>last name        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>nickname           
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssno      
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>telno
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>street address      
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>city    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>state
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zip
    hiredate(monthnow,daynow,yearnow,dataentered,9,10,11,NdataFunclist)           
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireday     
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth     
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear 
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets department   






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
        depsetter(dataentered,depset)
    elif mission == '3':
        pass
    elif mission == '4':
        quit()
    else:
        print('boopbeep Error!')
        modeset()

modeset()