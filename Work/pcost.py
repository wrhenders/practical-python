# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    cost = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                cost += nshares * price
            except ValueError:
                print(f"Row:{i} Couldn't convert:", row)
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
