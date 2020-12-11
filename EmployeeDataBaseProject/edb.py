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
from empcreateintegrate import demorun
from initiate import resetnoclist
from initiate import demoend
from restoredefault import filedeleter
from restoredefault import freshstart
import os
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



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> credentials
screennames = []
passwords = []



def clearscreen():
    import os
    from os import system
    clear = lambda: system('cls')
    clear()

def noclistedit():
    terminator(noclist)
    nocupdate(noclist)
    terminencrypter()
    clearscreen()
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

    clearscreen()


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
    clearscreen()


def ViewerStart(nlist,nmlist,retfunc):
    # this instantiates
    OOPstart(nlist,nmlist)
    # this starts the menu
    objectMenu(nlist,retfunc)


def demochoose(nlist):
    print('\nThe Demo mode of Employee Database will create fictional files\n so that you may test run its functionality\n')
    demochoice = input('to begin Enter <1>\n if you are already in Demo mode and would like to delete the fictional files Enter <2>: ')
    if demochoice == '1':
        demorun()
        clearscreen()
        print('DEMO MODE IN EFFECT!!!')
        modeset()
        
    elif demochoice == '2':
        demoend(nlist)
        resetnoclist()
        clearscreen()
        modeset()
    else:
        demochoose()



def resetEDB(nlist):
    filedeleter(nlist)
    freshstart()
    clearscreen()
    modeset()



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>mode select
def modeset():
    noclist.clear()
    nocmemlist.clear()
    dataentered.clear()
    for x in range(18):
        dataentered.append(0)
    employeeloader(noclist,nocmemlist)
    mission = input("(1) new ENTRY // (2) file READER // (3) Terminator // (4)Viewer // (5) begin or end Demo Content // ('X') Logout // ('C') Create New Log in // ('R') RESTORE factory Default // (q) EXiT: ")
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
    
    elif mission == '5':
        clearscreen()
        demochoose(noclist)

    elif mission == 'X':
        logout()

    elif mission == 'C':
        clearscreen()
        createEntry()

    elif mission == 'R':
        resetEDB(noclist)
        modeset()

    elif mission == 'q':
        clearscreen()
        quit()

    else:
        print('boopbeep Error!')
        modeset()




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# LOG IN and LOG IN CREATOR FUNCTIONS



def credloader():
    from cryptography.fernet import Fernet
    fkey = open('testdocs/niterun/filekeyMain.NIGHT','rb')
    key = fkey.read()
    cipher = Fernet(key)          

    with open('testdocs/niterun/mulder.night','rb') as df:
        encryptedfile = df.read()
    decrypted_file = cipher.decrypt(encryptedfile)


    screener = (decrypted_file.decode()).splitlines() 
    for sm in range(len(screener)):
        screennames.append(screener[sm])
        

    with open('testdocs/niterun/scully.night','rb') as ef:
        encryptedfile2 = ef.read()
    decrypted_file2 = cipher.decrypt(encryptedfile2)


    passer = (decrypted_file2.decode()).splitlines() 
    for tn in range(len(passer)):
        passwords.append(passer[tn])
        

def entrycrypt():
    from cryptography.fernet import Fernet
    fkey = open('testdocs/niterun/filekeyMain.NIGHT','rb')
    key = fkey.read()
    print (key)
    cipher = Fernet(key)

#     opens created files to be encrypted and encrypts
    foxfile= 'testdocs/niterun/mulder.night'
    with open(foxfile,'rb')as e:
        foxfiletoencrypt = e.read()

    foxencryptedfile = cipher.encrypt(foxfiletoencrypt) 
    with open(foxfile,'wb') as xx:
        xx.write(foxencryptedfile)

        
    danafile= 'testdocs/niterun/scully.night'
    with open(danafile,'rb')as e:
        danafiletoencrypt = e.read()

    danaencryptedfile = cipher.encrypt(danafiletoencrypt) 
    with open(danafile,'wb') as xs:
        xs.write(danaencryptedfile)
    clearscreen()
    modeset()
    
def entrystore():

    with open(f'testdocs/niterun/mulder.night',mode='w')as f:
        for m in range(len(screennames)):
            f.write(f'{screennames[m]}\n')
    with open(f'testdocs/niterun/scully.night',mode='w')as d:
        for n in range(len(passwords)):
            d.write(f'{passwords[n]}\n')
    print('filecreated')
    entrycrypt()

def passwordCreate():
    print('create your password here\nyour password needs be at least 6 characters long and\n to include one of each of the following !@#$%^&*, a number and a letter:')
    alphab = 'abcdefghijklmnopqrstuvwxyz'
    nmr = '1234567890'
    symb = '!@#$%^&*'
    pcheck = [[],[],[]]
    newpass = input('new password: ')
    for a in range(len(newpass)):
        if newpass[a] in (alphab):
            pcheck[0].append('A')
        elif newpass[a] in (nmr):
            pcheck[1].append('B')
        elif newpass[a] in (symb):
            pcheck[2].append('C')
        else:
            print('you are using an unauthorized character in your password READ THE INSTRUCTION PLS.')
            passwordCreate()
            
    if len(pcheck[0])>0 and len(pcheck[1])>0 and len(pcheck[2])>0 and len(newpass) > 5:
        print('password Created')
        passwords.append(newpass)
        entrystore()
    else:
        print('password missing requirement/s try again')
        passwordCreate()
                
def createEntry():
    print('create screen name here')
    newuser = input('enter your new username here: ')
    for a in range(len(screennames)):
        if newuser != screennames[a]:
            screennames.append(newuser)
            passwordCreate()
        else:
            print('that user name has been picked')
            createEntry()

def login():
    scn = input('enter your screen name or type in quit to close program: ')
    pw = input('enter your password: ')
    logcheck = []
    if  scn == 'quit':
        quit()
    else:
        for x in range(len(screennames)):
            if scn == screennames[x]:
                logcheck.append('s')
            else:
                pass
                
        for y in range(len(passwords)):
            if pw == passwords[y]:
                logcheck.append('s')
            else:
                pass
        if len(logcheck) == 2:
            clearscreen()
            print('WELCOME')
            modeset()
        else:
            print('try again')
            login()


def logout():
    clearscreen()
    login()

    
credloader()
clearscreen()
login()





