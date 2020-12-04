import random
rosterbox = []
empbox = []
sickdates = []
persdates = []
vacadates = []


names=[['0','0','0'],['jason','bourne','jabo'],['sara','walker','yvon'],['john','casey','jcas'],['charles','bartowski','chuk'],['jack','bauer','jbow'],['tony','roop','troo'],['greg','cosent','gcos'],['macgregor','jones','macj'],['jalen','hurts','jhur'],['nick','saban','nsab'],['paul','bryant','pbry'],['jim','fallon','jimy'],['conan','brian','cone'],['adam','driver','sith'],['daisy','ridley','drid'],['alec','baldwin','bald'],['steff','tuan','stef'],['chris','rudolf','crud'],['kylo','ren','kyre'],['michael','okeyo','mike'],['michael','donaldson','mdon'],['peter','camp','gunn'],['justine','dean','jusd'],['mary','bailey','bail'],['marc','singer','funk'],['franco','franus','fran'],['chris','velez','slam'],['jose','quizon','chic'],['jumpa','smith','jusm'],['jumpa','jones','jujo'],['thavone','pengpang','peng'],['paul','singh','psin'],['jerry','springer','jspr'],['andrew','jones','anjo'],['cole','henderson','heno'],['george','st.pierre','gstp'],['luc','petty','lpet'],['todd','bryant','tbry'],['robin','banger','bang']
areac = ['718','212','917','914']
stype = ['avenue','road','street']
borough = ['manhattan','queens','staten island','bronx','brooklyn']
zipcode = [['10001','10011','10018','10019','10020'],['11354','11355','11356','11357','11358'],['10306','10307','10308','10309','10312'],['10461','10462','10464','10465','10472'],['11201','11205','11215','11217','11231']]




dept= ['hsk','FD','eng','pbx','sle','acct']
deptpos =[['*deptmgr','*adeptmgr','*deptsup','hskper','hseman'],['*deptmgr','*adeptmgr','*ntmgr','deptsup','ntaud','fdagnt','bllmn','drmn'],['*deptmgr','*adeptmgr','*deptsup','engnr'],['*deptmgr','*adeptmgr','*deptsup','oprtr'],['*deptmgr','*adeptmgr','*deptsup','res'],['*cntrller','*asscntrller','acctnt']]


for emp in range(40):
	xname = random.randint(0,39)
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
	xdepos = random.randint(0,(lendeptpos[xdep]))

	xpay = random.randint(17,30)

	empbox.append(names[xname][0])
	empbox.append(names[xname][1])
	empbox.append(names[xname][2])
	empbox.append(xsoc)
	empbox.append((str(xarea))+(str(xtelp))+(str(xtels)))
	empbox.append()
	empbox.append()
	empbox.append()
	empbox.append()
	empbox.append()
	empbox.append()










