import random
import pandas as pd

# Ball machine "generating" the random numbers 
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
    	yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

# The announcer calls out each number
# for random_number in lottery():
# 	print("And the next number is... %d!" %(random_number))

def fib():
	a = 1
	b = 1
	while True:
		yield a
		a, b = b, a + b

def scroll(df):

	num_ln = input("How many lines should we read at a time?: ")
	
	for i in range(num_ln, df.shape[0], num_ln):
		yield cars[i-num_ln:i]

cars = pd.read_csv('cars.csv', index_col = 0)

for page in scroll(cars):
	response = raw_input("Read next section?: ")
	if response == "y" or response == "yes":
		print page
