import os
def demoend():
    fnames=['00','jasonbourne','sarawalker','johncasey','charlesbartowski','jackbauer','tonyroop','gregcosent','macgregorjones','jalenhurts','nicksaban','paulbryant','jimfallon','conanbrian','adamdriver','daisyridley','alecbaldwin','stefftuan','chrisrudolf','kyloren','michaelokeyo','michaeldonaldson','petercamp','justinedean','marybailey','marcsinger','francofranus','chrisvelez','josequizon','jumpasmith','jumpajones','thavonepengpang','paulsingh','jerryspringer','andrewjones','colehenderson','georgest.pierre','lucpetty','toddbryant','robinbanger']
    for x in range (len(fnames)):
        if os.path.exists(f'testdocs/{fnames[x]}D.night'):
            os.remove(f'testdocs/{fnames[x]}D.night')
            print('file1 deleted!')
            os.remove(f'testdocs/{fnames[x]}Dsickdates.night')
            print('file2 deleted!')
            os.remove(f'testdocs/{fnames[x]}Dpersdates.night')
            print('file3 deleted!')
            os.remove(f'testdocs/{fnames[x]}Dvacdates.night')
            print('file4 deleted!')
        else:
            print('no file no delete!')



def freshstart():
    noclist = ['0']

    nocmemlist = [[ '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0'],['0'],['0']]
    nocadder=[]

    def listcreate(list,list2,list3,list4,nlist):
    #     this creates txt files from list
        empname = nlist
        with open(f'testdocs\\noclist.night',mode='w')as n:
            for m in range(len(nocadder)):
                n.write(f'{nocadder[m]}\n')    
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





    def filencrypter(listo):  
    #         from cryptography.fernet import Fernet
    #         key = Fernet.generate_key()
    #         fkey = open('testdocs/filekey.night','wb')
    #         fkey.write(key)
    #         print (key)
    #     this open encrypter key created by keycreate() as variable

        empname = listo
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
        print(decrypted_file.decode())      




    for x in range(len(noclist)):
    		nocadder.append(noclist[x])
    		listcreate(nocmemlist[(x*4)],nocmemlist[(x*4)+1],nocmemlist[(x*4)+2],nocmemlist[(x*4)+3],noclist[x])
    		filencrypter(noclist[x])
