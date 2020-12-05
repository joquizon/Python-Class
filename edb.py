from openerLoader import employeeloader
from openerLoader import terminator
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
from newEmpdataFuncsModule import postsetter
from newEmpdataFuncsModule import depconfirmation
from newEmpdataFuncsModule import paysetter
from newEmpdataFuncsModule import verifier
from newEmpdataFuncsModule import linechooser
from savers import readytosave
from savers import filencrypter
from savers import listcreate
from savers import newempfilesaver
from editEmp import empsearchprinter
from editEmp import sickdayslog
from editEmp import persdayslog
from editEmp import vacdayslog
from logmtn import Mainsicpervac_Mtn
from nocsaver import goneempfilesaver
from nocsaver import nocupdate
from nocsaver import terminencrypter
from mainInstant import OOPstart
from mainInstant import objectMenu


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
# print(monthnow)
# print(daynow)
# print(yearnow)
hireY=1
hiredD=1
hiredM=1
x=datetime.datetime(hireY,hiredD,hiredM)
depset=[0]
daynowstr = (z.strftime("%d"))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sickday persday vacday listcreator
sickdatestart =['AA']
persdatestart =['AA']
vacdatestart =['AA']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> position of input match on employeesearch
searchpos=[0]
nocpos=0



def noclistedit():
    terminator(noclist)
    nocupdate(noclist)
    terminencrypter()
    modeset()
    





# this fnction is for editing existing employee info entries
def EditempInfo():
    # subfunc to save before restarting back the toedit input 
    def sicpervacsavers():
        editlist = nocmemlist[searchpos[0]]
        editlistA = nocmemlist[searchpos[0]+1]
        editlistB= nocmemlist[searchpos[0]+2]
        editlistC= nocmemlist[searchpos[0]+3]
        newempfilesaver(editlist,editlistA,editlistB,editlistC,EditempInfo,noclist)

    print(searchpos)
    toedit = input('enter the no. of the line you wish to edit or (s) if you want to save youre done and ready to save\nor (m) to go to the log maintenance\n(<)if you wish to return to the previous menu: ')
    for x in range(0,18):
        if toedit == str(x):
            linechooser(toedit,noclist,nocmemlist,searchpos,modeset,monthnow,daynow,yearnow,depset,EditempInfo,daynowstr)
        else: pass
    if toedit == '<':
        modeset()
    elif toedit == 's':
        editlist = nocmemlist[searchpos[0]]
        editlistA = nocmemlist[searchpos[0]+1]
        editlistB= nocmemlist[searchpos[0]+2]
        editlistC= nocmemlist[searchpos[0]+3]
        readytosave(editlist,editlistA,editlistB,editlistC,EditempInfo,modeset,newempfilesaver,noclist,monthnow,daynow,yearnow,depset)
    elif (toedit) == '19' or (toedit) == '21' or (toedit) == '23':
        linechooser(toedit,noclist,nocmemlist,searchpos,modeset,monthnow,daynow,yearnow,depset,EditempInfo,daynowstr)
    elif (toedit) == '18' or (toedit) == '24':
        sickdayslog(sicpervacsavers,nocmemlist,searchpos,monthnow,daynow,yearnow)
    elif (toedit) == '20' or (toedit) == '25':
        persdayslog(sicpervacsavers,nocmemlist,searchpos,monthnow,daynow,yearnow)
    elif (toedit) == '22' or (toedit) == '26':
        vacdayslog(sicpervacsavers,nocmemlist,searchpos,monthnow,daynow,yearnow)
    elif toedit ==  'm':
        Mainsicpervac_Mtn(sicpervacsavers,nocmemlist,searchpos)
    elif toedit == 'Q':
        quit()
    else:
        print('boopbeep doesnot compute')
        EditempInfo()


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
    hiredate(monthnow,daynow,yearnow,dataentered,daynowstr)           
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireday     
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hiremonth     
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hireyear 
    depsetter(dataentered,depset)
    postsetter(dataentered,depset)
    depconfirmation(dataentered,depset)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets department   
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets position  
    paysetter(dataentered)   
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sets pay
    verifier(dataentered,sickdatestart,persdatestart,vacdatestart,modeset,monthnow,daynow,yearnow,depset,noclist,daynowstr)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>confirm or edit info
    readytosave(dataentered,sickdatestart,persdatestart,vacdatestart,verifier,modeset,newempfilesaver,noclist,monthnow,daynow,yearnow,depset)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> say yes and runs func to creates files --> encrypted --> saved



def ViewerStart(nlist,nmlist,retfunc):
    # this instantiates
    OOPstart(nlist,nmlist)
    # this starts the menu
    objectMenu(nlist,retfunc)




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>mode select
def modeset():
    noclist.clear()
    nocmemlist.clear()
    employeeloader(noclist,nocmemlist)
    mission = input("(1) new ENTRY // (2) file READER // (3) Terminator // (4)Viewer // (q) EXiT: ")
    if mission== '1':
        print("A new employee! coo'coo :)")
        Ndataenter()
    elif mission== '2':
        # if youve reset the list (add 0 in first position as a dummy posit no. else EditempInfo wont print employee info properly)
        empsearchprinter(nocpos,noclist,nocmemlist,searchpos,modeset)
        print(nocpos)
        EditempInfo()
    elif mission == '3':
        noclistedit()

    elif mission == '4':
        ViewerStart(noclist,nocmemlist,modeset)

    elif mission == 'q':
        quit()

    else:
        print('boopbeep Error!')
        modeset()
modeset()