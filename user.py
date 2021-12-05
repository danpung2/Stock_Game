class User:
    def __init__(self, investment, wallet, date):
        self.total = investment + wallet
        self.investment = investment
        self.wallet = wallet
        self.date = date
        self.time = 0

    def update(self, investment):
        self.investment = self.investment + investment
        self.wallet = self.wallet - investment
        self.total = self.investment + self.wallet

    def update_date(self):
        self.date -= 1

    def update_time(self):
        if self.time == 2:
            self.time = 0
        else:
            self.time += 1

    def update_rate(self, investment):
        self.investment = investment
        self.total = self.investment + self.wallet
