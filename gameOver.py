from tkinter import *


def gameOver(total, investment, wallet, rate):
    game_over = Tk()
    game_over.geometry('600x600')
    game_over.title('Game over')

    logo = Label(game_over, text='Game over', font=('', 30))
    total_result = Label(game_over, text='최종 금액: {}'.format(total))
    investment_result = Label(game_over, text='최종 투자 금액: {}'.format(investment))
    wallet_result = Label(game_over, text='지갑 잔여 금액: {}'.format(wallet))
    rate_result = Label(game_over, text='최종 수익율: {}'.format(rate))

    exit_btn = Button(game_over, text='종료하기', font=('', 20), width='10', height='2', command=exit)

    logo.place(x=200, y=180)
    total_result.place(x=200, y=300)
    investment_result.place(x=200, y=320)
    wallet_result.place(x=200, y=340)
    rate_result.place(x=200, y=360)
    exit_btn.place(x=200, y=400)
    game_over.mainloop()
