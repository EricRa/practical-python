from pprint import pprint

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        """
        Computes the total value of all shares at the current price
        """
        total = self.shares * self.price
        return total
        
    def sell(self, shares_to_sell):
        """
        Adjusts the total number of shares based on the specified amount sold
        """
        self.shares = self.shares - shares_to_sell
        
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
        
    #def cost(self): #returns an incorrect value for cost
        #return 1.25 * self.shares * self.price
    
    def cost(self):
        # Check the call to "super"
        actual_cost = super().cost()
        return 1.25 * actual_cost
    
s = MyStock("GOOG", 100, 490.1)

pprint(s.cost())

s.sell(25)
pprint(f"Shares sold.  Current shares: {s.shares}")

s.panic()
pprint(f"PANIC!  All shares sold.  Current shares: {s.shares}")
    