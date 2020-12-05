noclist = []

nocmemlist = []

nocadder=[]

import random

empbox = []
sickdates =[['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA']]
persdates =[['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA']]
vacdates =[['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA'],['AA']]


names=[['0','0','0'],['jason','bourne','jabo'],['sara','walker','yvon'],['john','casey','jcas'],['charles','bartowski','chuk'],['jack','bauer','jbow'],['tony','roop','troo'],['greg','cosent','gcos'],['macgregor','jones','macj'],['jalen','hurts','jhur'],['nick','saban','nsab'],['paul','bryant','pbry'],['jim','fallon','jimy'],['conan','brian','cone'],['adam','driver','sith'],['daisy','ridley','drid'],['alec','baldwin','bald'],['steff','tuan','stef'],['chris','rudolf','crud'],['kylo','ren','kyre'],['michael','okeyo','mike'],['michael','donaldson','mdon'],['peter','camp','gunn'],['justine','dean','jusd'],['mary','bailey','bail'],['marc','singer','funk'],['franco','franus','fran'],['chris','velez','slam'],['jose','quizon','chic'],['jumpa','smith','jusm'],['jumpa','jones','jujo'],['thavone','pengpang','peng'],['paul','singh','psin'],['jerry','springer','jspr'],['andrew','jones','anjo'],['cole','henderson','heno'],['george','st.pierre','gstp'],['luc','petty','lpet'],['todd','bryant','tbry'],['robin','banger','bang']]
areac = ['718','212','917','914']
stype = ['avenue','road','street']
borough = ['manhattan','queens','staten island','bronx','brooklyn']
zipcode = [['10001','10011','10018','10019','10020'],['11354','11355','11356','11357','11358'],['10306','10307','10308','10309','10312'],['10461','10462','10464','10465','10472'],['11201','11205','11215','11217','11231']]




dept= ['hsk','FD','eng','pbx','sle','acct']
deptpos =[['*deptmgr','*adeptmgr','*deptsup','hskper','hseman'],['*deptmgr','*adeptmgr','*ntmgr','deptsup','ntaud','fdagnt','bllmn','drmn'],['*deptmgr','*adeptmgr','*deptsup','engnr'],['*deptmgr','*adeptmgr','*deptsup','oprtr'],['*deptmgr','*adeptmgr','*deptsup','res'],['*cntrller','*asscntrller','acctnt']]


for emp in range(len(names)):
    xsoc = random.randint(100000000,999999999)

    xarea = random.randint(0,3)
    xtelp = random.randint(100,999)
    xtels = random.randint(1000,9999)

    xbuildno = random.randint(1,300)
    xstreetno = random.randint(1,140)
    xstreetype = random.randint(0,2)
    xbtype = random.randint(0,4)
    xziptype = zipcode[xbtype][random.randint(0,4)]

    xmonth = random.randint(1,12)
    xday = random.randint(1,28)
    xyear = random.randint(4,19)

    xdep = random.randint(0,5)
    xdepos = random.randint(0,((len(deptpos[xdep]))-1))

    xpay = random.randint(17,30)

    xsicktk = random.randint(0,6)
    xperstk = random.randint(0,3)
    xvactk = random.randint(0,15)

    names[emp].append(str(xsoc))
    names[emp].append((str(xarea))+(str(xtelp))+(str(xtels)))
    names[emp].append(str(xbuildno)+' '+str(xstreetno)+' '+stype[xstreetype])
    names[emp].append(borough[xbtype])
    names[emp].append('NY')
    names[emp].append(xziptype)
    names[emp].append(xmonth)
    names[emp].append(xday)
    names[emp].append(xyear)
    names[emp].append(dept[xdep])
    names[emp].append(deptpos[xdep][xdepos])
    names[emp].append(str(xpay))
    names[emp].append(str(xpay*40))
    names[emp].append(str((xpay*40)*4))
    names[emp].append(str((xpay*40)*52))
    names[emp].append(str(xsicktk))
    names[emp].append(str(6-xsicktk))
    names[emp].append(str(xperstk))
    names[emp].append(str(3-xperstk))
    names[emp].append(str(xvactk))
    names[emp].append(str(15-xvactk))

    for z in range(xsicktk):
        sickdates[emp].append((str(random.randint(1,12)))+'/'+(str(random.randint(1,28)))+'/19')
    for zz in range(xperstk):
        persdates[emp].append((str(random.randint(1,12)))+'/'+(str(random.randint(1,28)))+'/19')
    for zzz in range(xvactk):
        vacdates[emp].append((str(random.randint(1,12)))+'/'+(str(random.randint(1,28)))+'/19')

for rost in range(len(names)):
    nocmemlist.append(names[rost])
    nocmemlist.append(sickdates[rost])
    nocmemlist.append(persdates[rost])
    nocmemlist.append(vacdates[rost])

for rostname in range(len(names)):
    noclist.append(names[rostname][0]+names[rostname][1])

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



print(noclist)
print(nocmemlist)
for x in range(len(noclist)):
		nocadder.append(noclist[x])
		listcreate(nocmemlist[(x*4)],nocmemlist[(x*4)+1],nocmemlist[(x*4)+2],nocmemlist[(x*4)+3],noclist[x])
		filencrypter(noclist[x])
