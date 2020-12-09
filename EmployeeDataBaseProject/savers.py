def readytosave(list,list2,list3,list4,confirmfunc,retfunc,savefunc,nlist,mn,dn,yn,ds):
    saver = input('save your entries enter (y) to save enter (n) to go back(<): ')
    if saver == 'y':
        savefunc(list,list2,list3,list4,retfunc,nlist)
    elif saver == 'n':
        confirmfunc()
        readytosave(list,list2,list3,list4,confirmfunc,retfunc,savefunc,nlist,mn,dn,yn,ds)
    elif saver =='<':
        print('going back to the main menu will erase all the data you have entered!!! Are you sure?')
        returner = input('type (y) for yes or (n) for no: ')
        if returner == "y":
            retfunc()
        elif returner == 'n':
            readytosave(list,list2,list3,list4,confirmfunc,retfunc,savefunc,nlist,mn,dn,yn,ds)
        else:
            print('let us try that again')
            readytosave(list,list2,list3,list4,confirmfunc,retfunc,savefunc,nlist,mn,dn,yn,ds)
    else:
        readytosave(list,list2,list3,list4,confirmfunc,retfunc,savefunc,nlist,mn,dn,yn,ds)   







def filencrypter(list):  
#         from cryptography.fernet import Fernet
#         key = Fernet.generate_key()
#         fkey = open('testdocs/niterun/filekeyMain.night','wb')
#         fkey.write(key)
#         print (key)
#     this open encrypter key created by keycreate() as variable

    empname = list[0]+list[1]
#  this is the encryption key opening
    from cryptography.fernet import Fernet
    fkey = open('testdocs/niterun/filekeyMain.night','rb')
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

# >>>>>>>>>>>>>>>>>>>>>
    infofile= 'testdocs/'+ empname +'.night'
    with open(infofile,'rb')as f:
        filetoencrypt = f.read()


    encryptedfile = cipher.encrypt(filetoencrypt) 
    with open(infofile,'wb') as ef:
        ef.write(encryptedfile)


# >>>>>>>>>>>>>>>>>>>>>          
    sickfile= 'testdocs/'+ empname +'sickdates.night'
    with open(sickfile,'rb')as ff:
        sickfiletoencrypt = ff.read()

    sickencryptedfile = cipher.encrypt(sickfiletoencrypt) 
    with open(sickfile,'wb') as eff:
        eff.write(sickencryptedfile)


# >>>>>>>>>>>>>>>>>>>>>          
    persfile= 'testdocs/'+ empname +'persdates.night'
    with open(persfile,'rb')as fff:
        persfiletoencrypt = fff.read()

    persencryptedfile = cipher.encrypt(persfiletoencrypt) 
    with open(persfile,'wb') as efff:
        efff.write(persencryptedfile)


# >>>>>>>>>>>>>>>>>>>>>      
    vacfile= 'testdocs/'+ empname +'vacdates.night'
    with open(vacfile,'rb')as ffff:
        vacfiletoencrypt = ffff.read()

    vacencryptedfile = cipher.encrypt(vacfiletoencrypt) 
    with open(vacfile,'wb') as effff:
        effff.write(vacencryptedfile)

        
    with open('testdocs/'+ empname +'.night','rb') as df:
        encryptedfile = df.read()
        print(encryptedfile)
        print('>>>>>>>>>>>>>>>>>>>>>>>')
    decrypted_file = cipher.decrypt(encryptedfile)           








def listcreate(list,list2,list3,list4,nlist):
#     this creates txt files from list
    empname = list[0]+list[1]
    with open(f'testdocs\\noclist.night',mode='w')as n:
        for m in range(len(nlist)):
            n.write(f'{nlist[m]}\n')    
    with open(f'testdocs\\{empname}.night',mode='w')as t:
        for k in range(len(list)):
            t.write(f'{list[k]}\n')
    with open(f'testdocs\\{empname}sickdates.night',mode='w')as q:
        for r in range(len(list2)):
            q.write(f'{list2[r]}\n')
    with open(f'testdocs\\{empname}persdates.night',mode='w')as s:
        for y in range(len(list3)):
            s.write(f'{list3[y]}\n')
    with open(f'testdocs\\{empname}vacdates.night',mode='w')as h:
        for j in range(len(list4)):
            h.write(f'{list4[j]}\n')
    print('files created!')



def newempfilesaver(list,list2,list3,list4,retfunc,nlist):
    listcreate(list,list2,list3,list4,nlist)
    filencrypter(list)
    retfunc()



def sicpervacfilesaver(list,list2,list3,list4,nlist):
    listcreate(list,list2,list3,list4,nlist)
    filencrypter(list)
#  plae 'nlist.append(empname)' when user says yes to save





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




































    # load = curremp[0]
    #     load2 = curremp[1]
    #     load3 = curremp[2]
    #     load4 = curremp[3]
        
    #     empnamer = curremp[0][0]+curremp[0][1]
    #     noclist[int(searchedpos[0])]= empnamer
    #     with open(f'testdocs\\noclist.night',mode='w')as n:
    #         for m in range(len(noclist)):
    #             n.write(f'{noclist[m]}\n')        
        
    #     with open(f'testdocs\\{empnamer}.night',mode='w')as t:
    #         for k in range(len(load)):
    #             t.write(f'{load[k]}\n')
    #     with open(f'testdocs\\{empnamer}sickdates.night',mode='w')as q:
    #         for r in range(len(load2)):
    #             q.write(f'{load2[r]}\n')
    #     with open(f'testdocs\\{empnamer}persdates.night',mode='w')as s:
    #         for y in range(len(load3)):
    #             s.write(f'{load3[y]}\n')
    #     with open(f'testdocs\\{empnamer}vacdates.night',mode='w')as h:
    #         for j in range(len(load4)):
    #             h.write(f'{load4[j]}\n')         
    #     print('saved')
        
    #     fkey = open('testdocs/niterun/filekeyMain.night','rb')
    #     key = fkey.read()
    #     print (key)
    #     cipher = Fernet(key)
        

    # # >>>>>>>>>>>>>>>>>>>>>>>>>    
    #     Nocfile= 'testdocs/noclist.night'
    #     with open(Nocfile,'rb')as e:
    #         Nocfiletoencrypt = e.read()

    #     Nocencryptedfile = cipher.encrypt(Nocfiletoencrypt) 
    #     with open(Nocfile,'wb') as ee:
    #         ee.write(Nocencryptedfile)  
        
        

    # # >>>>>>>>>>>>>>>>>>>>>
    #     infofileN= 'testdocs/'+ empnamer +'.night'
    #     with open(infofileN,'rb')as f:
    #         fileNtoencrypt = f.read()


    #     encryptedfileN = cipher.encrypt(fileNtoencrypt) 
    #     with open(infofileN,'wb') as ef:
    #         ef.write(encryptedfileN)


    # # >>>>>>>>>>>>>>>>>>>>>          
    #     sickfileN= 'testdocs/'+ empnamer +'sickdates.night'
    #     with open(sickfileN,'rb')as ff:
    #         sickfileNtoencrypt = ff.read()

    #     sickencryptedfileN = cipher.encrypt(sickfileNtoencrypt) 
    #     with open(sickfileN,'wb') as eff:
    #         eff.write(sickencryptedfileN)


    # # >>>>>>>>>>>>>>>>>>>>>          
    #     persfileN= 'testdocs/'+ empnamer +'persdates.night'
    #     with open(persfileN,'rb')as fff:
    #         persfileNtoencrypt = fff.read()

    #     persencryptedfileN = cipher.encrypt(persfileNtoencrypt) 
    #     with open(persfileN,'wb') as efff:
    #         efff.write(persencryptedfileN)


    # # >>>>>>>>>>>>>>>>>>>>>      
    #     vacfileN= 'testdocs/'+ empnamer +'vacdates.night'
    #     with open(vacfileN,'rb')as ffff:
    #         vacfileNtoencrypt = ffff.read()

    #     vacencryptedfileN = cipher.encrypt(vacfileNtoencrypt) 
    #     with open(vacfileN,'wb') as effff:
    #         effff.write(vacencryptedfileN)

    # #/////////////////////////////////////////////////////////////
    #     with open('testdocs/'+ empnamer +'.night','rb') as df:
    #         encryptedfileN = df.read()
    #         print(encryptedfileN)
    #         print('>>>>>>>>>>>>>>>>>>>>>>>')
    #     decrypted_fileN = cipher.decrypt(encryptedfileN)
    #     print(decrypted_fileN.decode())   
    #     EditMenu()