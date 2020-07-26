from newEmpdataFuncsModule import fnameFunc
from newEmpdataFuncsModule import lnameFunc
from newEmpdataFuncsModule import nicknameFunc
from newEmpdataFuncsModule import ssno
from newEmpdataFuncsModule import telno
from newEmpdataFuncsModule import address1
from newEmpdataFuncsModule import cityfunc
from newEmpdataFuncsModule import statecheck
from newEmpdataFuncsModule import zipno
from newEmpdataFuncsModule import firstset
from newEmpdataFuncsModule import hiredate
from newEmpdataFuncsModule import depsetter
from newEmpdataFuncsModule import paysetter





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> state verfication dict and list and utility list for loops
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list that collects input data
dataentered=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
    
         
        

    
                
        

        
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets department    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>first name     
    firstset(dataentered,modeset)        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>last name        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>nickname           
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ssno      
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>telno
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>street address      
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>city    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>state
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zip
    hiredate(monthnow,daynow,yearnow,dataentered)           
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireday     
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth     
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear 
    depsetter(dataentered,depset)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets department   
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets position  
    paysetter(dataentered)   
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets pay





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
        paysetter(dataentered)
    elif mission == '3':
        hiredate(monthnow,daynow,yearnow,dataentered)
    elif mission == '4':
        quit()
    else:
        print('boopbeep Error!')
        modeset()
modeset()