from tkinter import*
import tkinter.font as tkFont
from functools import partial
import random

def gameStart(start_date, balance):
    window = Tk()
    window.geometry('1200x800')
    window.title('투자 게임')

    window.balance = 0
    window.total_purchase_cost = 0
    window.total_current_cost = 0  
    window.total = 0

    var1 = StringVar()    
    var2 = StringVar()
    var3 = StringVar()

    if(window.total_purchase_cost == 0):
        window.balance = balance
        window.total_purchase_cost = 0
        window.total_current_cost = 0  
        window.total = balance
        var1.set(window.total)
        var2.set(window.balance)
        var3.set(window.total_purchase_cost)

    window.item = {1 : 100000, 2 : 200000, 3 : 300000, 4 : 400000}
    window.investment = {1 : 0, 2 : 0, 3 : 0, 4 : 0}

    canvas = Canvas(window)

    datefont = tkFont.Font(size=15)
    tradefont = tkFont.Font(size=18)
    buyLBfont = tkFont.Font(size=20)
    titlefont = tkFont.Font(size=60, weight='bold')
    capitalfont = tkFont.Font(size=20)
    ratefont = tkFont.Font(size=15)
    reportfont = tkFont.Font(size=30)

    #날짜

    date_lb = Label(window,
                    text='N일차/{0}일'.format(start_date),
                    font=datefont)
    date_lb.place(x=50, y=50)

    date_lb = Label(window,
                    text='아침/점심/저녁',
                    font=datefont)
    date_lb.place(x=50, y=80)

    # 게임 이름

    title = Label(window,
                    text='Stock Game',
                    font=titlefont)
    title.place(x=50, y=150)

    #총 자본, 지갑, 투자액

    capital_lb1 = Label(window,
                        text = '총 자본    : ' + var1.get(),
                        font=capitalfont)
    capital_lb1.place(x=700, y=50)

    # capital_lb2 = Label(window,
    #                     text='자본',
    #                     font=capitalfont)
    # capital_lb2.place(x=850, y=50)


    wallet_lb1 = Label(window,
                        text = '지갑         : ' + var2.get(),
                        font=capitalfont)
    wallet_lb1.place(x=700, y=85)

    # wallet_lb2 = Label(window,
    #                     text='지갑',
    #                     font=capitalfont)
    # wallet_lb2.place(x=850, y=85)


    investment_lb1 = Label(window,
                        text = '총 투자액 : '+ var3.get(),
                        font=capitalfont)
    investment_lb1.place(x=700, y=120)

    # investment_lb2 = Label(window,
    #                         text='투자액',
    #                 font=capitalfont)
    # investment_lb2.place(x=850, y=120)

    def buy(item_num, buy_num, balance, total):
        buy_num_int = int(buy_num.get())
        if(balance < (buy_num_int) * window.item[item_num]):
            return
        else:
            total = 0
            window.investment[item_num] += buy_num_int * window.item[item_num]
            window.total_purchase_cost += buy_num_int * window.item[item_num]
            balance -= buy_num_int * window.item[item_num]
            for i in range(1, 5):
                total += window.investment[i]
            total += balance
            window.balance = balance
            capital_lb1.configure(text = '총 자본    : {0}'.format(total))
            wallet_lb1.configure(text = '지갑         : {0}'.format(window.balance))
            investment_lb1.configure(text = '총 투자액 : {0}'.format(window.total_purchase_cost))
        num_ent1.delete(0, END)
        num_ent2.delete(0, END)
        num_ent3.delete(0, END)
        num_ent4.delete(0, END)
        return window.balance

    def rate_of_fluctuation(investment, balance, total, total_current_cost):
        for i in range(1, 5):
            fluctuation = random.randint(1, 10)
            if(fluctuation <= 5):
                investment[i] *= (fluctuation * 10)/100 + 1
                window.item[i] *= (fluctuation * 10)/100 + 1
            else:
                investment[i] *= 1 - ((10-fluctuation) * 10)/100
                window.item[i] *= 1 - ((10-fluctuation) * 10)/100
        for i in range(1, 5):
            total += investment[i]
            total_current_cost += investment[i]
        total += balance
        return total, total_current_cost

    #리포트

    canvas.create_rectangle(20, 30, 40, 80,
                            outline='black',
                            width='3',
                            fill='black')

    report_lb1 = Label(window,
                    text='재정 리포트',
                    font=reportfont)
    report_lb1.place(x=700, y=220)

    earnrate_lb1 = Label(window,
                        text='수익률: ',
                        font=tradefont)
    earnrate_lb1.place(x=700, y=290)

    earnrate_lb2 = Label(window,
                        text='수익률',
                        font=tradefont)
    earnrate_lb2.place(x=790, y=290)

    myinvest_lb = Label(window,
                        text='보유 현황: ',
                        font=tradefont)
    myinvest_lb.place(x=700, y=335)

    myinvest_lb1 = Label(window,
                        text='종목1: {0}'.format(window.investment[1]),
                        font=tradefont)
    myinvest_lb1.place(x=700, y=380)

    myinvest_lb2 = Label(window,
                        text='종목2: {0}'.format(window.investment[2]),
                        font=tradefont)
    myinvest_lb2.place(x=700, y=420)

    myinvest_lb3 = Label(window,
                        text='종목3: {0}'.format(window.investment[3]),
                        font=tradefont)
    myinvest_lb3.place(x=700, y=460)

    myinvest_lb4 = Label(window,
                        text='종목4: {0}'.format(window.investment[4]),
                        font=tradefont)
    myinvest_lb4.place(x=700, y=500)


    #투자란

    rate = 0
    rate_lb = Button


    def buybtclick(self):
        if self['state'] == 'normal':
            self['state'] == 'active'


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
                    font=buyLBfont)
    buy_lb1.place(x=20, y=302)

    current_ent1 = Label(window,
                        text=window.item[1],
                        justify='center',
                        font=tradefont)
    current_ent1.place(x=150,
                    y=300,
                    width=150,
                    height=65)

    num_ent1 = Entry(window,
                    justify='center',
                    textvariable=buy_num_first,
                    font=tradefont)
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
                    command=partial(buy, 1, buy_num_first, window.balance, window.total),
                    font=tradefont)
    buy_bt1.place(x=400, y=300)

    sell_bt1 = Button(window,
                    text='판매',
                    width=6,
                    height=2,
                    activebackground='red',
                    activeforeground='white',
                    command=buybtclick,
                    font=tradefont)
    sell_bt1.place(x=500, y=300)

    rate_lb1 = Label(window,
                    text=int(rate),
                    font=ratefont)
    rate_lb1.place(x=600, y=317)

    # second set

    buy_lb2 = Label(window,
                    text='종목2',
                    width=10,
                    height=2,
                    justify='right',
                    font=buyLBfont)
    buy_lb2.place(x=20, y=392)

    current_ent2 = Label(window,
                        text=window.item[2],
                        justify='center',
                        font=tradefont)
    current_ent2.place(x=150,
                    y=390,
                    width=150,
                    height=65)

    num_ent2 = Entry(window,
                    justify='center',
                    textvariable=buy_num_second,
                    font=tradefont)
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
                    command=partial(buy, 2, buy_num_second, window.balance, window.total),
                    font=tradefont)
    buy_bt2.place(x=400, y=390)

    sell_bt2 = Button(window,
                    text='판매',
                    width=6,
                    height=2,
                    activebackground='red',
                    activeforeground='white',
                    command=buybtclick,
                    font=tradefont)
    sell_bt2.place(x=500, y=390)

    rate_lb2 = Label(window,
                    text=int(rate),
                    font=ratefont)
    rate_lb2.place(x=600, y=407)

    # third set

    buy_lb3 = Label(window,
                    text='종목3',
                    width=10,
                    height=2,
                    justify='right',
                    font=buyLBfont)
    buy_lb3.place(x=20, y=482)

    current_ent3 = Label(window,
                        text=window.item[3],
                        justify='center',
                        font=tradefont)
    current_ent3.place(x=150,
                    y=480,
                    width=150,
                    height=65)

    num_ent3 = Entry(window,
                    justify='center',
                    textvariable=buy_num_third,
                    font=tradefont)
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
                    command=partial(buy, 3, buy_num_third, window.balance, window.total),
                    font=tradefont)
    buy_bt3.place(x=400, y=480)

    sell_bt3 = Button(window,
                    text='판매',
                    width=6,
                    height=2,
                    activebackground='red',
                    activeforeground='white',
                    command=buybtclick,
                    font=tradefont)
    sell_bt3.place(x=500, y=480)

    rate_lb3 = Label(window,
                    text=int(rate),
                    font=ratefont)
    rate_lb3.place(x=600, y=497)

    # fourth set

    buy_lb4 = Label(window,
                    text='종목4',
                    width=10,
                    height=2,
                    justify='right',
                    font=buyLBfont)
    buy_lb4.place(x=20, y=572)

    current_ent4 = Label(window,
                        text=window.item[4],
                        justify='center',
                        font=tradefont)
    current_ent4.place(x=150,
                    y=570,
                    width=150,
                    height=65)

    num_ent4 = Entry(window,
                    justify='center',
                    textvariable=buy_num_fourth,
                    font=tradefont)
    num_ent4.place(x=310,
                y=570,
                width=80,
                height=65)

    buy_bt4 = Button(window,
                    text='구매',
                    width=6,
                    height=2,
                    activebackground='blue',
                    activeforeground='white',
                    command=partial(buy, 4, buy_num_fourth, window.balance, window.total),
                    font=tradefont)
    buy_bt4.place(x=400, y=570)

    sell_bt4 = Button(window,
                    text='판매',
                    width=6,
                    height=2,
                    activebackground='red',
                    activeforeground='white',
                    command=buybtclick,
                    font=tradefont)
    sell_bt4.place(x=500, y=570)

    rate_lb4 = Label(window,
                    text=int(rate),
                    font=ratefont)
    rate_lb4.place(x=600, y=587)


    next_bt = Button(window,
                    text='다음 턴',
                    width=13,
                    height=2,
                    activebackground='black',
                    activeforeground='white',
                    #command=
                    font=tradefont)
    next_bt.place(x=400, y=670)


    window.mainloop()
