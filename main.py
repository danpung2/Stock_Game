from tkinter import *
import inGame
import GUI

def goGame():
    start_page.destroy()
    GUI.gameStart(int(start_date.get()), int(balance.get()))


start_page = Tk()
start_page.geometry('600x600')
start_page.title('게임 메인')

balance = StringVar()
start_date = StringVar()

logo = Label(start_page, text='주식투자 게임', font=('', 30), fg='blue3')
start_btn = Button(start_page, text='시작하기', font=('', 20), width='10', height='2', command=goGame)
record_txt = Label(start_page, text='날짜 입력 or 선택', font=('', 20), width='10')
start_date_btn1 = Radiobutton(start_page, text = "7일", variable=start_date, value = 7)
start_date_btn2 = Radiobutton(start_page, text = "9일", variable=start_date, value = 9)
start_date_btn3 = Radiobutton(start_page, text = "12일", variable=start_date, value = 12)

money_txt = Label(start_page, text='금액 입력 or 선택', font=('', 20), width='10')
start_capital_btn1 = Radiobutton(start_page, text = "1,000,000원", variable=balance, value = 1000000)
start_capital_btn2 = Radiobutton(start_page, text = "2,000,000원", variable=balance, value = 2000000)
start_capital_btn3 = Radiobutton(start_page, text = "3,000,000원", variable=balance, value = 3000000)

logo.place(x=220, y=180)
start_btn.place(x=240, y=240)
record_txt.place(x=230, y=300)
start_date_btn1.place(x=230, y=350)
start_date_btn2.place(x=230, y=370)
start_date_btn3.place(x=230, y=390)
money_txt.place(x=230, y=420)
start_capital_btn1.place(x=230, y=470)
start_capital_btn2.place(x=230, y=490)
start_capital_btn3.place(x=230, y=510)


start_page.mainloop()
