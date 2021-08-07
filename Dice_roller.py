from tkinter import *
app=Tk()
app.title("Dice Roller Application")
Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}
dice =Label(app,text=Dice[0],font=('Courier',100))
dice.grid(row=0, column=0, padx=40, pady=25)

def Roll():
    from random import randint
    i=randint(1, 6)
    dice_choice=Label(app,text=Dice[i],font=('Courier',100),width=2)
    dice_choice.grid(row=0, column=0, padx=40, pady=25)
    
roll_button=Button(app,text='Roll',command=Roll)
roll_button.grid()

app.mainloop()