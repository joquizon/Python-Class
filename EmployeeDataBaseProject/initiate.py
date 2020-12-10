import os
def demoend(nlist):
    for x in range (len(nlist)):
        if os.path.exists(f'testdocs/{nlist[x]}.night'):
            os.remove(f'testdocs/{nlist[x]}.night')
            print('file1 deleted!')
            os.remove(f'testdocs/{nlist[x]}sickdates.night')
            print('file2 deleted!')
            os.remove(f'testdocs/{nlist[x]}persdates.night')
            print('file3 deleted!')
            os.remove(f'testdocs/{nlist[x]}vacdates.night')
            print('file4 deleted!')
        else:
            print('no file no delete!')



def resetnoclist():
    import os
    os.remove('testdocs\\noclist.night')
    new = 'testdocs\\noclist.night'
    old = 'testdocs\\noclistog.night'

    os.rename(old,new)