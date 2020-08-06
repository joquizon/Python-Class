
# noclist is list
#elist is big giant nocmemlist
# nocmemlist =[]
# x = 'noclist'
def employeeloader(nlist,elist):
    from cryptography.fernet import Fernet
    fkey = open('testdocs/filekey.night','rb')
    key = fkey.read()
    cipher = Fernet(key)          
    with open('testdocs/noclist.night','rb') as df:
        encryptedfile = df.read()
    decrypted_file = cipher.decrypt(encryptedfile)

    stringnlist = (decrypted_file.decode()).splitlines() 
    for sm in range(len(stringnlist)):
        nlist.append(stringnlist[sm])


    for emp in range(len(stringnlist)):
        from cryptography.fernet import Fernet
        fkey = open('testdocs/filekey.night','rb')
        key = fkey.read()
        cipher = Fernet(key)   
        search = stringnlist[emp]
        with open('testdocs/'+search+'.night','rb') as et:
            encryptedfileA = et.read()
        decrypted_fileA = cipher.decrypt(encryptedfileA)

        load = (decrypted_fileA.decode()).splitlines() 
        elist.append(load)
    print(stringnlist)







# >>>>>>>>>>>>>>>>>>>>>>>Edits noclist basically fires employees
def terminator(list):
    for x in range(len(list)):
        print(f"{x}....{list[x]}")
    connor = input('typed the line no. of the employee you wish to tuhminate:')
    while True:
        try:
            connorno = int(connor)
            if connorno <= len(list):
                print(f'hasta la vista {list[connorno]}')
                list.pop(connorno)
                for x in range(len(list)):
                    print(f"{x}....{list[x]}")
            else:
                print('nooooo')
                terminator(list)
        except ValueError :
            print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
            terminator(list)
            break
        else:
            break        




# >>>>>>>>>>>>>>>>>>>>>>>saves noclist after fires employees

def Terminsave(retfunc,savefunc,nlist):
    saver = input('save your entries or edits? enter (y) to save enter (<) to go back: ')
    if saver == 'y':
        savefunc(retfunc,nlist)
    elif saver =='<':
        print('going back to the main menu will erase all the data you have entered!!! Are you sure?')
        returner = input('type (y) for yes or (n) for no: ')
        if returner == "y":
            retfunc()
        elif returner == 'n':
            Terminsave(retfunc,savefunc,nlist)
        else:
            print('let us try that again')
            Terminsave(retfunc,savefunc,nlist)
    else:
        Terminsave(retfunc,savefunc,nlist)







def terminencrypter():  
#  this is the encryption key opening
    from cryptography.fernet import Fernet
    fkey = open('testdocs/filekey.night','rb')
    key = fkey.read()
    print (key)
    cipher = Fernet(key)

#     opens created files to be encrypted and encrypts
    Nocfile= 'testdocs/noclist.night'
    with open(Nocfile,'rb')as e:
        Nocfiletoencrypt = e.read()

        
    Nocencryptedfile = cipher.encrypt(Nocfiletoencrypt) 
    with open(Nocfile,'wb') as ee:
        ee.write(Nocencryptedfile)




def nocupdate(nlist):
#     this creates txt files from list
    with open(f'testdocs\\noclist.night',mode='w')as n:
        for m in range(len(nlist)):
            n.write(f'{nlist[m]}\n')  
    print('files created!')


def goneempfilesaver(retfunc,nlist):
    nocupdate(nlist)
    terminencrypter()
    retfunc()
            






