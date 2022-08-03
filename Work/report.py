# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    """Converts a portfolio from csv file to dictionary"""
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:

                holding = {'name': record['name'], 'shares': int(
                    record['shares']), 'price': float(record['price'])}
                portfolio.append(holding)
            except ValueError:
                print(f"Row:{i} Couldn't convert:", row)

    return portfolio


def read_prices(filename):
    """Reads prices into a dictionary"""
    portfolio = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                portfolio[row[0]] = float(row[1])

    return portfolio


def make_report(portfolio, prices):
    """Computes the PnL of a portfolio from prices"""
    table = []
    for s in portfolio:
        change = prices[s['name']]-s['price']
        table.append((s['name'], s['shares'], s['price'], change))
    return table


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)


headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
