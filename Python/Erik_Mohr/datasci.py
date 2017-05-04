import numpy as np 
import pandas as pd

# Create 2 new lists for height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Add the height, weight of your family members to this list, using extend()

# Oops, you forgot one! Add my height, weight using append()

# Convert height and weight lists to numpy arrays
np_height = np.array(height)
np_weight = np.array(weight)

# Assign two new lists these heights and weights, converted to imperial

height_US = np_height * 3.28
weight_US = np_weight * 2.205

# Print out type of numpy array
print "Numpy arrays are of type %s." % (type(np_height))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Create a string of bmi values using join(), list comprehension
bmi_str = ', '.join(str(val) for val in bmi)

print "The bmi values are " + bmi_str



# Print the result
print(bmi)

# Subsetting

# Write out boolean response
bmi > 23

# Print only those observations above 23
high_bmi = bmi[bmi > 23]

# Alternative way of returning bmi string
high_bmi_str = ', '.join(map(str, high_bmi))

print "The bmi values over 23 are " + high_bmi_str
# Create dictionary for information on BRICS

brics_dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics_table = pd.DataFrame(brics_dict)
print brics_table

# Set the index for brics
brics_table.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print brics_table

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# The DataFrame's column has the following column indices
# Model, MPG, Cylinder, Engine Disp, Horsepower, Weight, Accelerate, Year, Origin

# Print out cars
print cars 

# Read cars with the 1st column as the index
cars = pd.read_csv('cars.csv', index_col = 0)

# Use square brackets to index DataFrame

# Print out country column as Pandas Series
print(cars['MPG'])

# Print out country column as Pandas DataFrame
print(cars[['MPG']])

# Print out DataFrame with country and drives_right columns
print(cars[['MPG', 'Horsepower']])

# Also use square brackets to slice DataFrame

#for i in range(8, 392, 8):
#	print(cars[i-8:i])


# Use loc to locate based on label, iloc to locate based on integer

# Print out observations for two different models
print(cars.loc[['bmw 320i', 'audi 5000']])