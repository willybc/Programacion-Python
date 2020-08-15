f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',')
headers

for line in f:
    row = line.split(',')
    print(row)


f.close()