
def Mainsicpervac_Mtn(retfunc,nmlist,sposit):
    sickremove=[]
    PerPremove=[]
    Vacremove=[]

    curremp = nmlist[sposit[0]]

    sicdates=nmlist[sposit[0]+1]
    perdates=nmlist[sposit[0]+2]
    vacdates= nmlist[sposit[0]+3] 

    Sictoremove=[]
    Perstoremove=[]
    Vactoremove=[]

    def Vacdateremover():
        Vremover = input('enter the year of the dates you wish to remove: ')
        if Vremover == '*':
            sicpervac_mtn()
        elif (len(Vremover)) == 2:
            for Vremo in range(len(vacdates)):
                if vacdates[Vremo][-2]+vacdates[Vremo][-1] == Vremover:
                    Vacremove.append(vacdates[Vremo])
                else:
                    pass
            if (len(Vacremove)) > 0:
                print('these are the dates you chose to remove')
                for x in range(len(Vacremove)):
                    print(f'date to be removed .....{Vacremove[x]}')
                
                fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                
                if fwarn == 'y':
                    for Vlisted in range (len(Vacremove)):
                        vacdates.remove(Vacremove[Vlisted])
                    print(vacdates)
                    print('alldone! :)')
                    retfunc()
                elif fwarn =='n':
                    print('cool cool lets try again or you can type (*) to go back to the previous menu')
                    Vacdateremover()
            else:
                print('sorry i did not find that year!Try again')
                Vacdateremover()
        elif (len(Vremover)) == 1:
            Vremover1= '/'+Vremover
            for Vremo in range(len(vacdates)):
                if vacdates[Vremo][-2]+vacdates[Vremo][-1] == Vremover1:
                    Vacremove.append(vacdates[Vremo])
                else:
                    pass
            if (len(Vacremove)) > 0:
                print('these are the dates you chose to remove')
                for x in range(len(Vacremove)):
                    print(f'date to be removed .....{Vacremove[x]}')
                
                fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                
                if fwarn == 'y':
                    for Vlisted in range (len(Vacremove)):
                        vacdates.remove(Vacremove[Vlisted])
                    print(vacdates)
                elif fwarn =='n':
                    print('cool cool lets try again or you can type (*) to go back to the previous menu')
                    Vacdateremover()
            else:
                print('sorry i did not find that year!Try again')
                Vacdateremover()
        elif remover == '*':
            morevacentries()
        else:
            print('sorry that is not on the list:)')
            dateremover()

            
            
    def specVac():
            Vactoremove.clear()
            datepicker = input('type the line no. of the date you wish to remove').lower()
            for dp in range(len(vacdates)):
                if str(dp) == datepicker:
                    Vactoremove.append(vacdates[dp])
                    print('got it')
                else:
                    pass
            if len(Vactoremove)>0:
                ffwarn = input(f' the  date {Vactoremove} will now be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ').lower()
                if ffwarn == 'y':
                    vacdates.pop(int(datepicker))
                    for sd in range(len(vacdates)):
                        print(f'{sd}.....{vacdates[sd]}')
                    curremp[22] = int(curremp[22]) - 1
                    curremp[23] = int(curremp[23]) + 1
                    print(f'{curremp[0]} {curremp[1]} has regained 1 Vacday')
                    print('great! that is done you can enter another date or type (*) to go back to the previous menu or type (s) to save your changes')
                    specVac()
                elif ffwarn == 'n':
                    print('ok cool you can enter another date or type (*) to go back to the previous menu')
                    specVac()
            elif datepicker == '*':
                Vacdatechoice()
            elif datepicker == 's':        
                retfunc()
            else:
                print('sorry I could not find the date let me try another date or type (*) to go back to the previous menu')
                specVac()    
                    
            
            
    def Vacdatechoice():
        for sd in range(len(vacdates)):
            print(f'{sd}.....{vacdates[sd]}')
        schoice= input('type (1) to remove a specific date or type (2) to remove all dates from a specific year or  type (*) to go back to the previous menu: ')
        if schoice == '1':
            specVac()
        elif schoice =='2':
            Vacdateremover()
        elif schoice == '*':
            sicpervac_mtn()
        else:
            print('beep boop beep does not compute beep boop beep try again!')
            Vacdatechoice()
    def Persdateremover():
        Premover = input('enter the year of the dates you wish to remove: ')
        if Premover == '*':
            sicpervac_mtn()
        elif (len(Premover)) == 2:
            for Premo in range(len(perdates)):
                if perdates[Premo][-2]+perdates[Premo][-1] == Premover:
                    PerPremove.append(perdates[Premo])
                else:
                    pass
            if (len(PerPremove)) > 0:
                print('these are the dates you chose to remove')
                for x in range(len(PerPremove)):
                    print(f'date to be removed .....{PerPremove[x]}')
                
                fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                
                if fwarn == 'y':
                    for Plisted in range (len(PerPremove)):
                        perdates.remove(PerPremove[Plisted])
                    print(perdates)
                    print('alldone! :)')
                    retfunc()
                elif fwarn =='n':
                    print('cool cool lets try again or you can type (*) to go back to the previous menu')
                    Persdateremover()
            else:
                print('sorry i did not find that year!Try again')
                Persdateremover()
        elif (len(Premover)) == 1:
            Premover1= '/'+Premover
            for Premo in range(len(perdates)):
                if perdates[Premo][-2]+perdates[Premo][-1] == Premover1:
                    PerPremove.append(perdates[Premo])
                else:
                    pass
            if (len(PerPremove)) > 0:
                print('these are the dates you chose to remove')
                for x in range(len(PerPremove)):
                    print(f'date to be removed .....{PerPremove[x]}')
                
                fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                
                if fwarn == 'y':
                    for Plisted in range (len(PerPremove)):
                        perdates.remove(PerPremove[Plisted])
                    print(perdates)
                elif fwarn =='n':
                    print('cool cool lets try again or you can type (*) to go back to the previous menu')
                    Persdateremover()
            else:
                print('sorry i did not find that year!Try again')
                Persdateremover()
        elif remover == '*':
            morevacentries()
        else:
            print('sorry that is not on the list:)')
            dateremover()

            
            
    def specPers():
            Perstoremove.clear()
            datepicker = input('type the line no. of the date you wish to remove').lower()
            for dp in range(len(perdates)):
                if str(dp) == datepicker:
                    Perstoremove.append(perdates[dp])
                    print('got it')
                else:
                    pass
            if len(Perstoremove)>0:
                ffwarn = input(f' the  date {Perstoremove} will now be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ').lower()
                if ffwarn == 'y':
                    perdates.pop(int(datepicker))
                    for sd in range(len(perdates)):
                        print(f'{sd}.....{perdates[sd]}')
                    curremp[20] = int(curremp[20]) - 1
                    curremp[21] = int(curremp[21]) + 1
                    print(f'{curremp[0]} {curremp[1]} has regained 1 Persday')
                    print('great! that is done you can enter another date or type (*) to go back to the previous menu or type (s) to save your changes')
                    specPers()
                elif ffwarn == 'n':
                    print('ok cool you can enter another date or type (*) to go back to the previous menu')
                    specPers()
            elif datepicker == '*':
                Persdatechoice()
            elif datepicker == 's':        
                retfunc()
            else:
                print('sorry I could not find the date let me try another date or type (*) to go back to the previous menu')
                specPers()    
                    
            
            
    def Persdatechoice():
        for sd in range(len(perdates)):
            print(f'{sd}.....{perdates[sd]}')
        schoice= input('type (1) to remove a specific date or type (2) to remove all dates from a specific year or  type (*) to go back to the previous menu: ')
        if schoice == '1':
            specPers()
        elif schoice =='2':
            Persdateremover()
        elif schoice == '*':
            sicpervac_mtn()
        else:
            print('beep boop beep does not compute beep boop beep try again!')
            Persdatechoice()
    def sickdateremover():
        Sremover = input('enter the year of the dates you wish to remove: ')
        if Sremover == '*':
            sicpervac_mtn()
        elif (len(Sremover)) == 2:
            for Sremo in range(len(sicdates)):
                if sicdates[Sremo][-2]+sicdates[Sremo][-1] == Sremover:
                    sickremove.append(sicdates[Sremo])
                else:
                    pass
            if (len(sickremove)) > 0:
                print('these are the dates you chose to remove')
                for x in range(len(sickremove)):
                    print(f'date to be removed .....{sickremove[x]}')
                
                fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                
                if fwarn == 'y':
                    for Slisted in range (len(sickremove)):
                        sicdates.remove(sickremove[Slisted])
                    print(sicdates)
                    print('alldone! :)')
                    retfunc()
                elif fwarn =='n':
                    print('cool cool lets try again or you can type (*) to go back to the previous menu')
                    sickdateremover()
            else:
                print('sorry i did not find that year!Try again')
                sickdateremover()
        elif (len(Sremover)) == 1:
            Sremover1= '/'+Sremover
            for Sremo in range(len(sicdates)):
                if sicdates[Sremo][-2]+sicdates[Sremo][-1] == Sremover1:
                    sickremove.append(sicdates[Sremo])
                else:
                    pass
            if (len(sickremove)) > 0:
                print('these are the dates you chose to remove')
                for x in range(len(sickremove)):
                    print(f'date to be removed .....{sickremove[x]}')
                
                fwarn = input('these will be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ')
                
                if fwarn == 'y':
                    for Slisted in range (len(sickremove)):
                        sicdates.remove(sickremove[Slisted])
                    print(sicdates)
                elif fwarn =='n':
                    print('cool cool lets try again or you can type (*) to go back to the previous menu')
                    sickdateremover()
            else:
                print('sorry i did not find that year!Try again')
                sickdateremover()
        elif remover == '*':
            morevacentries()
        else:
            print('sorry that is not on the list:)')
            dateremover()

            
            
    def specsick():
            Sictoremove.clear()
            datepicker = input('type the line no. of the date you wish to remove').lower()
            for dp in range(len(sicdates)):
                if str(dp) == datepicker:
                    Sictoremove.append(sicdates[dp])
                    print('got it')
                else:
                    pass
            if len(Sictoremove)>0:
                ffwarn = input(f' the  date {Sictoremove} will now be removed permanently. Are you sure about this? type (y) for yes Or type (n) for no: ').lower()
                if ffwarn == 'y':
                    sicdates.pop(int(datepicker))
                    for sd in range(len(sicdates)):
                        print(f'{sd}.....{sicdates[sd]}')
                    curremp[18] = int(curremp[18]) - 1
                    curremp[19] = int(curremp[19]) + 1
                    print(f'{curremp[0]} {curremp[1]} has regained 1 sickday')
                    print('great! that is done you can enter another date or type (*) to go back to the previous menu or type (s) to save your changes')
                    specsick()
                elif ffwarn == 'n':
                    print('ok cool you can enter another date or type (*) to go back to the previous menu')
                    specsick()
            elif datepicker == '*':
                sickdatechoice()
            elif datepicker == 's':        
                retfunc()
            else:
                print('sorry I could not find the date let me try another date or type (*) to go back to the previous menu')
                specsick()    
                    
            
            
    def sickdatechoice():
        for sd in range(len(sicdates)):
            print(f'{sd}.....{sicdates[sd]}')
        schoice= input('type (1) to remove a specific date or type (2) to remove all dates from a specific year or  type (*) to go back to the previous menu: ')
        if schoice == '1':
            specsick()
        elif schoice =='2':
            sickdateremover()
        elif schoice == '*':
            sicpervac_mtn()
        else:
            print('beep boop beep does not compute beep boop beep try again!')
            sickdatechoice()


            
    def sicpervac_mtn():
        for s in range(len(sicdates)):
            print(f'Sick date: {sicdates[s]}')
        for p in range(len(perdates)):
            print(f'Personal date: {perdates[p]}')
        for v in range(len(vacdates)):
            print(f'Vacation date: {vacdates[v]}')
        
        mtnchoice = input('pls choose which set you would like to edit.\nEnter: (1) for sickdates (2) for personal dates (3) for vacation dates: ')
        if mtnchoice == '*':
            retfunc
        elif mtnchoice == '1':
            sickdatechoice()
        elif mtnchoice == '2':
            Persdatechoice()
        elif mtnchoice == '3':
            Vacdatechoice()
        else:
            print('that is not on the list')
            sicpervac_mtn()
    sicpervac_mtn()