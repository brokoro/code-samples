# An inventory class that stores a catalogue of products and their number in 
# stock
# Multiple constructors for passing in only the catalogue, or the catalogue with
# the stock
# Use *args to create tuple of anonymous arguments, **kwargs for dictionary of 
# named arguments
def args(*args, **kwargs):
    print 'args: ', args, ' kwargs: ', kwargs

class Inventory:
    def __init__(self, **data)
        self.stock = data['stock']
        self.inventory = (data['inventory'] if data['inventory'] 
                else {self.stock : 0} }

# Alternatively use @classmethod

class Inventory2:
    def __init__(self, stock):
        self.stock = data
        self.catalogue = stock.keys()

    @classmethod
    def catalogue(inv, data):
        stock = dict((item, 0) for item in data)
        return inv(stock, data)
