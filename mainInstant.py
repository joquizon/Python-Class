import datetime
z=datetime.datetime.now()
monthnow = int((z.strftime("%m")))
yearnow = (z.strftime("%Y"))
yearint = (int(yearnow))-2000
print(monthnow)
print(yearnow)
print(yearint)

# zipped dict
obdict = 0
noclistkey=[]
dictionaryhold = []


# this file is used annual functions to be run. new yr ret True updates file and save
# if true every employee is given an additional 3 personal days
def yearcheck():
    from cryptography.fernet import Fernet
    fkey = open('testdocs/filekey.night','rb')
    key = fkey.read()
    cipher = Fernet(key)   
    
    with open('testdocs/yearstore.night','rb') as ys:
        encryptedfileA = ys.read()
    decrypted_fileA = cipher.decrypt(encryptedfileA)
    yearstore = (decrypted_fileA.decode())
    
    if int(yearstore) == yearint:
        print(f"Year check done")
    else:
        print(f"it is now the year 20{yearint}")
        
        with open(f'testdocs\\yearstore.night',mode='w')as n:
            n.write(f'{yearint}')  
            # print('files created!')
            
        yearstorefile= 'testdocs/yearstore.night'
        with open(yearstorefile,'rb')as e:
            yearstorefiletoencrypt = e.read()
    
        yearstoreencryptedfile = cipher.encrypt(yearstorefiletoencrypt) 
        with open(yearstorefile,'wb') as ee:
            ee.write(yearstoreencryptedfile)
            # print('file encryted')   
        return True
        for key in range(len(dictionaryhold)):
            z=dictionaryhold[key]['first'] + dictionaryhold[key]['last']
            d = dictionaryhold[key]['persremaining']
            d = int(d) + 3
            print(f' it is a new year {z} has 3 additional personal days')

# this file is used  functions to be run every 2 mos. if its been 2 mos. ret True update file and save
# if true employees are given 1 additional sickday
def everytwocheck():   
    from cryptography.fernet import Fernet
    fkey = open('testdocs/filekey.night','rb')
    key = fkey.read()
    cipher = Fernet(key)   
    
    with open('testdocs/sickrun.night','rb') as ys:
        encryptedfileSR = ys.read()
    decrypted_fileSR = cipher.decrypt(encryptedfileSR)
    sickrun = (decrypted_fileSR.decode())
    print(sickrun)
    if int(sickrun) == 12:
        newsick = 2
        with open(f'testdocs\\sickrun.night',mode='w')as s:
            s.write(f'{newsick}')  
            print('files created!')
            
        sickrunfile = 'testdocs/sickrun.night'
        with open(sickrunfile,'rb')as e:
            sickrunfiletoencrypt = e.read()
    
        sickrunencryptedfile = cipher.encrypt(sickrunfiletoencrypt) 
        with open(sickrunfile,'wb') as ee:
            ee.write(sickrunencryptedfile)
            print('file encryted')
        return True
        for key in range(len(dictionaryhold)):
            u=dictionaryhold[key]['first']+' '+dictionaryhold[key]['last']
            v = dictionaryhold[key]['sickremaining']
            dictionaryhold[key]['sickremaining'] = int(v) + 1
            w=dictionaryhold[key]['sickremaining']
            print(f' {u} has {w} remaining sick days')
    
    elif int(sickrun) == 11:
        newsick = 1
        with open(f'testdocs\\sickrun.night',mode='w')as s:
            s.write(f'{newsick}')  
            print('files created!')
            
        sickrunfile = 'testdocs/sickrun.night'
        with open(sickrunfile,'rb')as e:
            sickrunfiletoencrypt = e.read()
    
        sickrunencryptedfile = cipher.encrypt(sickrunfiletoencrypt) 
        with open(sickrunfile,'wb') as ee:
            ee.write(sickrunencryptedfile)
            print('file encryted')
        return True
        for key in range(len(dictionaryhold)):
            u=dictionaryhold[key]['first']+' '+dictionaryhold[key]['last']
            v = dictionaryhold[key]['sickremaining']
            dictionaryhold[key]['sickremaining'] = int(v) + 1
            w=dictionaryhold[key]['sickremaining']
            print(f' {u} has {w} remaining sick days')
            
    elif int(sickrun) == monthnow:
        newsick = int(sickrun) + 2
        with open(f'testdocs\\sickrun.night',mode='w')as s:
            s.write(f'{newsick}')  
            print('files created!')
            
        sickrunfile = 'testdocs/sickrun.night'
        with open(sickrunfile,'rb')as e:
            sickrunfiletoencrypt = e.read()
    
        sickrunencryptedfile = cipher.encrypt(sickrunfiletoencrypt) 
        with open(sickrunfile,'wb') as ee:
            ee.write(sickrunencryptedfile)
            print('file encryted')
        return True
        for key in range(len(dictionaryhold)):
            u=dictionaryhold[key]['first']+' '+dictionaryhold[key]['last']
            v = dictionaryhold[key]['sickremaining']
            dictionaryhold[key]['sickremaining'] = int(v) + 1
            w=dictionaryhold[key]['sickremaining']
            print(f' {u} has {w} remaining sick days')
    
    else:
        print('falseret')
        return False
    
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      

class Employee:
    def __init__(self,first,last,nickname,social,contel,address,city,state,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates,empnoyrs):
        self.first = first
        self.last = last
        self.nickname = nickname
        self.social = social
        self.contel = contel
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode 
        self.hiremonth = hiremonth     
        self.hiredate = hiredate
        self.hireyear = hireyear
        self.dept = dept
        self.position = position
        self.hourlypay = hourlypay
        self.weeklypay= weeklypay
        self.monthlypay= monthlypay
        self.yearlypay= yearlypay
        self.sicktaken = sicktaken
        self.sickremaining = sickremaining
        self.perstaken = perstaken
        self.persremaining = persremaining
        self.vactaken = vactaken
        self.vacremaining = vacremaining
        self.sickdates = sickdates
        self.persdates = persdates
        self.vacdates = vacdates
        self.empnoyrs = empnoyrs
        self.hdatecombo = int(hireyear+hiremonth+hiredate)
        
        
        
        


    # class method to give employees login or email usernames
    def emailgen(self,dom):
        companydomain = '@' + dom
        email = self.first+self.last+companydomain
        email2 = self.nickname+self.last[0]+companydomain
        email3 = self.first[0]+self.last+companydomain
        email4 = self.first+self.contel[-4:]+companydomain
        email5 = self.first+self.last[0]+companydomain
        
        print(f"possible email addresses generated:\n{email}\n{email2}\n{email3}\n{email4}\n{email5}")   
    


    def termlogingen(self):
        terminal = self.first+self.last
        terminal2 = self.nickname+self.last[0]
        terminal3 = self.first[0]+self.last
        terminal4 = self.first+self.contel[-4:]
        terminal5 = self.first+self.last[0]
        
        print(f"possible terminal logins generated:\n{terminal}\n{terminal2}\n{terminal3}\n{terminal4}\n{terminal5}")






    # class method to give employees categ based on hiredate
    def empstatus(self):
        import datetime
        z=datetime.datetime.now()
        monthnow = (z.strftime("%m"))
        daynow = (z.strftime("%d"))
        yearnow = (z.strftime("%Y"))
        yeardbl = str((int(yearnow))-2000)
        x = int(yeardbl+monthnow+daynow)
        probie = x - self.hdatecombo
        if probie < 300:
            print('Probation Period')
        elif probie>300 and probie<10000:
            print('Rookie')
        elif probie>10000 and probie<30000:
            print('Vet')
        elif probie>30000 and probie<50000:
            print('Bronze')
        elif probie>50000 and probie<100000:
            print('Silver')
        else:
            print('Gold')




    # class method to give notice if employee is up for review
    def annivCheck(self):
        import datetime
        z=datetime.datetime.now()
        monthnow = (z.strftime("%m"))
        daynow = (z.strftime("%d"))
        yearnow = (z.strftime("%Y"))
        yearint = (int(yearnow))-2000
        monthint= int(monthnow)
        dayint = int(daynow)
        
        if int(self.hireyear) < yearint:
            if int(self.hiremonth) < monthint:
                print("Time to Review / Raise")
                return True
            elif int(self.hiremonth) == monthint:
                if int(self.hiredate) <= dayint:
                    print("Time to Review / Raise")
                    return True
                else:
                    print(f'{int(self.hiredate) - dayint} day(s) away from Review and / or Raise')
                    return False        
            else:
                print(f'{int(self.hiremonth) - monthint} month(s) away from Review and / or Raise')
                return False
        else:
            print('not yet')





    # class method to give employees additional personal days on new calendar year this needs to run a loop and
#     check every employee at each instantiation... this is not for the query of indiv, employee. write a sep func for that
#     def persadd(self,odc):
#         nextyear = yearcheck()
#         if nextyear == True:
#             for key in odc:
#                 self.persremaining = int(self.persremaining) + 3
#                 print(f'{self.first} has {self.persremaining} personal days')
#         else:
#             print(f' it is still {yearnow} so no new personal days have been added ')

def persaddX():
    nextyear = yearcheck()
    if nextyear == True:
        for key in range(len(dictionaryhold)):
            z=dictionaryhold[key]['first']
            d = dictionaryhold[key]['persremaining']
            d = int(d) + 3
            print(f' it is a new year {z} has 3 additional personal days')
    else:
        print('same brah')

            
            
def EmployeeCreate(nlist,nmlist):
    for x in range(len(nlist)):
        z = x * 4
        first = nmlist[z][0]
        last = nmlist[z][1] 
        nickname = nmlist[z][2] 
        social = nmlist[z][3] 
        contel = nmlist[z][4] 
        address = nmlist[z][5]
        city =nmlist[z][6]
        state =nmlist[z][7] 
        zipcode  = nmlist[z][8]
        hiremonth = nmlist[z][9]
        hiredate = nmlist[z][10]
        hireyear = nmlist[z][11]
        dept = nmlist[z][12]
        position = nmlist[z][13]
        hourlypay = nmlist[z][14]
        weeklypay = nmlist[z][15]
        monthlypay = nmlist[z][16]
        yearlypay = nmlist[z][17]
        sicktaken = nmlist[z][18]
        sickremaining = nmlist[z][19]
        perstaken = nmlist[z][20]
        persremaining = nmlist[z][21]
        vactaken = nmlist[z][22]
        vacremaining = nmlist[z][23]
        empnoyears = nmlist[z][24]
        sickdates = nmlist[z+1]
        persdates = nmlist[z+2]
        vacdates = nmlist[z+3]
        hdatecombo =nmlist[z][11]+hiremonth+nmlist[z][9]+nmlist[z][10]
        
        nlist[x] = Employee(first,last,nickname,social,contel,address,city,state,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates,empnoyears)
        print(f'employee {nlist[x]} has been instantiated')
    for dt in range(len(nlist)):
        dictionaryhold.append(nlist[dt].__dict__)
    print(dictionaryhold)

def instantiation(nlist,nmlist):
    yearcheck()
    everytwocheck()
    EmployeeCreate(nlist,nmlist)
    for x in range(len(dictionaryhold)):
        noclistkey.append(dictionaryhold[x]['first']+dictionaryhold[x]['last'])
    print(noclistkey)
    obdict=dict(zip(noclistkey,nlist))


# ignition func --- this starts instantiation 
def OOPstart(nlist,nmlist):
    instantiation(nlist,nmlist)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# THIS IS WHERE THE INDIVIDUAL FUNCTIONS BEGIN --- MENU CHOICE 1 FROM OBJECTMENU()
def specfuncMenu(empname,position,nlist,retfunc):
    def submenu(empname,position,nlist,retfunc):
        print(f'\n>>>>>>>>>>>>>>>>>>>>>\n>>>>>>>>>>>>>>>>>>>>>\n>>>>>>>>>>>>>>>>>>>>>\nWhat would you like to do now ? ')
        newchoice = input(f'\nTo try a new task with {empname} enter ... <y>\nTo search another Employee ... <*>\nTo QUIT and return to the main menu enter ... <q>:\n')
        if newchoice == '*':
            print('ok cool\n>>>>>>>>>>>>>>>>>>>>>\n>>>>>>>>>>>>>>>>>>>>>\n>>>>>>>>>>>>>>>>>>>>>\n')
            quickempcheckMenu(nlist,retfunc)
        elif newchoice == 'q':
            retfunc()
        elif newchoice == 'y':
            print(f'ok cool\n>>>>>>>>>>>>>>>>>>>>>\n>>>>>>>>>>>>>>>>>>>>>\n>>>>>>>>>>>>>>>>>>>>>\n')
            specfuncMenu(empname,position,nlist,retfunc)
        else:
            print('beepboop... does not compute! try again :(')
            submenu(empname,position,nlist,retfunc)
        
    empquery = input(f'To view {empname}-s entire record enter ... <r>\nTo generate an email address for {empname} enter ... < 1 >\nTo generate Terminal login for {empname} enter ... < 2 >\nTo find out the tenure status of {empname} enter ... < 3 >\nTo find out if {empname} is due for a raise enter ... < 4 >\nFor the previous menu enter ... <*>\nTo QUIT and return to the main menu enter ... <q>:')
    if empquery == '*':
        quickempcheckMenu(nlist,retfunc)
    elif empquery == 'q':
        retfunc()
    elif empquery == 'r':
        x = []
        for z in dictionaryhold[position].keys():
            x.append(z)
        for c in range(len(x)):
            print(f"\n{x[c]} .... {dictionaryhold[position][x[c]]}")
        submenu(empname,position,nlist,retfunc)
    elif empquery == '1':
        domain = input('please enter your company domain:')
        print('\n  \n  ')
        nlist[position].emailgen(domain)
        submenu(empname,position,nlist,retfunc)
    elif empquery == '2':
        print('\n  \n  ')
        nlist[position].termlogingen()
        submenu(empname,position,nlist,retfunc)
    elif empquery == '3':
        print('\n  \n  ')
        nlist[position].empstatus()
        submenu(empname,position,nlist,retfunc)
    elif empquery == '4':
        print('\n  \n  ')
        nlist[position].annivCheck()
        submenu(empname,position,nlist,retfunc)
    else:
        print('beepboop... does not compute! try again :(')
        specfuncMenu(empname,position,nlist,retfunc)




def quickempcheckMenu(nlist,retfunc):
    empfound = 'false'
#     position of found employee in the istantiated dictionary
    empposit = 0
    empentry = input('Enter employees name here:')
    empsearch=empentry.replace(" ", "")
    print(empsearch)
    for name in range(len(nlist)):
        if nlist[name].first + nlist[name].last == empsearch:
            empfound = 'true'
            empposit = name
        elif nlist[name].nickname == empsearch:
            empfound = 'true'
            empposit = name
        else:
            pass
    if empfound == 'true':
        print(f'found ur entry. what do you want to know about {empentry}?')
        print(empposit)
        specfuncMenu(empsearch,empposit,nlist,retfunc)
    else:
        print('sorry did not find them. Try Again!')
        quickempcheckMenu(nlist,retfunc)





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# THIS IS WHERE THE GROUP FUNCTIONS BEGIN ----- MENU CHOICE 2 FROM OBJECTMENU()









# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# THIS THE MENU TO CHOOSE WETHER INDIVIDUAL OR GROUP VIEW UTILIZES FUNCTIONS ABOVE

def objectMenu(nlist,retfunc):
    print('welcome to the dataviewer')
    viewerchoice = input('To view individual Employee data enter ... < 1 >\nTo view Group date enter ... < 2 >\nTo return to main menu enter ... <q>\n:')
    if viewerchoice == '1':
        quickempcheckMenu(nlist,retfunc)
    elif viewerchoice == '2':
        pass
    elif viewerchoice == 'q':
        retfunc()
    else:
        print('please choose 1 or 2...try again')
        objectMenu(nlist,retfunc)
    