import csv
from pprint import pprint

f = open("Data/dowstocks.csv")
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
headers
rows

types = [str,float,str,str,float,float,float,float,int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
print(record)
pprint(record["name"])
pprint(record["price"])

f.close()