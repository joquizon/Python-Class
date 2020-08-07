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
        



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







#employeecreate() takes the inputs so the emplyee is instantiated in the class
def EmployeeCreate(nlist,dtlist,dhold):
        first = dtlist[0]
        last = dtlist[1] 
        nickname = dtlist[2] 
        social = dtlist[3] 
        contel = dtlist[4] 
        address = dtlist[5]
        city = dtlist[6]
        state = dtlist[7] 
        zipcode  = dtlist[8]
        hiremonth = dtlist[9]
        hiredate = dtlist[10]
        hireyear = dtlist[11]
        dept = dtlist[12]
        position = dtlist[13]
        hourlypay = dtlist[14]
        weeklypay = dtlist[15]
        monthlypay = dtlist[16]
        yearlypay = dtlist[17]
        sicktaken = dtlist[18]
        sickremaining = dtlist[19]
        perstaken = dtlist[20]
        persremaining = dtlist[21]
        vactaken = dtlist[22]
        vacremaining = dtlist[23]
        sickdates = dtlist[24]
        persdates = dtlist[25]
        vacdates = dtlist[26]
        hdatecombo =dtlist[z][11]+hiremonth+dtlist[z][9]+dtlist[z][10]

        nlist[-1] = Employee(first,last,nickname,social,contel,address,city,state,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates)
        
        print(f'employee {nlist[-1].first+nlist[-1].last} has been instantiated')
        
        dhold.append(nlist[-1].__dict__)







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
def classcomprede(dhold):
    noclistkey=[]
    for x in range(len(dhold)):
        noclistkey.append(dhold[x]['first']+dhold[x]['last'])
    print(noclistkey)
    obdict=dict(zip(noclistkey,noclist))



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