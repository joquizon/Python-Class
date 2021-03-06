import datetime
z=datetime.datetime.now()
monthnow = int((z.strftime("%m")))
yearnow = (z.strftime("%Y"))
yearint = (int(yearnow))-2000


# zipped dict
obdict = 0
noclistkey=[]



# this file is used annual functions to be run. new yr ret True updates file and save
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


# this file is used  functions to be run every 2 mos. if its been 2 mos. ret True update file and save  
def everytwocheck():   
    from cryptography.fernet import Fernet
    fkey = open('testdocs/filekey.night','rb')
    key = fkey.read()
    cipher = Fernet(key)   
    
    with open('testdocs/sickrun.night','rb') as ys:
        encryptedfileSR = ys.read()
    decrypted_fileSR = cipher.decrypt(encryptedfileSR)
    sickrun = (decrypted_fileSR.decode())
    
    if int(sickrun) == monthnow:
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
        self.empnoyrs = empnoyrs
        self.sickdates = sickdates
        self.persdates = persdates
        self.vacdates = vacdates
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
                print("Review / Raise")
                return True
            elif int(self.hiremonth) == monthint:
                if int(self.hiredate) <= dayint:
                    print("Review / Raise")
                    return True
                else:
                    print(f'{int(self.hiredate) - dayint} day(s) from Review and / or Raise')
                    return False        
            else:
                print(f'{int(self.hiremonth) - monthint} month(s) away Review and / or Raise')
                return False
        else:
            print('next year')





    # class method to give employees additional personal days on new calendar year
    def persadd(self,odc):
        nextyear = yearcheck()
        if nextyear == True:
            for key in odc:
                self.persremaining = int(self.persremaining) + 3
                print(f'{self.first} has {self.persremaining} personal days')
        else:
            print('same brah')




    





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




#employeecreate() takes the all employees and instantiate as class objects
def EmployeeCreate(nlist,nmlist,dhold):
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
        empnoyrs = nmlist[z][24]
        sickdates = nmlist[z+1]
        persdates = nmlist[z+2]
        vacdates = nmlist[z+3]
        hdatecombo =nmlist[z][11]+hiremonth+nmlist[z][9]+nmlist[z][10]
        
        noclist[x] = Employee(first,last,nickname,social,contel,address,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates,empnoyrs)
        print(f'employee {nlist[x]} has been instantiated')
    for dt in range(len(noclist)):
        dictionaryhold.append(noclist[dt].__dict__)

    print(dictionaryhold)



# creates dictionary to make instance variables

for x in range(len(dictionaryhold)):
    noclistkey.append(dictionaryhold[x]['first']+dictionaryhold[x]['last'])
print(noclistkey)
obdict=dict(zip(noclistkey,noclist))







# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



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
acct = {}
accntposDict = [acct]
accntposDictSTR = ['acct']

engdict = {}
engMgmt = {}
engnr = {}
engposDict = [engnr]
engposDictSTR = ['engnr']


positlist = [fdagnt,ntaud,bllmn,drmn,hskper,hseman,res,oprtr,acct,engnr]
positlistSTR = ['front desk agents','nightauditors','bellmen','doormen','housekeeper','housemen','reservationists','operators','accountants','engineers']

mngmt = [accntMgmt,engMgmt,fdMgmt,hskMgmt,pbxMgmt,sleMgmt]

dep = [hskdict,fddict,engdict,pbxdict,sledict,accntdict]                
depString = ['housekeeping','front desk','engineering','pbx','sales','accounting'] 

# this function sorts the whole direct by last name. loops thru that and updates dep dict. then loops throug dep dict
# and updates position dictionaries from that dep
def depsep(dep,dest,destA,destAstr,destB):
    obd={key: value for key, value in sorted(obdict.items(), key=lambda item: item[1].last)}
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



depsep('FD',fddict,FDposDict,FDposDictSTR,fdMgmt)
depsep('hsk',hskdict,HskposDict,HskposDictSTR,hskMgmt)
depsep('sle',sledict,SleposDict,SleposDictSTR,sleMgmt)
depsep('pbx',pbxdict,pbxposDict,pbxposDictSTR,pbxMgmt)
depsep('acct',accntdict,accntposDict,accntposDictSTR,accntMgmt)
depsep('sle',sledict,SleposDict,SleposDictSTR,sleMgmt)
depsep('eng',engdict,engposDict,engposDictSTR,engMgmt)

# this function prints the directory for the whole property
def propDirprint():
    pdp={key: value for key, value in sorted(obdict.items(), key=lambda item: item[1].last)}
    for  x in pdp:
        print(f'\n{pdp[x].last}, {pdp[x].first}  <{pdp[x].dept}//{pdp[x].position}>......{pdp[x].contel}\n{pdp[x].address}\n{pdp[x].city}, {pdp[x].state} {pdp[x].zipcode}\n')



# this function prints the directory for a chosen department
def indyDirprint():
    for pick in range(len(depString)):
        print(f'{pick}....{depString[pick]}')
    
    usercho = input('choose the no. of the dep directory you would like to see: ')

    if usercho not in ('012345') and len(usercho)>0:
        print('try again')
        indyDirprint()
    else:
        for ent in dep[int(usercho)]:
            print(f'\n{dep[int(usercho)][ent].last}, {dep[int(usercho)][ent].first}  <{dep[int(usercho)][ent].dept}//{dep[int(usercho)][ent].position}>......{dep[int(usercho)][ent].contel}\n{dep[int(usercho)][ent].address}\n{dep[int(usercho)][ent].city}, {dep[int(usercho)][ent].state} {dep[int(usercho)][ent].zipcode}\n')



# this function prints the directory for a chosen labor position // or the management direct
def specDirprint():
    for pos in range(len(positlistSTR)):
        print(f'{pos}....{positlistSTR[pos]}')
    print(f'{(len(positlistSTR))+1}....Manager directory')
    userchoA = input('choose the no. of the position directory you would like to see: ')
    if userchoA == str((len(positlistSTR))+1) and len(userchoA)>0:
        for dmg in range(len(mngmt)):
            for subdmg in mngmt[dmg]:
                print(f'\n{mngmt[dmg][subdmg].last}, {mngmt[dmg][subdmg].first}  <{mngmt[dmg][subdmg].dept}//{mngmt[dmg][subdmg].position}>......{mngmt[dmg][subdmg].contel}\n{mngmt[dmg][subdmg].address}\n{mngmt[dmg][subdmg].city}, {mngmt[dmg][subdmg].state} {mngmt[dmg][subdmg].zipcode}\n')
        specDirprint()
    elif userchoA not in ('0123456789') or len(userchoA) == 0:
        print('try again')
        specDirprint()
    else:
        for pst in positlist[int(userchoA)]:
            print(f'\n{positlist[int(userchoA)][pst].last}, {positlist[int(userchoA)][pst].first}  <{positlist[int(userchoA)][pst].dept}//{positlist[int(userchoA)][pst].position}>......{positlist[int(userchoA)][pst].contel}\n{positlist[int(userchoA)][pst].address}\n{positlist[int(userchoA)][pst].city}, {positlist[int(userchoA)][pst].state} {positlist[int(userchoA)][pst].zipcode}\n')
        specDirprint()

# this function is the menu for choosing to print which directory
def menuforDctry():
    print('1....Complete Property Directory\n2....Department Directory\n3...Position Directory\n')
    userchoB = input('Enter the no. of the directory you wish to open: ')
    if userchoB in ('123') and len(userchoB)>0:
        if userchoB == '1':
            propDirprint()
        elif userchoB =='2':
            indyDirprint()
        else:
            specDirprint()
        menuforDctry()
    else:
        print('Sorry Try again')
        menuforDctry()
        

# chart attendance patterns over time using sickdates or vacation and persdates tendencies with pervac dates







# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>













def hdateAnniv(dictr,vacalotLu,vacalotMg,payincLu):
    for emp in dictr:
        check = dictr[emp].annivCheck()
        runcheck = yearint - int(dictr[emp].hireyear)
        print(dictr[emp].first)
        print(dictr[emp].position)
        if dictr[emp].position[0]=='*' and check == True and int(dictr[emp].empnoyrs) < runcheck:
            dictr[emp].empnoyrs = int(dictr[emp].empnoyrs) + 1
            dictr[emp].vacremaining = int(dictr[emp].vacremaining) + vacalotMg
            print('raise time')
            print(f'{dictr[emp].first},{dictr[emp].empnoyrs}')
        elif dictr[emp].position[0] != '*' and check == True and int(dictr[emp].empnoyrs) < runcheck:
            dictr[emp].empnoyrs = int(dictr[emp].empnoyrs) + 1
            dictr[emp].vacremaining = int(dictr[emp].vacremaining) + vacalotLu
            print(dictr[emp].hourlypay)
            dictr[emp].hourlypay = float(dictr[emp].hourlypay) + (float(payincLu))
            print(dictr[emp].hourlypay)
            print(f'{dictr[emp].first},{dictr[emp].yearlypay}')
            dictr[emp].weeklypay = float(dictr[emp].hourlypay) * 40
            dictr[emp].monthlypay = float(dictr[emp].hourlypay) * 160
            dictr[emp].yearlypay = float(dictr[emp].hourlypay) * 2080
            print('raise time')
            print(f'{dictr[emp].first},{dictr[emp].empnoyrs}')
            print(f'{dictr[emp].first},{dictr[emp].yearlypay}')
        elif dictr[emp].position[0]=='*' and check == True and int(dictr[emp].empnoyrs) == runcheck:
            print('Anniversary passed // raise applied manually')
        elif check == True and int(dictr[emp].empnoyrs) == runcheck:
            print('Anniversary passed // raise applied')
        else:
            print('not yet')




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# this func checks if its time to add sickdays and adds it
def sickadd(dictr):
    sickadder = everytwocheck()
    if sickadder == True:
        for sickey in dictr:
            print(f'{dictr[sickey].first} {dictr[sickey].last} ... {dictr[sickey].sickremaining}')
            ns = int(dictr[sickey].sickremaining) + 1
            dictr[sickey].sickremaining = str(ns)
            print(f'{dictr[sickey].first} {dictr[sickey].last} ... {dictr[sickey].sickremaining}')
    else:
        print('not yet')
            




# this func checks if its time to add persdays and adds them
def persadd(dictr):
    nextyear = yearcheck(dictr)
    if nextyear == True:
        for key in dictr:
            dictr[key].persremaining = int(dictr[key].persremaining) + 3
            print(f'{dictr[key].first} has {dictr[key].persremaining} personal days')
    else:
        print('same brah')



# this func checks if its time to add vacdays and adds them marks them as up for review / raise








# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>











