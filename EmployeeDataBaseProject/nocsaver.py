
# Terminsave(modeset,goneempfilesaver,noclist)
   
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
    from cryptography.fernet import Fernet
    #     this open encrypter key created by keycreate() as variable
    fkey = open('testdocs/niterun/filekeyMain.night','rb')
    key = fkey.read()
    print (key)
    cipher = Fernet(key)

#     opens created files to be encrypted and encrypts

# >>>>>>>>>>>>>>>>>>>>>
    Nocfile= 'testdocs/noclist.night'
    with open(Nocfile,'rb')as e:
        Nocfiletoencrypt = e.read()


    Nocencryptedfile = cipher.encrypt(Nocfiletoencrypt) 
    with open(Nocfile,'wb') as ee:
        ee.write(Nocencryptedfile)

    with open('testdocs/noclist.night','rb') as df:
        encryptedfile = df.read()
        print(encryptedfile)
        print('>>>>>>>>>>>>>>>>>>>>>>>')
    decrypted_file = cipher.decrypt(encryptedfile)




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