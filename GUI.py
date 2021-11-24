from tkinter import*
import tkinter.font as tkFont
from functools import partial

window=Tk()
window.geometry('1200x800')
window.title('투자 게임')

canvas=Canvas(window)

datefont=tkFont.Font(size=15)
tradefont=tkFont.Font(size=18)
buyLBfont=tkFont.Font(size=20)
titlefont=tkFont.Font(size=60, weight='bold')
capitalfont=tkFont.Font(size=20)
ratefont=tkFont.Font(size=15)
reportfont=tkFont.Font(size=30)

#날짜

date_lb=Label(window,
             text='N일차',
             font=datefont)
date_lb.place(x=50, y=50)

date_lb=Label(window,
             text='아침/점심/저녁',
             font=datefont)
date_lb.place(x=50, y=80)

# 게임 이름

title=Label(window,
             text='게임 이름',
             font=titlefont)
title.place(x=50, y=150)

#총 자본, 지갑, 투자액

capital_lb1=Label(window,
             text='총 자본    : ',
             font=capitalfont)
capital_lb1.place(x=700, y=50)

capital_lb2=Label(window,
             text='자본',
             font=capitalfont)
capital_lb2.place(x=850, y=50)


wallet_lb1=Label(window,
             text='지갑        : ',
             font=capitalfont)
wallet_lb1.place(x=700, y=85)

wallet_lb2=Label(window,
             text='지갑',
             font=capitalfont)
wallet_lb2.place(x=850, y=85)


investment_lb1=Label(window,
             text='총 투자액 : ',
             font=capitalfont)
investment_lb1.place(x=700, y=120)

investment_lb2=Label(window,
             text='투자액',
             font=capitalfont)
investment_lb2.place(x=850, y=120)


#리포트

canvas.create_rectangle(20, 30, 40, 80,
                        outline='black',
                        width='3',
                        fill='black')

report_lb1=Label(window,
                 text='재정 리포트',
                 font=reportfont)
report_lb1.place(x=700, y=220)

earnrate_lb1=Label(window,
                 text='수익률: ',
                 font= tradefont)
earnrate_lb1.place(x=700, y=290)

earnrate_lb2=Label(window,
                 text='수익률',
                 font= tradefont)
earnrate_lb2.place(x=790, y=290)

myinvest_lb=Label(window,
                 text='현재 보유 종목: ',
                 font= tradefont)
myinvest_lb.place(x=700, y=335)

myinvest_lb1=Label(window,
                 text='-종목1',
                 font= tradefont)
myinvest_lb1.place(x=700, y=380)

myinvest_lb2=Label(window,
                 text='-종목2',
                 font= tradefont)
myinvest_lb2.place(x=700, y=420)

myinvest_lb3=Label(window,
                 text='-종목3',
                 font= tradefont)
myinvest_lb3.place(x=700, y=460)


#투자란

rate=0
rate_lb=Button

def buybtclick(self):
    if self['state']=='normal':
        self['state']=='active'
        
def ratecolor(rate_lb):
    if rate<0:
        rate_lb.configure(color='red')
    else:
        rate_lb.configure(color='blue')


# first set

buy_lb1=Label(window,
             text='종목1',
             width=10,
             height=2,
             justify='right',
             font=buyLBfont)
buy_lb1.place(x=20, y=302)

current_ent1=Entry(window,
              justify='center',
              font=tradefont)
current_ent1.place(x=150,
              y=300,
              width=150,
              height=65)

num_ent1=Entry(window,
              justify='center',
              font=tradefont)
num_ent1.place(x=310,
              y=300,
              width=80,
              height=65)

buy_bt1=Button(window,
               text='구매',
               width=6,
               height=2,
               activebackground='blue',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
buy_bt1.place(x=400, y=300)

sell_bt1=Button(window,
               text='판매',
               width=6,
               height=2,
               activebackground='red',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
sell_bt1.place(x=500, y=300)

rate_lb1=Label(window,
               text=int(rate),
               font=ratefont)
rate_lb1.place(x=600, y=317)

# second set

buy_lb2=Label(window,
             text='종목2',
             width=10,
             height=2,
             justify='right',
             font=buyLBfont)
buy_lb2.place(x=20, y=392)

current_ent2=Entry(window,
              justify='center',
              font=tradefont)
current_ent2.place(x=150,
              y=390,
              width=150,
              height=65)

num_ent2=Entry(window,
              justify='center',
              font=tradefont)
num_ent2.place(x=310,
              y=390,
              width=80,
              height=65)

buy_bt2=Button(window,
               text='구매',
               width=6,
               height=2,
               activebackground='blue',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
buy_bt2.place(x=400, y=390)

sell_bt2=Button(window,
               text='판매',
               width=6,
               height=2,
               activebackground='red',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
sell_bt2.place(x=500, y=390)

rate_lb2=Label(window,
               text=int(rate),
               font=ratefont)
rate_lb2.place(x=600, y=407)

# third set

buy_lb3=Label(window,
             text='종목3',
             width=10,
             height=2,
             justify='right',
             font=buyLBfont)
buy_lb3.place(x=20, y=482)

current_ent3=Entry(window,
              justify='center',
              font=tradefont)
current_ent3.place(x=150,
              y=480,
              width=150,
              height=65)

num_ent3=Entry(window,
              justify='center',
              font=tradefont)
num_ent3.place(x=310,
              y=480,
              width=80,
              height=65)

buy_bt3=Button(window,
               text='구매',
               width=6,
               height=2,
               activebackground='blue',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
buy_bt3.place(x=400, y=480)

sell_bt3=Button(window,
               text='판매',
               width=6,
               height=2,
               activebackground='red',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
sell_bt3.place(x=500, y=480)

rate_lb3=Label(window,
               text=int(rate),
               font=ratefont)
rate_lb3.place(x=600, y=497)

# fourth set

buy_lb4=Label(window,
             text='종목4',
             width=10,
             height=2,
             justify='right',
             font=buyLBfont)
buy_lb4.place(x=20, y=572)

current_ent4=Entry(window,
              justify='center',
              font=tradefont)
current_ent4.place(x=150,
              y=570,
              width=150,
              height=65)

num_ent4=Entry(window,
              justify='center',
              font=tradefont)
num_ent4.place(x=310,
              y=570,
              width=80,
              height=65)

buy_bt4=Button(window,
               text='구매',
               width=6,
               height=2,
               activebackground='blue',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
buy_bt4.place(x=400, y=570)

sell_bt4=Button(window,
               text='판매',
               width=6,
               height=2,
               activebackground='red',
               activeforeground='white',
               command=buybtclick,
               font=tradefont)
sell_bt4.place(x=500, y=570)

rate_lb4=Label(window,
               text=int(rate),
               font=ratefont)
rate_lb4.place(x=600, y=587)



next_bt=Button(window,
               text='다음 턴',
               width=13,
               height=2,
               activebackground='black',
               activeforeground='white',
               #command=
               font=tradefont)
next_bt.place(x=400, y=670)



window.mainloop()
