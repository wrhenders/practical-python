# report.py
#
# Exercise 2.4

import fileparse
from stock import Stock
import tableformat


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as f:
        file_dictionary = fileparse.parse_csv(
            f, select=['name', 'shares', 'price'], types=[str, int, float])
    return [Stock(d['name'], d['shares'], d['price']) for d in file_dictionary]


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as f:
        return dict(fileparse.parse_csv(f, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    """Computes the PnL of a portfolio from prices"""
    table = []
    for s in portfolio:
        change = prices[s.name]-s.price
        table.append((s.name, s.shares, prices[s.name], change))
    return table


def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
