

import datetime
z=datetime.datetime.now()
monthnow = int((z.strftime("%m")))
yearnow = (z.strftime("%Y"))
yearint = (int(yearnow))-2000
print(monthnow)
print(yearnow)
print(yearint)

# zipped dict
obdictA = []

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
    obs = dict(zip(noclistkey,nlist))
    obdictA.append(obs)
# ignition func --- this starts instantiation 
def OOPstart(nlist,nmlist):
    obdictA.clear()
    noclistkey.clear()
    dictionaryhold.clear()
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



# this is where the departments and positions are divided up
# this starts with choice 2 on objectmMenu()

obdict = 0
fddict = {}
fdMgmt = {}
fdagnt = {}
ntaud = {}
bllmn = {}
drmn = {}
FDposDict = [fdagnt,ntaud,bllmn,drmn]
FDposDictSTR = ['fdagnt','ntaud','bllmn','drmn']


hskdict = {}
hskMgmt = {}
hskper = {}
hseman ={} 
HskposDict = [hskper,hseman]
HskposDictSTR = ['hskper','hseman']

sledict = {}
sleMgmt = {}
res = {}
SleposDict = [res]
SleposDictSTR = ['res']

pbxdict = {}
pbxMgmt = {}
oprtr = {}
pbxposDict = [oprtr]
pbxposDictSTR = ['oprtr']

accntdict = {}
accntMgmt = {}
acctnt = {}
accntposDict = [acctnt]
accntposDictSTR = ['acctnt']

engdict = {}
engMgmt = {}
engnr = {}
engposDict = [engnr]
engposDictSTR = ['engnr']

positlist = [fdagnt,ntaud,bllmn,drmn,hskper,hseman,res,oprtr,acctnt,engnr]
positlistSTR = ['front desk agents','nightauditors','bellmen','doormen','housekeeper','housemen','reservationists','operators','accountants','engineers']

mngmt = [accntMgmt,engMgmt,fdMgmt,hskMgmt,pbxMgmt,sleMgmt]
mngmtString = ['Accounting Mgmt','Engineering Mgmt','Front Desk Mgmt','Housekeeping Mgmt','Reservations Mgmt','Sales Mgmt']

dep = [hskdict,fddict,engdict,pbxdict,sledict,accntdict]                
depString = ['housekeeping','front desk','engineering','pbx','sales','accounting'] 

positSalcollectY = []
positSalcollectM = []
positSalcollectW = []









# this function sorts the whole direct by last name. loops thru that and updates dep dict. then loops throug dep dict
# and updates position dictionaries from that dep
def depsep(dep,dest,destA,destAstr,destB):
    obd={key: value for key, value in sorted(obdictA[0].items(), key=lambda item: item[1].last)}
    for x in obd:
        if obd[x].dept == dep:
            dest.update({obd[x].first+obd[x].last:obd[x]})  
        else:
            pass
    for y in dest:
        if dest[y].position[0] == '*':
            destB.update({dest[y].first+dest[y].last:dest[y]})
        else:
            for b in range (len(destA)):
                if dest[y].position == destAstr[b]:
                    destA[b].update({dest[y].first+dest[y].last:dest[y]})
                else:
                    pass
    print('directory created')
    
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#  subfunc to run to return user to groupfuncmenu
def subretfunc(prevfunc,nlist,retfunc):
    print(f'\nWhat would you like to do now?\n')
    subChoice = input(f'\nTry Again enter ... <y>\nGo back to the previous Menu enter ... <*>\nGo back to the Viewer Menu enter ... <m>\n:')
    if subChoice == 'y':
        prevfunc(nlist,retfunc)
    elif subChoice == '*':
        groupfuncMenu(nlist,retfunc)
    elif subChoice == 'm':
        objectMenu(nlist,retfunc)
    else: 
        print('sorry does not compute...try again')
        subretfunc(prevfunc,nlist,retfunc)



# this function displays the status of a position group's pay and time off remaining and taken

def positionStat(nlist,retfunc):
    poskeyhold=[]
    PstsalcollectY = []
    PstsalcollectM = []
    PstsalcollectW = []
    Pstsiclist = []
    Pstperlist = []
    Pstvaclist = []
    Pstsictklist = []
    Pstpertklist = []
    Pstvactklist = []

    lbormgchoice = input('Is it a labor position .... <l> or management .... <m>:')
    if lbormgchoice == 'l':
        for statpos in range(len(positlistSTR)):
            print(f'{statpos}....{positlistSTR[statpos]}')
        poschoiceno = input('please choose the department you would like to review: ')
        if poschoiceno in ('0123456789') and  len(poschoiceno)>0:
            for z in positlist[int(poschoiceno)].keys():
                    poskeyhold.append(z)
            for x in range(len(poskeyhold)):
                PstsalcollectY.append(int(float(obdictA[0][poskeyhold[x]].yearlypay)))  
                PstsalcollectM.append(int(float(obdictA[0][poskeyhold[x]].monthlypay)))  
                PstsalcollectW.append(int(float(obdictA[0][poskeyhold[x]].weeklypay)))
                Pstsiclist.append(int(float(obdictA[0][poskeyhold[x]].sickremaining)))   
                Pstperlist.append(int(float(obdictA[0][poskeyhold[x]].persremaining)))   
                Pstvaclist.append(int(float(obdictA[0][poskeyhold[x]].vacremaining))) 
                Pstsictklist.append(int(float(obdictA[0][poskeyhold[x]].sicktaken)))   
                Pstpertklist.append(int(float(obdictA[0][poskeyhold[x]].perstaken)))   
                Pstvactklist.append(int(float(obdictA[0][poskeyhold[x]].vactaken))) 
    elif lbormgchoice =='m':
        for mgstatpos in range(len(mngmtString)):
            print(f'{mgstatpos}....{mngmtString[mgstatpos]}')
        Mposchoiceno = input('please choose the department you would like to review: ')
        if Mposchoiceno in ('012345') and  len(Mposchoiceno)>0:
            for z in mngmt[int(Mposchoiceno)].keys():
                    poskeyhold.append(z)
            for x in range(len(poskeyhold)):
                PstsalcollectY.append(int(float(obdictA[0][poskeyhold[x]].yearlypay)))  
                PstsalcollectM.append(int(float(obdictA[0][poskeyhold[x]].monthlypay)))  
                PstsalcollectW.append(int(float(obdictA[0][poskeyhold[x]].weeklypay))) 
                Pstsiclist.append(int(float(obdictA[0][poskeyhold[x]].sickremaining)))   
                Pstperlist.append(int(float(obdictA[0][poskeyhold[x]].persremaining)))   
                Pstvaclist.append(int(float(obdictA[0][poskeyhold[x]].vacremaining))) 
                Pstsictklist.append(int(float(obdictA[0][poskeyhold[x]].sicktaken)))   
                Pstpertklist.append(int(float(obdictA[0][poskeyhold[x]].perstaken)))   
                Pstvactklist.append(int(float(obdictA[0][poskeyhold[x]].vactaken)))
    else:
        print('does not compute')
        positionStat(nlist,retfunc)
        
    statuswhat = input('do you want to see salary status .... <s>\n or time off status .... <t>:')
    if statuswhat == 's':
        print(poskeyhold)
        payY=sum(PstsalcollectY)
        payM=sum(PstsalcollectM)
        payW=sum(PstsalcollectW)
        for dd in range(len(poskeyhold)):
            print(f'{obdictA[0][poskeyhold[dd]].first} {obdictA[0][poskeyhold[dd]].last} earns {PstsalcollectY[dd]} yearly\n ')
            print(f'{obdictA[0][poskeyhold[dd]].first} {obdictA[0][poskeyhold[dd]].last} earns {PstsalcollectM[dd]} monthly\n ')
            print(f'{obdictA[0][poskeyhold[dd]].first} {obdictA[0][poskeyhold[dd]].last} earns {PstsalcollectW[dd]} weekly\n ')
        print(f'This position group earns {payY} yearly\n')
        print(f'This position group earns {payM} monthly\n')
        print(f'This position group earns {payW} weekly\n')
        subretfunc(positionStat,nlist,retfunc)
    elif statuswhat == 't':
        print(poskeyhold)
        sicrem =sum(Pstsiclist)
        persrem =sum(Pstperlist)
        vacrem =sum(Pstvaclist)
        sictake =sum(Pstsictklist)
        perstake =sum(Pstpertklist)
        vactake =sum(Pstvactklist)
        for ee in range(len(poskeyhold)):
            print(f'{obdictA[0][poskeyhold[ee]].first} {obdictA[0][poskeyhold[ee]].last} has taken {Pstsiclist[ee]} sick days and has {Pstsictklist[ee]} remaining.\n')
            print(f'{obdictA[0][poskeyhold[ee]].first} {obdictA[0][poskeyhold[ee]].last} has taken {Pstperlist[ee]} personal days and has {Pstpertklist[ee]} remaining.\n')
            print(f'{obdictA[0][poskeyhold[ee]].first} {obdictA[0][poskeyhold[ee]].last} has taken {Pstvaclist[ee]} vacation days and has {Pstvactklist[ee]} remaining.\n')
        print(f'This position group has taken {sictake} sickdays and has {sicrem} remaining\n ') 
        print(f'This position group has taken {perstake} personal days and has {persrem} remaining\n ') 
        print(f'This position group has taken {vactake} vacation days and has {vacrem} remaining\n ') 
        subretfunc(positionStat,nlist,retfunc)
    else:
        print('doesnot compute')
        positionStat(nlist,retfunc)







# this function shows y m w -ly payroll per dept, their members, sic per vac remaining and taken, yrs of experience

def depStat(nlist,retfunc):
    depkeyhold=[]
    depkeyholdSalY=[]
    depkeyholdSalW=[]
    depkeyholdSalM=[]

    siclist = []
    perlist = []
    vaclist = []

    sictlist = []
    pertlist = []
    vactlist = []

    explist = []

    mnglist = []
    lbrlist = []
    
    for depS in range(len(depString)):
        print(f'{depS}....{depString[depS]}')
    
    depchoiceno = input('please choose the department you would like to review: ')
    if depchoiceno in ('012345') and  len(depchoiceno)>0:
        for z in dep[int(depchoiceno)].keys():
                depkeyhold.append(z)
        for x in range(len(depkeyhold)):
            depkeyholdSalY.append(int(float(obdictA[0][depkeyhold[x]].yearlypay)))    
            depkeyholdSalM.append(int(float(obdictA[0][depkeyhold[x]].monthlypay)))    
            depkeyholdSalW.append(int(float(obdictA[0][depkeyhold[x]].weeklypay)))    
            siclist.append(int(float(obdictA[0][depkeyhold[x]].sickremaining)))
            perlist.append(int(float(obdictA[0][depkeyhold[x]].persremaining)))
            vaclist.append(int(float(obdictA[0][depkeyhold[x]].vacremaining)))
            sictlist.append(int(float(obdictA[0][depkeyhold[x]].sicktaken)))
            pertlist.append(int(float(obdictA[0][depkeyhold[x]].perstaken)))
            vactlist.append(int(float(obdictA[0][depkeyhold[x]].vactaken)))
            explist.append(int(float(obdictA[0][depkeyhold[x]].empnoyrs)))
            
            if obdictA[0][depkeyhold[x]].position[0]=='*':
                mnglist.append(obdictA[0][depkeyhold[x]].first+' '+ obdictA[0][depkeyhold[x]].last + '//' + obdictA[0][depkeyhold[x]].position)
            else:
                lbrlist.append(obdictA[0][depkeyhold[x]].first+' '+ obdictA[0][depkeyhold[x]].last + '//' + obdictA[0][depkeyhold[x]].position)


            

        print('\nManagers:')
        for mm in range (len(mnglist)):
            print(f'{mnglist[mm]}\n')
        print('\nTeam Members:')   
        for ll in range (len(lbrlist)):
            print(f'{lbrlist[ll]}\n' )
        
        print(f'sum total years of worker experience:....{sum(explist)}\n')
#         print(f'{depString[int(userChoE)]}....total personnel count: {len(depStatdict)}\n')
        print(f'Yearly Payroll total....{sum(depkeyholdSalY)}\n')
        print(f'Monthly Payroll total....{sum(depkeyholdSalM)}\n')
        print(f'Weekly Payroll total....{sum(depkeyholdSalW)}\n')
        
        print(f'total no. of sick days taken:....{sum(sictlist)} / {sum(siclist)} remaining')
        print(f'total no. of personal days taken:....{sum(pertlist)} / {sum(perlist)} remaining')
        print(f'total no. of vacation days taken:....{sum(vactlist)} / {sum(vaclist)} remaining')
        
    else:
        print('sorry try again!')
        depStat(nlist,retfunc)
        
    subretfunc(depStat,nlist,retfunc)


# this function prints the directory for the whole property
def propDirprint(nlist,retfunc):
    pdp={key: value for key, value in sorted(obdictA[0].items(), key=lambda item: item[1].last)}
    for  x in pdp:
        print(f'\n{pdp[x].last}, {pdp[x].first}  <{pdp[x].dept}//{pdp[x].position}>......{pdp[x].contel}\n{pdp[x].address}\n{pdp[x].city}, {pdp[x].state} {pdp[x].zipcode}\n')
    subretfunc(propDirprint,nlist,retfunc)

def indyDirprint(nlist,retfunc):
    for pick in range(len(depString)):
        print(f'{pick}....{depString[pick]}')
    
    usercho = input('choose the no. of the dep directory you would like to see: ')

    if usercho not in ('012345') and len(usercho)>0:
        print('try again')
        indyDirprint(nlist,retfunc)
    else:
        for ent in dep[int(usercho)]:
            print(f'\n{dep[int(usercho)][ent].last}, {dep[int(usercho)][ent].first}  <{dep[int(usercho)][ent].dept}//{dep[int(usercho)][ent].position}>......{dep[int(usercho)][ent].contel}\n{dep[int(usercho)][ent].address}\n{dep[int(usercho)][ent].city}, {dep[int(usercho)][ent].state} {dep[int(usercho)][ent].zipcode}\n')
    
    subretfunc(indyDirprint,nlist,retfunc)        



# this function prints the directory for a chosen labor position // or the management direct
def specDirprint(nlist,retfunc):
    for pos in range(len(positlistSTR)):
        print(f'{pos}....{positlistSTR[pos]}')
    print(f'mg....Manager directory')
    userchoA = input('choose the no. of the position directory you would like to see: ')
    if userchoA == 'mg':
        for dmg in range(len(mngmt)):
            for subdmg in mngmt[dmg]:
                print(f'\n{mngmt[dmg][subdmg].last}, {mngmt[dmg][subdmg].first}  <{mngmt[dmg][subdmg].dept}//{mngmt[dmg][subdmg].position}>......{mngmt[dmg][subdmg].contel}\n{mngmt[dmg][subdmg].address}\n{mngmt[dmg][subdmg].city}, {mngmt[dmg][subdmg].state} {mngmt[dmg][subdmg].zipcode}\n')
    elif userchoA not in ('0123456789m') or len(userchoA) == 0 :
        print('try again')
        specDirprint(nlist,retfunc)
    else:
        for pst in positlist[int(userchoA)]:
            print(f'\n{positlist[int(userchoA)][pst].last}, {positlist[int(userchoA)][pst].first}  <{positlist[int(userchoA)][pst].dept}//{positlist[int(userchoA)][pst].position}>......{positlist[int(userchoA)][pst].contel}\n{positlist[int(userchoA)][pst].address}\n{positlist[int(userchoA)][pst].city}, {positlist[int(userchoA)][pst].state} {positlist[int(userchoA)][pst].zipcode}\n')
    subretfunc(specDirprint,nlist,retfunc)

# prints total dep sal by yr mo wk -- ly
def depsalprint(nlist,retfunc):
    salcollectY = []
    salcollectM = []
    salcollectW = []
    
    for depick in range(len(depString)):
        print(f'{depick}....{depString[depick]}')
    print
    
    userchoC = input('choose the department salary you would like to see: ')

    
    if userchoC in ('012345') and len(userchoC)>0:
        chosendict = dep[int(userchoC)]
        for cc in chosendict:
            salcollectY.append(float(chosendict[cc].yearlypay))
            salcollectM.append(float(chosendict[cc].monthlypay))
            salcollectW.append(float(chosendict[cc].weeklypay))
            
        print(f'{depString[int(userchoC)]} department total yearly salary\n{sum(salcollectY)}\n')
        print(f'{depString[int(userchoC)]} department total monthly salary\n{sum(salcollectM)}\n')
        print(f'{depString[int(userchoC)]} department total weekly salary\n{sum(salcollectW)}\n')
        subretfunc(depsalprint,nlist,retfunc)
    else:
        print('Please try again')
        depsalprint(nlist,retfunc)




# this func prints the count of each position 
def positCT(nlist,retfunc):
    for ct in range(len(positlistSTR)):
        print(f'{positlistSTR[ct]}....{len(positlist[ct])}')
    
    for ctA in range(len(mngmtString)):
        print(f'{mngmtString[ctA]}....{len(mngmt[ctA])}')
    subretfunc(positCT,nlist,retfunc)

# this function only runs inside positionsalprint func. it provides submenu for printing  spcific dep mgr sals
def mgmtpositsal(nlist,retfunc):
    for mgsal in range(len(mngmtString)):
        print(f'{mgsal}....{mngmtString[mgsal]}')
        
    print(f'6....All')

    userchoDmg = input('Please choose an option: ')

    if userchoDmg in ('012345') and len(userchoDmg)>0 and (len(mngmt[int(userchoDmg)])) > 0:
        MgChospositdict = mngmt[int(userchoDmg)]
        for posal in MgChospositdict:
            positSalcollectY.append(float(MgChospositdict[posal].yearlypay))
            positSalcollectM.append(float(MgChospositdict[posal].monthlypay))
            positSalcollectW.append(float(MgChospositdict[posal].weeklypay))
        print(f'{mngmtString[int(userchoDmg)]}....total count:{len(MgChospositdict)}')
        yearlyAVG = float((sum((positSalcollectY))) // (len(positSalcollectY)))
        monthlyAVG = float((sum((positSalcollectM))) // (len(positSalcollectM)))
        weeklyAVG = float((sum((positSalcollectW))) // (len(positSalcollectW)))   
        print(f'Yearly total....{sum(positSalcollectY)}\nYearly Avg....{yearlyAVG}\n')
        print(f'Monthly total....{sum(positSalcollectM)}\nMonthly Avg....{monthlyAVG}\n')
        print(f'Weekly total....{sum(positSalcollectW)}\nWeekly Avg....{weeklyAVG}\n')
        positSalcollectY.clear()
        positSalcollectM.clear()
        positSalcollectW.clear()
        subretfunc(mgmtpositsal,nlist,retfunc)
    elif userchoDmg == '6'and len(userchoDmg)>0:
        for mgposal in range(len(mngmt)):
            for subposal in mngmt[mgposal]:
                positSalcollectY.append(float(mngmt[mgposal][subposal].yearlypay))
                positSalcollectM.append(float(mngmt[mgposal][subposal].monthlypay))
                positSalcollectW.append(float(mngmt[mgposal][subposal].weeklypay))
            yearlyAVG = float((sum((positSalcollectY))) // (len(positSalcollectY)))
            monthlyAVG = float((sum((positSalcollectM))) // (len(positSalcollectM)))
            weeklyAVG = float((sum((positSalcollectW))) // (len(positSalcollectW)))   
            print(f'Yearly total....{sum(positSalcollectY)}\nYearly Avg....{yearlyAVG}\n')
            print(f'Monthly total....{sum(positSalcollectM)}\nMonthly Avg....{monthlyAVG}\n')
            print(f'Weekly total....{sum(positSalcollectW)}\nWeekly Avg....{weeklyAVG}\n')
            positSalcollectY.clear()
            positSalcollectM.clear()
            positSalcollectW.clear()
            subretfunc(mgmtpositsal,nlist,retfunc)
    else:
        print('sorry There may not be anyone at that position. check the position directory. try again.')
        mgmtpositsal(nlist,retfunc)
        
# this prints salary by position // prints mgmt as whole per dept        
def positionSalprint(nlist,retfunc):
    for salpos in range(len(positlistSTR)):
        print(f'{salpos}....{positlistSTR[salpos]}')
        
    print(f'{len(positlistSTR)}....Management Listing by dep')
    
    userchoD = input('Please choose the salary position you wish to print: ')
    
    if userchoD in ('0123456789') and len(userchoD)>0 and (len(positlist[int(userchoD)])) > 0:
        chospositdict = positlist[int(userchoD)]
        for psal in chospositdict:
            positSalcollectY.append(float(chospositdict[psal].yearlypay))
            positSalcollectM.append(float(chospositdict[psal].monthlypay))
            positSalcollectW.append(float(chospositdict[psal].weeklypay))
        print(f'\n{positlistSTR[int(userchoD)]}....total count:{len(chospositdict)}')
        yearlyAVG = float((sum((positSalcollectY))) // (len(positSalcollectY)))
        monthlyAVG = float((sum((positSalcollectM))) // (len(positSalcollectM)))
        weeklyAVG = float((sum((positSalcollectW))) // (len(positSalcollectW)))
        print(f'Yearly total....{sum(positSalcollectY)}\nYearly Avg....{yearlyAVG}\n')
        print(f'Monthly total....{sum(positSalcollectM)}\nMonthly Avg....{monthlyAVG}\n')
        print(f'Weekly total....{sum(positSalcollectW)}\nWeekly Avg....{weeklyAVG}\n')      
        positSalcollectY.clear()
        positSalcollectM.clear()
        positSalcollectW.clear()
        subretfunc(positionSalprint,nlist,retfunc)
    elif userchoD == '10' and len(userchoD)>0:
        mgmtpositsal(nlist,retfunc)
    else:
        print('sorry There may not be anyone at that position. check the position directory. try again.')
        positionSalprint(nlist,retfunc)

    
    


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





















# menu for departmental positional object viewer
        
def groupfuncMenu(nlist,retfunc):
#     CHOICE 1 TO PRINT DIRECTORY RUNS SUBFUNC menuforDctry()
    def menuforDctry(nlist,retfunc):
        print('1....Complete Property Directory\n2....Department Directory\n3...Position Directory\n*...Previous Menu')
        userchoB = input('Enter the no. of the directory you wish to open: ')
        if userchoB in ('123*') and len(userchoB)>0:
            if userchoB == '1':
                propDirprint(nlist,retfunc)
            elif userchoB =='2':
                indyDirprint(nlist,retfunc)
            elif userchoB =='3':
                specDirprint(nlist,retfunc)
            elif userchoB =='*':
                groupfuncMenu(nlist,retfunc)
            else:
                menuforDctry(nlist,retfunc)
        else:
            print('Sorry Try again')
            menuforDctry(nlist,retfunc)
    
    def menuforSalry(nlist,retfunc):
        print('1...Department Salary Summary\n2...Position Salary Summary\n*...Previous Menu')
        userchoD = input('Enter the no. of the Summary you wish to view: ')
        if userchoD == '1':
            depsalprint(nlist,retfunc)
        elif userchoD =='2':
            positionSalprint(nlist,retfunc)
        elif userchoD =='*':
            pass
#             groupfuncMenu(nlist,retfunc)                
        else:
            print('Sorry Try again')
            menuforSalry(nlist,retfunc)    
            
    gchoice = input('What would you like to do?\nTo print a Directory enter ... <a>\nTo print a Salary Summaries enter ... <b>\nTo see a count of each Property position enter ... <c>\nTo see a Department overview enter ... <d>\nTo see a Position group overview enter ... <e>\n')
    if gchoice == 'a':
        menuforDctry(nlist,retfunc)
    elif gchoice == 'b':
        menuforSalry(nlist,retfunc)
    elif gchoice == 'c':
        positCT(nlist,retfunc)
    elif gchoice == 'd':   
        depStat(nlist,retfunc)
    elif gchoice == 'e':    
        positionStat(nlist,retfunc)
    elif gchoice == '*':
        objectMenu(nlist,retfunc)
    elif gchoice == 'q':
        quit()
    else:
        print('please choose again')
        groupfuncMenu(nlist,retfunc)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# THIS THE MENU TO CHOOSE WETHER INDIVIDUAL OR GROUP VIEW UTILIZES FUNCTIONS ABOVE

def objectMenu(nlist,retfunc):
    print('welcome to the dataviewer')
    viewerchoice = input('To view individual Employee data enter ... < 1 >\nTo view Group date enter ... < 2 >\nTo return to main menu enter ... <*>\nTo QUIT enter ... <q>\n:')
    if viewerchoice == '1':
        quickempcheckMenu(nlist,retfunc)
    elif viewerchoice == '2':
        depsep('FD',fddict,FDposDict,FDposDictSTR,fdMgmt)
        depsep('hsk',hskdict,HskposDict,HskposDictSTR,hskMgmt)
        depsep('sle',sledict,SleposDict,SleposDictSTR,sleMgmt)
        depsep('pbx',pbxdict,pbxposDict,pbxposDictSTR,pbxMgmt)
        depsep('acct',accntdict,accntposDict,accntposDictSTR,accntMgmt)
        depsep('sle',sledict,SleposDict,SleposDictSTR,sleMgmt)
        depsep('eng',engdict,engposDict,engposDictSTR,engMgmt)
        groupfuncMenu(nlist,retfunc)
    elif viewerchoice == '*':
        retfunc()
    elif viewerchoice == 't':
        depStat()
    elif viewerchoice == 'q':
        quit()
    else:
        print('please choose 1 or 2...try again')
        objectMenu(nlist,retfunc)
    