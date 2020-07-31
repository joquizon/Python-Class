

curremp=[]
searchlist=[]
notsearch=[]
searchedpos=[]
def editinput():
    curremp.clear()
    searchlist.clear()
    notsearch.clear()
    searchedpos.clear()
    from cryptography.fernet import Fernet
    #     this open encrypter key created by keycreate() as variable
    fkey = open('testdocs/filekey.night','rb')
    key = fkey.read()
    print (key)
    cipher = Fernet(key)

#     opens created files to be encrypted and encrypts
    with open('testdocs/noclist.night','rb') as df:
        encryptedfile = df.read()
        print(encryptedfile)
        print('>>>>>>>>>>>>>>>>>>>>>>>')
    decrypted_file = cipher.decrypt(encryptedfile)
    print(decrypted_file.decode()) 
    noclist = (decrypted_file.decode()).splitlines() 
    searcher= input('employee name:')
    for k in range(len(noclist)):
        if searcher == noclist[k]:
            searchlist.append(noclist[k])
            searchedpos.append(k)
        else:
            notsearch.append(noclist[k])
    if len(searchlist) == 1:
        print('employee found!')
        from cryptography.fernet import Fernet
        fkey = open('testdocs/filekey.night','rb')
        key = fkey.read()
        print (key)
        cipher = Fernet(key)   
        search = searchlist[0]
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
        print(load)
        curremp.append(load)
        print(load2)
        curremp.append(load2)
        print(load3)
        curremp.append(load3)
        print(load4)
        curremp.append(load4)
        for reader in range(len(load)):
            if reader==0:
                print(f'{[reader]}>>>firstname:.....{load[reader]}')
            elif reader==1:
                print(f'{[reader]}>>>lastname:......{load[reader]}')
            elif reader==2:
                print(f'{[reader]}>>>nickname:......{load[reader]}')
            elif reader==3:
                print(f'{[reader]}>>>soc no.:......{load[reader]}')
            elif reader==4:
                print(f'{[reader]}>>>tel no.:......{load[reader]}')
            elif reader==5:
                print(f'{[reader]}>>>address:......{load[reader]}')
            elif reader==6:
                print(f'{[reader]}>>>city:......{load[reader]}')
            elif reader==7:
                print(f'{[reader]}>>>state:......{load[reader]}')
            elif reader==8:
                print(f'{[reader]}>>>zip:......{load[reader]}')
            elif reader==9:
                print(f'{[reader]}>>>hire month:......{load[reader]}')
            elif reader==10:
                print(f'{[reader]}>>>hire date:......{load[reader]}')
            elif reader==11:
                print(f'{[reader]}>>>hire year:......{load[reader]}')
            elif reader==12:
                print(f'{[reader]}>>>department:......{load[reader]}')
            elif reader==13:
                print(f'{[reader]}>>>position:......{load[reader]}')
            elif reader==14:
                print(f'{[reader]}>>>hourly pay:......{load[reader]}')
            elif reader==15:
                print(f'{[reader]}>>>weekly pay:......{load[reader]}')
            elif reader==16:
                print(f'{[reader]}>>>monthly pay:......{load[reader]}')
            elif reader==17:
                print(f'{[reader]}>>>yearly pay:......{load[reader]}')
            elif reader==18:
                print(f'{[reader]}>>>sick days taken:......{load[reader]}')
            elif reader==19:
                print(f'{[reader]}>>>sick days remaining:......{load[reader]}')
            elif reader==20:
                print(f'{[reader]}>>>personal days taken:......{load[reader]}')
            elif reader==21:
                print(f'{[reader]}>>>personal days remaining:......{load[reader]}')
            elif reader==22:
                print(f'{[reader]}>>>vacation days taken:......{load[reader]}')
            elif reader==23:
                print(f'{[reader]}>>>vacation days remaining:......{load[reader]}')
        for reader in range(len(load2)):
            if reader==0:
                print(f'{[reader]}>>>sick dates:......{load2}')
        for reader in range(len(load3)):
            if reader==0:
                print(f'{[reader]}>>>personal dates:......{load3}')
        for reader in range(len(load4)):
            if reader==0:
                print(f'{[reader]}>>>vacation dates:......{load4}')
        print(curremp)
        editinput()
    elif searcher == 'quit':
        quit()
    elif searcher == 'again':
        editinput()
    else:
        print('employee not found!')
        editinput()
    
editinput() 





