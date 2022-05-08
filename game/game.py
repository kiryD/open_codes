from tkinter import *
import pyautogui

x=2
y=1
game_screenl1=['█','+','█']
game_screenl2=['█','█','█']
game_screenl3=['█','█','█']
game_screen2=[['█','+','█'],
              ['█','█','█'],
              ['█','█','█']]

def left_move():
    for i in range(len(game_screenl1)):
        print(i)
        
root=Tk()
gui_game_screenl1=Label(root,text=game_screenl1)
gui_game_screenl1.pack()
gui_game_screenl2=Label(root,text=game_screenl2)
gui_game_screenl2.pack()
gui_game_screenl3=Label(root,text=game_screenl3)
gui_game_screenl3.pack()
left_button=Button(root,text='←',command=left_move)
left_button.pack()
   

root.mainloop()
