# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        cost = 0
        for row in rows:
            try:
                cost += int(row[1])*float(row[2])
                print(row)
            except ValueError:
                print('Bad row:', row)
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
