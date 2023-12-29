import csv
from pprint import pprint

f = open("Data/portfoliodate.csv")
rows = csv.reader(f)
headers = next(rows)


select = ["name", "shares", "price"]

indices = [headers.index(colname) for colname in select]
#print(indices)

row = next(rows)
portfolio = [{colname:row[index] for colname, index in zip(select, 
  indices)} for row in rows]
pprint(portfolio)

f.close()