import random
import tkinter.font as tk_font
from tkinter import *
from commodities import Commodities
from user import User
import gameOver


def gameStart(start_date, start_balance):
    total_current_cost = 0

    player = User(0, int(start_balance), int(start_date))

    window = Tk()
    window.geometry('1000x800')
    window.title('투자 게임')

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    if total_current_cost == 0:
        balance = start_balance
        total_purchase_cost = 0
        total = start_balance
        var1.set(total)
        var2.set(balance)
        var3.set(total_purchase_cost)

    item = {1: Commodities(10000), 2: Commodities(20000), 3: Commodities(30000), 4: Commodities(40000)}

    current_date = start_date - player.date + 1

    var4.set("아침")

    canvas = Canvas(window)

    date_font = tk_font.Font(size=15)
    trade_font = tk_font.Font(size=18)
    buy_label_font = tk_font.Font(size=20)
    title_font = tk_font.Font(size=60, weight='bold')
    capital_font = tk_font.Font(size=20)
    rate_font = tk_font.Font(size=15)
    report_font = tk_font.Font(size=30)

    # 날짜

    date_lb = Label(window,
                    text='{1}일차/{0}일'.format(start_date, current_date),
                    font=date_font)
    date_lb.place(x=50, y=50)

    date_2b = Label(window,
                    text=var4.get(),
                    font=date_font)
    date_2b.place(x=50, y=80)

    # 게임 이름

    title = Label(window,
                  text='Stock Game',
                  font=title_font)
    title.place(x=50, y=150)

    # 총 자본, 지갑, 투자액

    capital_lb1 = Label(window,
                        text='총 자본    : {}'.format(player.total),
                        font=capital_font)
    capital_lb1.place(x=700, y=50)

    wallet_lb1 = Label(window,
                       text='지갑        : {}'.format(player.wallet),
                       font=capital_font)
    wallet_lb1.place(x=700, y=85)

    investment_lb1 = Label(window,
                           text='총 투자액 : {}'.format(player.investment),
                           font=capital_font)
    investment_lb1.place(x=700, y=120)

    def buy(item_num, buy_num):
        buy_num_int = int(buy_num)
        if player.wallet < buy_num_int * item[item_num].price:
            num_ent1.delete(0, END)
            num_ent2.delete(0, END)
            num_ent3.delete(0, END)
            num_ent4.delete(0, END)
            return
        else:
            item[item_num].update_num(buy_num_int)
            player.update(item[item_num].price * buy_num_int)
            wallet_lb1.configure(text='지갑        : {0}'.format(player.wallet))
            investment_lb1.configure(text='총 투자액 : {0}'.format(player.investment))
            update()

    def sell(item_num, sell_num):

        sell_num_int = int(sell_num)
        if item[item_num].num < sell_num_int:
            num_ent1.delete(0, END)
            num_ent2.delete(0, END)
            num_ent3.delete(0, END)
            num_ent4.delete(0, END)
            return
        else:
            item[item_num].update_num(-sell_num_int)
            player.update(-(item[item_num].price * sell_num_int))
            wallet_lb1.configure(text='지갑        : {0}'.format(player.wallet))
            investment_lb1.configure(text='총 투자액 : {0}'.format(player.investment))
            capital_lb1.configure(text='총 자본    :{0}'.format(player.total))
            update()

    def update():
        num_ent1.delete(0, END)
        num_ent2.delete(0, END)
        num_ent3.delete(0, END)
        num_ent4.delete(0, END)
        my_invest_lb1.configure(text='종목1: {0} / 보유액: {1}'.format(item[1].num, item[1].total))
        my_invest_lb2.configure(text='종목2: {0} / 보유액: {1}'.format(item[2].num, item[2].total))
        my_invest_lb3.configure(text='종목3: {0} / 보유액: {1}'.format(item[3].num, item[3].total))
        my_invest_lb4.configure(text='종목4: {0} / 보유액: {1}'.format(item[4].num, item[4].total))

    def next_turn():
        if player.time == 2:
            player.update_date()
            player.update_time()
            var4.set('아침')
        elif player.time == 0:
            player.update_time()
            var4.set('점심')
        else:
            player.update_time()
            var4.set('저녁')
        date_lb.configure(text='{1}일차/{0}일'.format(start_date, start_date - player.date + 1))
        date_2b.configure(text=var4.get())
        update()
        rate_of_fluctuation()
        amount_of_investment = 0
        for index in range(1, 5):
            amount_of_investment += item[index].total
        player.update_rate(amount_of_investment)

        if player.date == 0:
            window.destroy()
            gameOver.gameOver(player.total, player.investment, player.wallet, (player.total/start_balance * 100) - 100)

    def item_update(index, fluctuation):
        item[index].update_price(fluctuation)

    def rate_of_fluctuation():
        for index in range(1, 5):
            fluctuation = random.randint(1, 10)
            up_down = random.randint(1, 2)
            if up_down == 1:
                item_update(index, fluctuation)
            else:
                item_update(index, -fluctuation)

        current_ent1.configure(text='{}'.format(item[1].price))
        current_ent2.configure(text='{}'.format(item[2].price))
        current_ent3.configure(text='{}'.format(item[3].price))
        current_ent4.configure(text='{}'.format(item[4].price))
        earn_rate_lb2.configure(text='{0}%'.format((player.total / start_balance * 100) - 100))
        my_invest_lb1.configure(text='종목1: {0} / 보유액: {1}'.format(item[1].num, item[1].total))
        my_invest_lb2.configure(text='종목2: {0} / 보유액: {1}'.format(item[2].num, item[2].total))
        my_invest_lb3.configure(text='종목3: {0} / 보유액: {1}'.format(item[3].num, item[3].total))
        my_invest_lb4.configure(text='종목4: {0} / 보유액: {1}'.format(item[4].num, item[4].total))
        investment_lb1.configure(text='총 투자액 : {0}'.format(player.investment))
        capital_lb1.configure(text='총 자본    :{0}'.format(player.total))

    # 리포트

    canvas.create_rectangle(20, 30, 40, 80,
                            outline='black',
                            width='3',
                            fill='black')

    report_lb1 = Label(window,
                       text='재정 리포트',
                       font=report_font)
    report_lb1.place(x=700, y=220)

    earn_rate_lb1 = Label(window,
                          text='수익률: ',
                          font=trade_font)
    earn_rate_lb1.place(x=700, y=290)

    earn_rate_lb2 = Label(window,
                          text='{0}%'.format(player.total / start_balance * 100 - 100),
                          font=trade_font)
    earn_rate_lb2.place(x=790, y=290)

    my_invest_lb = Label(window,
                         text='보유 현황: ',
                         font=trade_font)
    my_invest_lb.place(x=700, y=335)

    my_invest_lb1 = Label(window,
                          text='종목1: {0} / 보유액: {1}'.format(item[1].num, item[1].total),
                          font=trade_font)
    my_invest_lb1.place(x=700, y=380)

    my_invest_lb2 = Label(window,
                          text='종목2: {0} / 보유액: {1}'.format(item[2].num, item[2].total),
                          font=trade_font)
    my_invest_lb2.place(x=700, y=420)

    my_invest_lb3 = Label(window,
                          text='종목3: {0} / 보유액: {1}'.format(item[3].num, item[3].total),
                          font=trade_font)
    my_invest_lb3.place(x=700, y=460)

    my_invest_lb4 = Label(window,
                          text='종목4: {0} / 보유액: {1}'.format(item[4].num, item[4].total),
                          font=trade_font)
    my_invest_lb4.place(x=700, y=500)

    # 투자란

    rate = 0
    rate_lb = Button

    # set1 button state

    def buy_btn_click1():
        buy_bt1.configure(bg="steelblue", fg="white")
        sell_bt1.configure(bg="lightgray", fg="black")

    def sell_btn_click1():
        sell_bt1.configure(bg="tomato", fg="white")
        buy_bt1.configure(bg="lightgray", fg="black")

    # set2 button state

    def buy_btn_click2():
        buy_bt2.configure(bg="steelblue", fg="white")
        sell_bt2.configure(bg="lightgray", fg="black")

    def sell_btn_click2():
        sell_bt2.configure(bg="tomato", fg="white")
        buy_bt2.configure(bg="lightgray", fg="black")

    # set3 button state

    def but_btn_click3():
        buy_bt3.configure(bg="steelblue", fg="white")
        sell_bt3.configure(bg="lightgray", fg="black")

    def sell_btn_click3():
        sell_bt3.configure(bg="tomato", fg="white")
        buy_bt3.configure(bg="lightgray", fg="black")

    # set4 button state

    def buy_btn_click4():
        buy_bt4.configure(bg="steelblue", fg="white")
        sell_bt4.configure(bg="lightgray", fg="black")

    def sell_btn_click4():
        sell_bt4.configure(bg="tomato", fg="white")
        buy_bt4.configure(bg="lightgray", fg="black")

    # reset button state

    def btn_reset():
        buy_bt1.configure(bg="lightgray", fg="black")
        sell_bt1.configure(bg="lightgray", fg="black")
        buy_bt2.configure(bg="lightgray", fg="black")
        sell_bt2.configure(bg="lightgray", fg="black")
        buy_bt3.configure(bg="lightgray", fg="black")
        sell_bt3.configure(bg="lightgray", fg="black")
        buy_bt4.configure(bg="lightgray", fg="black")
        sell_bt4.configure(bg="lightgray", fg="black")

    # rate state

    def ratecolor(rate_lb):
        if rate < 0:
            rate_lb.configure(color='red')
        else:
            rate_lb.configure(color='blue')

    buy_num_first = StringVar()
    buy_num_second = StringVar()
    buy_num_third = StringVar()
    buy_num_fourth = StringVar()

    # first set

    buy_lb1 = Label(window,
                    text='종목1',
                    width=10,
                    height=2,
                    justify='right',
                    font=buy_label_font)
    buy_lb1.place(x=20, y=302)

    current_ent1 = Label(window,
                         text=item[1].price,
                         justify='center',
                         font=trade_font)
    current_ent1.place(x=150,
                       y=300,
                       width=150,
                       height=65)

    num_ent1 = Entry(window,
                     justify='center',
                     textvariable=buy_num_first,
                     font=trade_font)
    num_ent1.place(x=310,
                   y=300,
                   width=80,
                   height=65)

    buy_bt1 = Button(window,
                     text='구매',
                     width=6,
                     height=2,
                     activebackground='blue',
                     activeforeground='white',
                     bg="lightgray",
                     command=lambda: [buy(1, buy_num_first.get()), buy_btn_click1()],
                     font=trade_font)
    buy_bt1.place(x=400, y=300)

    sell_bt1 = Button(window,
                      text='판매',
                      width=6,
                      height=2,
                      bg="lightgray",
                      command=lambda: [sell(1, buy_num_first.get()), sell_btn_click1()],
                      font=trade_font)
    sell_bt1.place(x=500, y=300)

    rate_lb1 = Label(window,
                     text=int(rate),
                     font=rate_font)
    rate_lb1.place(x=600, y=317)

    # second set

    buy_lb2 = Label(window,
                    text='종목2',
                    width=10,
                    height=2,
                    justify='right',
                    font=buy_label_font)
    buy_lb2.place(x=20, y=392)

    current_ent2 = Label(window,
                         text=item[2].price,
                         justify='center',
                         font=trade_font)
    current_ent2.place(x=150,
                       y=390,
                       width=150,
                       height=65)

    num_ent2 = Entry(window,
                     justify='center',
                     textvariable=buy_num_second,
                     font=trade_font)

    num_ent2.place(x=310,
                   y=390,
                   width=80,
                   height=65)

    buy_bt2 = Button(window,
                     text='구매',
                     width=6,
                     height=2,
                     activebackground='blue',
                     activeforeground='white',
                     bg="lightgray",
                     command=lambda: [buy(2, buy_num_second.get()), buy_btn_click2()],
                     font=trade_font)
    buy_bt2.place(x=400, y=390)

    sell_bt2 = Button(window,
                      text='판매',
                      width=6,
                      height=2,
                      bg="lightgray",
                      command=lambda: [sell(2, buy_num_second.get()), sell_btn_click2()],
                      font=trade_font)
    sell_bt2.place(x=500, y=390)

    rate_lb2 = Label(window,
                     text=int(rate),
                     font=rate_font)
    rate_lb2.place(x=600, y=407)

    # third set

    buy_lb3 = Label(window,
                    text='종목3',
                    width=10,
                    height=2,
                    justify='right',
                    font=buy_label_font)
    buy_lb3.place(x=20, y=482)

    current_ent3 = Label(window,
                         text=item[3].price,
                         justify='center',
                         font=trade_font)
    current_ent3.place(x=150,
                       y=480,
                       width=150,
                       height=65)

    num_ent3 = Entry(window,
                     justify='center',
                     textvariable=buy_num_third,
                     font=trade_font)
    num_ent3.place(x=310,
                   y=480,
                   width=80,
                   height=65)

    buy_bt3 = Button(window,
                     text='구매',
                     width=6,
                     height=2,
                     activebackground='blue',
                     activeforeground='white',
                     bg="lightgray",
                     command=lambda: [buy(3, buy_num_third.get()), but_btn_click3()],
                     font=trade_font)
    buy_bt3.place(x=400, y=480)

    sell_bt3 = Button(window,
                      text='판매',
                      width=6,
                      height=2,
                      bg="lightgray",
                      command=lambda: [sell(3, buy_num_third.get()), sell_btn_click3()],
                      font=trade_font)
    sell_bt3.place(x=500, y=480)

    rate_lb3 = Label(window,
                     text=int(rate),
                     font=rate_font)
    rate_lb3.place(x=600, y=497)

    # fourth set

    buy_lb4 = Label(window,
                    text='종목4',
                    width=10,
                    height=2,
                    justify='right',
                    font=buy_label_font)
    buy_lb4.place(x=20, y=572)

    current_ent4 = Label(window,
                         text=item[4].price,
                         justify='center',
                         font=trade_font)
    current_ent4.place(x=150,
                       y=570,
                       width=150,
                       height=65)

    num_ent4 = Entry(window,
                     justify='center',
                     textvariable=buy_num_fourth,
                     font=trade_font)
    num_ent4.place(x=310,
                   y=570,
                   width=80,
                   height=65)

    buy_bt4 = Button(window,
                     text='구매',
                     width=6,
                     height=2,
                     bg="lightgray",
                     command=lambda: [buy(4, buy_num_fourth.get()), buy_btn_click4()],
                     font=trade_font)
    buy_bt4.place(x=400, y=570)

    sell_bt4 = Button(window,
                      text='판매',
                      width=6,
                      height=2,
                      bg="lightgray",
                      command=lambda: [sell(4, buy_num_fourth.get()), sell_btn_click4()],
                      font=trade_font)
    sell_bt4.place(x=500, y=570)

    rate_lb4 = Label(window,
                     text=int(rate),
                     font=rate_font)
    rate_lb4.place(x=600, y=587)

    next_bt = Button(window,
                     text='다음 턴',
                     width=13,
                     height=2,
                     activebackground='black',
                     activeforeground='white',
                     command=lambda: [next_turn(), btn_reset()],
                     font=trade_font)
    next_bt.place(x=400, y=670)

    window.mainloop()
