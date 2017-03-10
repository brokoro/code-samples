# An inventory class that stores a catalogue of products and their number in 
# stock
# Multiple constructors for passing in only the catalogue, or the catalogue with
# the stock
# Use *args to create tuple of anonymous arguments, **kwargs for dictionary of 
# named arguments
def args(*args, **kwargs):
    print 'args: ', args, ' kwargs: ', kwargs

# For example, initialized optionally by map from items to quantity in stock
# or simply by list of available merchandise
class Inventory:
    def __init__(self, **data):
        self.stock = data['stock']
        self.catalogue = data['catalogue'] if 'catalogue' in data else data['stock'].keys() 

# Alternatively use @classmethod
class Inventory2:
    # Initialize with dictionary mapping items to quantity in stock
    def __init__(self, stock = {}):
        self.stock = data
        self.catalogue = stock.keys()

    @classmethod
    # Initialize inventory w list of available merchandise
    # Quantity in stock initialized to 0
    def catalogue(inv, data):
        stock = dict((item, 0) for item in data)
        return inv(stock, data)

    def add_item(self, item, supply=0):
        stock[item] += supply

    def sub_item(self, item, supply=0):
        if supply == 0:
            del stock[item]
        elif supply < stock[item]:
            stock[item] -= supply
        else:
            stock[item] = 0 
