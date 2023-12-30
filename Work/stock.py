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