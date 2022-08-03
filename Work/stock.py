class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    def cost(self):
        return self.shares * self.price

    def sell(self, num):
        self.shares -= num
        if self.shares < 0:
            self.shares = 0
