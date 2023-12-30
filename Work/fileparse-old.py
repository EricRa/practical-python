# fileparse.py
#
# Exercise 3.3


import csv
from pprint import pprint

def parse_csv(filename, select=""):
    """
    Parse a CSV file into a list of records
    """
    
    with open(filename) as f:
        rows = csv.reader(f)
        
        # Read the file headers
        headers = next(rows)
        #print(type(headers))
        
        # If a column selector was given, find indices of the specified columns
        # Also narrows the set of headers used for resulting dicts.
        
        if select:
            #print(select)
            try:
                indices = [headers.index(colname) for colname in select]
                headers = select
            except Exception as e:
                pprint(f"There was an error:  {e}")
                indices = []
 
        else:
            indices = []
            
        records = []
        for row in rows:
            if not row: #skip rows with no data
                continue
                
            if indices:
                try:
                    row = [row[index] for index in indices]
                except ValueError as e:
                    pprint(f"There was an error:  {e}")
            
            record = dict(zip(headers, row))
            records.append(record)
            
    return records

portfolio = parse_csv("Data/portfolio.csv", select=["name"])
pprint(portfolio)
