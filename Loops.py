# Basic while loop
# -------------------------------------------

# Initialize offset
offset = 8
# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# -------------------------------------------
# Add conditionals
# -------------------------------------------

# Initialize offset
offset = -6
# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset = offset -1
    else :
        offset = offset + 1
    print(offset)

# -------------------------------------------
# Loop over a list
# -------------------------------------------

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for area in areas:
    print(area)

# -------------------------------------------
# Indexes and values (1)
# -------------------------------------------

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Change for loop to use enumerate()
for index,a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))

# -------------------------------------------
# Indexes and values (2)
# -------------------------------------------

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for index, area in enumerate(areas) :
    roomnumber = index + 1
    print("room " + str(roomnumber) + ": " + str(area))

# -------------------------------------------
# Loop over list of lists
# -------------------------------------------

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
# Build a for loop from scratch
for room, area in house:
    print("the " + room + " is " + str(area) + " sqm")

# -------------------------------------------
# Loop over dictionary
# -------------------------------------------

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)

# -------------------------------------------
# Loop over Numpy array
# -------------------------------------------

# Import numpy as np
import numpy as np
# For loop over np_height
for val in np_height:
    print(str(val) + " inches" )
# For loop over np_baseball
for val2 in np.nditer(np_baseball):
    print(val2)

# -------------------------------------------
# Loop over DataFrame (1)
# -------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Iterate over rows of cars
for lab,row in cars.iterrows():
    print(lab)
    print(row)

# -------------------------------------------
# Loop over DataFrame (2)
# -------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

# -------------------------------------------
# Add column (1)
# -------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab,"COUNTRY"] = row['country'].upper()
# Print cars
print(cars)

# -------------------------------------------
# Add column (2)
# -------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)
