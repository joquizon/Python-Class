
def yearcheck():
    import datetime
    z=datetime.datetime.now()
    yearnow = (z.strftime("%Y"))
    yearint = (int(yearnow))-2000
    
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

yearcheck()

class Employee:
    def __init__(self,first,last,nickname,social,contel,address,city,state,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates):
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
    def raiseyet(self):
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
            elif int(self.hiremonth) == monthint:
                if int(self.hiredate) <= dayint:
                    print("Review / Raise")
                else:
                    print(f'{int(self.hiredate) - dayint} day(s) from Review and / or Raise')        
            else:
                print(f'{int(self.hiremonth) - monthint} month(s) away Review and / or Raise')
        else:
            print('next year')








    # class method to give employees vacation days on hiredate anniversy
    def addvacdays(self,vacalot):
        import datetime
        z=datetime.datetime.now()
        monthnow = (z.strftime("%m"))
        daynow = (z.strftime("%d"))
        yearnow = (z.strftime("%Y"))
        yearint = (int(yearnow))-2000
        monthint= int(monthnow)
        dayint = int(daynow)
        print (self.hdatecombo)
        
        if int(self.hireyear) < yearint:
            if int(self.hiremonth) < monthint:
                self.vacremaining = int(self.vacremaining) + vacalot 
                print(self.vacremaining)
            elif int(self.hiremonth) == monthint:
                if int(self.hiredate) <= dayint:
                    self.vacremaining = int(self.vacremaining) + vacalot 
                    print(self.vacremaining)
                else:
                    print(f'{int(self.hiredate) - dayint} day(s) away from additional vacation time')        
            else:
                print(f'{int(self.hiremonth) - monthint} month(s) away from additional vacation time')
        else:
            print('next year')



    # class method to give employees additional personal days on new calendar year
    def persadd(self):
        nextyear = yearcheck()
        if nextyear == True:
            for key in obdict:
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
        sickdates = nmlist[z+1]
        persdates = nmlist[z+2]
        vacdates = nmlist[z+3]
        hdatecombo =nmlist[z][11]+hiremonth+nmlist[z][9]+nmlist[z][10]
        
        noclist[x] = Employee(first,last,nickname,social,contel,address,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates)
        print(f'employee {nlist[x]} has been instantiated')
    for dt in range(len(noclist)):
        dictionaryhold.append(noclist[dt].__dict__)

    print(dictionaryhold)












# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# def editlistloader(nlist,nmlist,dhold):
#     for x in range (len(dhold)):
#         nmlist.append([])
#     newlistA=[]
#     for v in range(len(dhold)):
#         nlist.append(dhold[v]['first']+dhold[v]['last'])
        
#     for w in range(len(dhold)):
#         newlistA.append(dhold[w])
#         for k in (newlistA[w]):
#             nmlist[w].append(newlistA[w][k])
#     print(f'here it is the freeekking dicter {dhold}')

obdict = 0

def classcomprede(dhold,odc):
    noclistkey=[]
    for x in range(len(dhold)):
        noclistkey.append(dhold[x]['first']+dhold[x]['last'])
    print(noclistkey)
    odc=dict(zip(noclistkey,noclist))



def sortbydept():
    alphsortdept = {key: value for key, value in sorted(obdict.items(), key=lambda item: item[1].dept)}
    pass

def listdeptPos():
    alphsortdept = {key: value for key, value in sorted(obdict.items(), key=lambda item: item[1].dept)}
    # loop obdict grab specific dept
    # append to new dictionary
    # sort new dictionary by position
    pass

def sortbyposition():
    alphsortposition = {key: value for key, value in sorted(obdict.items(), key=lambda item: item[1].position)}
    pass

def positionAllCount():
    pass

def positionDeptCount():
    pass

# you can create counts of position and average out pay and longevity in position overall or by dept


def sortbylastname():
    alphsortlast = {key: value for key, value in sorted(obdict.items(), key=lambda item: item[1].last)}
    pass

def sortbypay():
    numsortyearlypay = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(float(item[1].yearlypay)))}
    pass

def sortbyhiredate():
    numsorthdatecombo = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(float(item[1].hdatecombo)))}
    pass

def sortbysicktake():
    numsortsicktaken = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(item[1].sicktaken))}
    pass

def sortbyperstake():
    numsortperstaken = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(item[1].perstaken))}
    pass

def sortbyvactake():
    numsortvactaken = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(item[1].vactaken))}
    pass

def sortbysickRemain():
    numsortsickremaining = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(item[1].sickremaining))}
    pass

def sortbypersRemain():
    numsortpersremaining = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(item[1].persremaining))}
    pass

def sortbyvacRemain():
    numsortvacremaining = {key: value for key, value in sorted(obdict.items(), key=lambda item: int(item[1].vacremaining))}
    pass



# chart attendance patterns over time using sickdates or vacation and persdates tendencies with pervac dates







# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





# grabs particular departments pay total and avg pay /// ret only total of dep so it can be reused by totalpay
def payavg(depvar):
    payadder=[]
    for key in obdict:
        if obdict[key].dept == depvar: 
            payadder.append(int(float(obdict[key].yearlypay)))
    avgpay = sum(payadder)//len(payadder)
    print(f'Yearly {avgpay}')
    print(f'Monthly {avgpay/12}')
    print(f'Weekly {avgpay/52}')
    print(f'Total{sum(payadder)}')
    return (sum(payadder))

# grabs particular departments pay total and avg pay THEN gives total annd avg pay
def totalpay(depvar,depvar2,depvar3,depvar4,depvar5,depvar6):
    a = payavg(depvar)
    b = payavg(depvar2)
    c = payavg(depvar3)
    d = payavg(depvar4)
    e = payavg(depvar5)
    f = payavg(depvar6)

    print(f'total payroll{sum[a,b,c,d,e,f]}')
    print(f'avg payroll/ yr {(sum[a,b,c,d,e,f])//6}')
    print(f'avg payroll/ mo {((sum[a,b,c,d,e,f])//6)12}')
    print(f'avg payroll/ wk {((sum[a,b,c,d,e,f])//6)52}')













# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>











def bulkinst(nlist,nmlist,dhold):
    for x in range(len(nlist)):
        first = nmlist[x][0]
        last = nmlist[x][1] 
        nickname = nmlist[x][2] 
        social = nmlist[x][3] 
        contel = nmlist[x][4] 
        address = nmlist[x][5]
        city = nmlist[x][6]
        state = nmlist[x][7] 
        zipcode  = nmlist[x][8]
        hiremonth = nmlist[x][9]
        hiredate = nmlist[x][10]
        hireyear = nmlist[x][11]
        dept = nmlist[x][12]
        position = nmlist[x][13]
        hourlypay = nmlist[x][14]
        weeklypay = nmlist[x][15]
        monthlypay = nmlist[x][16]
        yearlypay = nmlist[x][17]
        sicktaken = nmlist[x][18]
        sickremaining = nmlist[x][19]
        perstaken = nmlist[x][20]
        persremaining = nmlist[x][21]
        vactaken = nmlist[x][22]
        vacremaining = nmlist[x][23]
        sickdates = nmlist[x][24]
        persdates = nmlist[x][25]
        vacdates = nmlist[x][26]

        nlist[x] = Employee(first,last,nickname,social,contel,address,city,state,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates)
    
    print(f'employee {nlist[x]} has been instantiated')
    for dt in range(len(nlist)):
        dhold.append(nlist[dt].__dict__)
    print(dhold)





def whoboss(dhold):
    for lo in range(len(dhold)):
        print(dhold[lo]['dept'])
        if dhold[lo]['position'][0] == '*':
            name = dhold[lo]['first']+' ' + dhold[lo]['last']
            print(f'{name} is a boss!!!!!!')


def whereerrbody(dhold):
    for zc in range(len(dhold)):
        print(f"{dhold[zc]['first']} {dhold[zc]['last']} is in this zipcode: {dhold[zc]['zipcode']}.")