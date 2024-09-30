import pandas as pd #aliases 
import numpy as np 

#**pandas' series object (one Dimention arrays of indexe data)

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data.values) # looks like a list 
print(data.index) #range computed for indicies 
print("getting one value")
print(data[1])
print("getting 2 values from thing. 3 is uninclusive")
print(data[0:3])
#            ^stop index. stops at this point 

#series are like arrays but with explicit indexting (dont let your parents hear it)
grades = pd.Series([9, 10, 11, 12], index=['freshmen', 'sophomore', 'junior', 'senior'])
print(data)
print("Seniors are in grade ", grades['senior'])

# can also create a series from a dictorany 
cockiesDict = { 'double chocolate': 5, 'chocolate chip': 8.5, 'oatmeal raisin': 9, 'snickerdoodle': 10,  'dirt': 1 }
cookies = pd.Series(cookiesDict)
print(cookies)
print("rating of dirt cookies: ", cookies['dirt'])