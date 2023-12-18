# pcost.py
#
# Exercise 1.27

data = []

f = open("Data/portfolio.csv", "rt")
headers = next(f).split(",")

for line in f:
    row = line.split(",")
    data.append(row)

f.close()

#print(data)

total = 0

for rowdata in data:
    subtotal = float(rowdata[1]) * float(rowdata[2])
    total = total + subtotal
    
print(f"The total is: ${total}")