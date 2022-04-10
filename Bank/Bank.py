from tkinter import *
on1=0
on2=0
def creditnumer():
    global on1
    on1=1
    creditnum=ent.get()
    lbl2=Label(text='Правильно?'+creditnum)
def cvv():
    global on2
    cvvv=ent.get()
    on2=1
    lbl1=Label(text='Правильно?' + cvv)
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
window.mainloop()