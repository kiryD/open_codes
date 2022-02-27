while True:
    menu=input('')
    if menu=='login':
        f=open('log.log','r')
        logoof=f.readline().split(' ')
        f.close()
        loginn=input('Please input your login')
        if loginn==logoof[0]:
            passss=input('GIVE ME YOUR PASSWORD')
            if passss==logoof[1]:
                print(':)')
    if menu=='register':
        f=open('log.log','w')
        login=input('Input login')
        password=input('Input password')
        f.write(login+' '+password)
        f.close()
        