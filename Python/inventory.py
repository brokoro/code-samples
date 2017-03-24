from collections import defaultdict

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
    def __init__(self, stock = defaultdict(int)):
        self.stock = stock
        self.catalogue = stock.keys()

    @classmethod
    # Initialize inventory w list of available merchandise
    # Quantity in stock initialized to 0
    def catalogue(inv, data):
        stock = dict((item, 0) for item in data)
        return inv(stock)

    # Increase the supply of an item
    def incr(self, item, supply = 0):
        self.stock[item] += supply

    # Decrease the supply of an item
    def decr(self, item, supply = None):
        if not supply:
            del self.stock[item]
        else:
            self.stock[item] -= supply
        if self.stock[item] < 0:
            print "You are short %d %ss" % (self.stock[item], item)

    # Put new items on the catalogue
    def enlist(self, *items):
        for item in items:
            self.stock[item] = 0

    # Remove old items from the catalogue
    def delist(self, item):
        del self.stock[item]

    # Write out each item and their amount in stock
    def audit(self):
        print self.stock

# Start with some initial catalogue

clothing_data = ["tshirts", "hats", "hoodies"]

# Initialize inventory from catalogue
clothing_inv = Inventory2.catalogue(clothing_data)

# Put new clothing items on catalogue
clothing_inv.enlist("sweats", "long sleeve")

# Display inventory
clothing_inv.audit()


