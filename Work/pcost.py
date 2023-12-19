# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):

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
        try:
            subtotal = float(rowdata[1]) * float(rowdata[2])
            total = total + subtotal
        except ValueError:
            print("Could not parse", rowdata)
        
    return total
        
    # print(f"The total is: ${total}")
    
cost = portfolio_cost("/Data/portfolio.csv")
print("Total cost: ", cost)