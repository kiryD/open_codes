maxpopularity=100
start=0
while True:
    menu=input('Country simulator. Start. Extra. Exit.')
    if menu=='Start':
        #f=open('save.txt','r')
        #stats=f.readlines()
        stats={'money':5,'popularity':2}
        start=1
        while start==1:
            print('Money : ',+stats['money'],'Population : ',+stats['popularity'])
            action=input('Buy : Food -1$. Buy : Gas -10$. Add territory : -100$. New day +$ -2 Population. Exit.')
            if action=='Food'or action == '1' or action == 'buy food':
                stats['money']=stats['money']-1
                stats['popularity']=stats['popularity']+1
            if action=='Gas' or action=='2':
                stats['money']=stats['money']-10
                stats['popularity']=stats['popularity']+5
            if action=='Add new territory' or action=='3':
                stats['money']=stats['money']-100
                stats['popularity']=stats['popularity']+4
                maxpopularity+=10
            if action=='New day' or action=='0':
                stats['money']=stats['money']+stats['popularity']
                stats['popularity']=stats['popularity']-2
            if stats['popularity']==0 or stats['popularity']<=0:
                input('Game over. Press ENTER')
                start=0
                exit()
            if stats['money']==-1000 or stats['money']<=-1000:
                input('Game over. Press ENTER')
                start=0
                exit()
            if stats['popularity']>=maxpopularity:
                satst=stats['popularity']-maxpopularity
                stats['popularity']-=satst
                print('Max population!')
            if action=='Exit':
                f=open('save.lolsaver','w')
                f.write(stats)
                f.close
                exit()