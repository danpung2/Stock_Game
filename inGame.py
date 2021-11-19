from tkinter import *


def gameStart():
    game_page = Tk()
    game_page.geometry('600x600')
    game_page.title('주식투자 게임중')

    logo = Label(game_page, text='주식투자 게임중 뜰 화면', font=('', 30))

    logo.place(x=160, y=180)

    game_page.mainloop()
