import csv


def read_prices():

    stock_prices = {}

    f = open("Data/prices.csv", "r")
    rows = csv.reader(f)
    for row in rows:
        try:
            stock_prices[row[0]] = row[1]
        except IndexError:
            pass
    f.close()
    
    return stock_prices
    
dict = read_prices()

print(dict)
print(type(dict))
print(dict["AA"])