from tkinter import *

x=-1
y=-1
ex=-1
ey=-1
enemy=0
game_object_enemy='☻'
game_object_wall='█'
game_object_player='+'
game_screenl1=['█','+','█']
game_screenl2=['█','█','█']
game_screenl3=['█','☻','█']
game_screen2=[['█','+','█'],
              ['█','█','█'],
              ['█','☻','█']]

def left_move():
    global enemy
    for stroka in game_screen2:
        for kletka in stroka:
            print(kletka,end='')
        print()
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='+':
                print(i)
                x=i
                y=o
    game_screen2[x][y]=game_object_wall
    if y == 0:
        y=y-1
    game_screen2[x][y-1]=game_object_player
    
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='☻':
                print(i)
                ex=i
                ey=o
            elif enemy!=0:
                exit()
    game_screen2[ex][ey]=game_object_wall
    if ey == 0:
        ey=ey-1
    game_screen2[ex][ey+1]=game_object_enemy
    game_screenl1=game_screen2[0]
    game_screenl2=game_screen2[1]
    game_screenl3=game_screen2[2]
    gui_game_screenl1.configure(text=game_screenl1)
    gui_game_screenl2.configure(text=game_screenl2)
    gui_game_screenl3.configure(text=game_screenl3)
def right_move():
    global enemy
    for stroka in game_screen2:
        for kletka in stroka:
            print(kletka,end='')
        print()
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='+':
                print(i)
                x=i
                y=o
    game_screen2[x][y]=game_object_wall
    if y == 2:
        y=y-1
    
    game_screen2[x][y+1]=game_object_player
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='☻':
                print(i)
                ex=i
                ey=o
            elif enemy!=0:
                exit()
    game_screen2[ex][ey]=game_object_wall
    if ey == 0:
        ey=ey+1
    game_screen2[ex][ey-1]=game_object_enemy
    game_screenl1=game_screen2[0]
    game_screenl2=game_screen2[1]
    game_screenl3=game_screen2[2]
    gui_game_screenl1.configure(text=game_screenl1)
    gui_game_screenl2.configure(text=game_screenl2)
    gui_game_screenl3.configure(text=game_screenl3)
def up_move():
    global enemy
    for stroka in game_screen2:
        for kletka in stroka:
            print(kletka,end='')
        print()
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='+':
                print(i)
                x=i
                y=o
    game_screen2[x][y]=game_object_wall
    if x == 0:
        x=x+1
    game_screen2[x-1][y]=game_object_player
    ex=0
    ey=0
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='☻':
                print(i)
                ex=i
                ey=o
                enemy+1
            elif enemy!=0:
                exit()
    game_screen2[ex][ey]=game_object_wall
    if ex == 0:
        ex=ex-1
    game_screen2[ex+1][ey]=game_object_enemy
    game_screenl1=game_screen2[0]
    game_screenl2=game_screen2[1]
    game_screenl3=game_screen2[2]
    gui_game_screenl1.configure(text=game_screenl1)
    gui_game_screenl2.configure(text=game_screenl2)
    gui_game_screenl3.configure(text=game_screenl3)
def down_move():
    global enemy
    for stroka in game_screen2:
        for kletka in stroka:
            print(kletka,end='')
        print()
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='+':
                print(i)
                x=i
                y=o
    game_screen2[x][y]=game_object_wall
    if x == 2:
        x=x-1
    game_screen2[x+1][y]=game_object_player
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='☻':
                print(i)
                ex=i
                ey=o
            elif enemy!=0:
                exit()
    game_screen2[ex][ey]=game_object_wall
    if ex == 0:
        ex=ex+1
    game_screen2[ex-1][ey]=game_object_enemy
    game_screenl1=game_screen2[0]
    game_screenl2=game_screen2[1]
    game_screenl3=game_screen2[2]
    gui_game_screenl1.configure(text=game_screenl1)
    gui_game_screenl2.configure(text=game_screenl2)
    gui_game_screenl3.configure(text=game_screenl3)
def fire_move():
    global enemy
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='+':
                print(i)
                x=i
                y=o
    for i in range(len(game_screen2)):
        for o in range(len(game_screen2)):
            if game_screen2[i][o]=='☻':
                print(i)
                ex=i
                ey=o
                enemy+1
            elif enemy!=0:
                exit()
    if game_screen2[x-1][y-1]=='☻' or game_screen2[x-1][y]=='☻' or game_screen2[x-1][y+1]=='☻' or game_screen2[x][y-1]=='☻'or game_screen2[x][y]=='☻' or game_screen2[x][y+1]=='☻'or game_screen2[x+1][y-1]=='☻'or game_screen2[x+1][y]=='☻' or game_screen2[x+1][y+1]=='☻':
        enemy=0
        game_screen2[ex][ey]=game_object_wall
    game_screenl1=game_screen2[0]
    game_screenl2=game_screen2[1]
    game_screenl3=game_screen2[2]
    gui_game_screenl1.configure(text=game_screenl1)
    gui_game_screenl2.configure(text=game_screenl2)
    gui_game_screenl3.configure(text=game_screenl3)
    
root=Tk()
gui_game_screenl1=Label(root,text=game_screenl1)
gui_game_screenl1.pack()
gui_game_screenl2=Label(root,text=game_screenl2)
gui_game_screenl2.pack()
gui_game_screenl3=Label(root,text=game_screenl3)
gui_game_screenl3.pack()
left_button=Button(root,text='←',command=left_move)
left_button.pack(side=LEFT)
right_button=Button(root,text='→',command=right_move)
right_button.pack(side=RIGHT)
right_button=Button(root,text='↓',command=down_move)
right_button.pack(side=BOTTOM)
right_button=Button(root,text='↑',command=up_move)
right_button.pack(side=TOP)
right_button=Button(root,text='●',command=fire_move)
right_button.pack(side=BOTTOM)

root.mainloop()

