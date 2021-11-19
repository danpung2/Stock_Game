from tkinter import *
import inGame


def goGame():
    start_page.destroy()
    inGame.gameStart()


start_page = Tk()
start_page.geometry('600x600')
start_page.title('게임 메인')

logo = Label(start_page, text='주식투자 게임', font=('', 30), fg='blue3')
start_btn = Button(start_page, text='시작하기', font=('', 20), width='10', height='2', command=goGame)
record_btn = Entry(start_page)
record_txt = Label(start_page, text='날짜 입력 or 선택', font=('', 20), width='10')
money_btn = Entry(start_page)
money_txt = Label(start_page, text='금액 입력 or 선택', font=('', 20), width='10')

logo.place(x=220, y=180)
start_btn.place(x=240, y=240)
record_txt.place(x=230, y=300)
record_btn.place(x=230, y=350)
money_txt.place(x=230, y=400)
money_btn.place(x=230, y=450)


start_page.mainloop()
