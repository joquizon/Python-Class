def clearscreen():
    import os
    from os import system
    clear = lambda: system('cls')
    clear()
# noclist is list
#elist is big giant nocmemlist
# nocmemlist =[]
# x = 'noclist'
def employeeloader(nlist,elist):
    from cryptography.fernet import Fernet
    fkey = open('testdocs/niterun/filekeyMain.night','rb')
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
        fkey = open('testdocs/niterun/filekeyMain.night','rb')
        key = fkey.read()
        cipher = Fernet(key)   
        search = stringnlist[emp]
        with open('testdocs/'+search+'.night','rb') as et:
            encryptedfileA = et.read()
        decrypted_fileA = cipher.decrypt(encryptedfileA)

        with open('testdocs/'+search+'sickdates.night','rb') as ms:
            encryptedfileB = ms.read()
        decrypted_fileB = cipher.decrypt(encryptedfileB)

        with open('testdocs/'+search+'persdates.night','rb') as lm:
            encryptedfileC = lm.read()
        decrypted_fileC = cipher.decrypt(encryptedfileC)

        with open('testdocs/'+search+'vacdates.night','rb') as nh:
            encryptedfileD = nh.read()
        decrypted_fileD = cipher.decrypt(encryptedfileD)

        load = (decrypted_fileA.decode()).splitlines() 
        load2 = (decrypted_fileB.decode()).splitlines() 
        load3 = (decrypted_fileC.decode()).splitlines() 
        load4 = (decrypted_fileD.decode()).splitlines() 

        elist.append(load)
        elist.append(load2)
        elist.append(load3)
        elist.append(load4)






# >>>>>>>>>>>>>>>>>>>>>>>Edits noclist basically fires employees
def terminator(list):
    for x in range(len(list)):
        print(f"{x}....{list[x]}")
    connor = input('typed the line no. of the employee you wish to tuhminate or if termination is over type <*>:')
    if connor == '*':
        print('Termination Over')
    else:
        while True:
            try:
                connorno = int(connor)
                if connorno <= len(list):
                    clearscreen()
                    print(f'hasta la vista {list[connorno]}')
                    list.pop(connorno)
                    for x in range(len(list)):
                        print(f"{x}....{list[x]}")
                    terminator(list)
                else:
                    print('nooooo')
                    terminator(list)
            except ValueError :
                print('Exceptumondo Dude! this thing just takes numbers!!!Try again!')
                terminator(list)
                break
            else:
                break
            






