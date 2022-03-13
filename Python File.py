while True:
    delas=input('add del kill')
    f=open('dela.gwsave','r')
    spisok=f.readlines()
    f.close()
    if delas == 'add':
        delaadd=input('')
        f=open('dela.gwsave','a')
        f.write(delaadd)
        f.close()
    if delas=='del':
        f=open('dela.gwsave','w')
        l=int(input('Цифра списка\n'))
        spisok.pop(l)
        for i in range (len(spisok)):
            f.write(spisok[i])
        f.close()
        
