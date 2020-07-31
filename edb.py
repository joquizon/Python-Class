from openerLoader import employeeloader
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
from newEmpdataFuncsModule import verifier
from newEmpdataFuncsModule import linechooser
from savers import readytosave
from savers import filencrypter
from savers import listcreate
from savers import newempfilesaver
from editEmp import empsearchprinter


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Openloader vars
nocmemlist =[]
noclist=[]


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list that collects input data
dataentered=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>time variables for time based funcs
import datetime
z=datetime.datetime.now()
monthnow = (z.strftime("%m"))
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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> position of input match on employeesearch
searchpos=[0]

# this fnction is for editing existing employee info entries
def EditempInfo():
    print(searchpos)
    toedit = input('enter the no. of the line you wish to edit or (s) if you want to save youre done and ready to save: ')
    if toedit == '<':
        modeset()
    elif toedit == 's':
        editlist = nocmemlist[searchpos[0]]
        editlistA = nocmemlist[searchpos[0]+1]
        editlistB = nocmemlist[searchpos[0]+2]
        editlistC = nocmemlist[searchpos[0]+3]
        readytosave(editlist,editlistA,editlistB,editlistC,EditempInfo,modeset,newempfilesaver,noclist,monthnow,daynow,yearnow,depset)
    elif int(toedit)<18:
        linechooser(toedit,noclist,nocmemlist,searchpos,modeset,monthnow,daynow,yearnow,depset,EditempInfo)
    else:
        print('boopbeep doesnot compute')
        EditempInfo()



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>











# this fnction is for new employee info entrie
def Ndataenter():
    firstset(dataentered,modeset)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>first name            
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
    verifier(dataentered,sickdatestart,persdatestart,vacdatestart,modeset,monthnow,daynow,yearnow,depset,noclist)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>confirm or edit info
    readytosave(dataentered,sickdatestart,persdatestart,vacdatestart,verifier,modeset,newempfilesaver,noclist,monthnow,daynow,yearnow,depset)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> say yes and runs func to creates files --> encrypted --> saved







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
    noclist.clear()
    nocmemlist.clear()

    employeeloader(noclist,nocmemlist)
    mission = input("1 for entry or 2 for output: ")
    if mission== '1':
        print("A new employee! coo'coo :)")
        Ndataenter()
    elif mission== '2':
        empsearchprinter(noclist,nocmemlist,searchpos,modeset)
        EditempInfo()
    elif mission == '3':
        print(nocmemlist)
        print(noclist)
        hiredate(monthnow,daynow,yearnow,dataentered)

    elif mission == '4':
        quit()
    else:
        print('boopbeep Error!')
        modeset()
modeset()