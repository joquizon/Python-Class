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
        nlist[-1] = Employee(first,last,nickname,social,contel,address,city,state,zipcode,hiremonth,hiredate,hireyear,dept,position,hourlypay,weeklypay,monthlypay,yearlypay,sicktaken,sickremaining,perstaken,persremaining,vactaken,vacremaining,sickdates,persdates,vacdates)
        print(f'employee {nlist[-1]} has been instantiated')







# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





def editlistloader(nlist,nmlist,dhold):
    for x in range (len(dhold)):
        nmlist.append([])
    print(nmlist)
    newlistA=[]
    for v in range(len(dhold)):
        nlist.append(dhold[v]['first']+dhold[v]['last'])
        
    for w in range(len(dhold)):
        newlistA.append(dhold[w])
        for k in (newlistA[w]):
            nmlist[w].append(newlistA[w][k])