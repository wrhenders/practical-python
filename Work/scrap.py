# import csv
# f = open('Data/portfolio.csv')
# rows = csv.reader(f)
# next(rows)
# row = next(rows)

# t = (row[0], int(row[1]), float(row[2]))

# d = {
#     'name': row[0],
#     'shares': int(row[1]),
#     'price': float(row[2])
# }


def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line


for line in filematch('Data/portfolio.csv', 'IBM'):
    print(line, end='')
