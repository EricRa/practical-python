# report.py
#
# Exercise 2.4

# 
# 
# import csv
# 
# def read_portfolio(filename):
#     """ Opens a portfolio file and reads it into a list of tuples"""
#     
#     portfolio = []
#     
#     with open(filename, "rt") as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = row[0], int(row[1]), float(row[2])
#             portfolio.append(holding)
#     
#     return portfolio
#     

    
# Exercise 2.5

import csv
from pprint import pprint

def read_portfolio(filename):
    """ Opens a portfolio file and reads it into a list of tuples"""
    
    portfolio = []
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            entry = {"name": row[0], "shares": int(row[1]), 
                "price": float(row[2])}
            portfolio.append(entry)
    
    return portfolio

data = read_portfolio("Data/portfolio.csv")
pprint(data)
