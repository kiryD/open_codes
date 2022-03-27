import random
HOC=15
b=10
maxpopularity=100
start=0
while True:
    menu=input('Country simulator. Start. Extra. Exit.')
    if menu=='Start':
        #f=open('save.txt','r')
        #stats=f.readlines()
        stats={'money':5,'population':2}
        start=1
        while start==1:
            print('Money : ',+stats['money'],'Population : ',+stats['population'])
            action=input('Buy : Food -1$. Buy : Gas -10$. Add territory : -100$. Open war menu. New day +$ -2 Population. Exit.')
            if action=='Food'or action == '1' or action == 'buy food':
                stats['money']=stats['money']-1
                stats['population']=stats['population']+1
            if action=='Gas' or action=='2':
                stats['money']=stats['money']-10
                stats['population']=stats['population']+5
            if action=='Add new territory' or action=='3':
                stats['money']=stats['money']-100
                stats['population']=stats['population']+4
                maxpopularity+=10
            if action=='Open war menu' or action=='ow':
                war_open=1
                while war_open==1:
                    war_action=input('Start war. Buy amunition. Exit.')
                    if war_action=='1':
                        war_started=input('Attack : 1 of 10 Win. Block : -1 HOC. Leave : -100 Population.')
                        if war_started=='1':
                            win_chance=random.randint(0,b)
                            if win_chance==10:
                                stats['population']+=100
                                war_open=0
                            else:
                                HOC-=10
                        if HOC==0 or HOC>=0:
                            break
                            exit()
                        if war_action=='2':
                            HOC-=1
                        if war_started=='3':
                            stats['population']-=100
                            break
                    if war_action=='2':
                        stats['money']-=1000
                        if b!=1:
                            b-=1
                    if war_action=='3':
                            break
            if action=='New day' or action=='0':
                stats['money']=stats['money']+stats['population']
                stats['population']=stats['population']-2
            if stats['population']==0 or stats['population']<=0:
                input('Game over. Press ENTER')
                start=0
                exit()
            if stats['money']==-1000 or stats['money']<=-1000:
                input('Game over. Press ENTER')
                start=0
                exit()
            if stats['population']>=maxpopularity:
                satst=stats['population']-maxpopularity
                stats['population']-=satst
                print('Max population!')
            if action=='Exit':
                break
                exit()
    if menu=='Extra' or menu=='2':
        print('Press f3 to win')