class Commodities:
    def __init__(self, price):
        self.price = price
        self.num = 0
        self.total = self.num * self.price

    def update_price(self, price):
        self.price = int(self.price + (self.price * price) / 100)
        self.total = self.price * self.num

    def update_num(self, num):
        self.num = self.num + num
        self.total = self.price * self.num

