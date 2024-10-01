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
cookiesDict = { 'double chocolate': 5, 'chocolate chip': 8.5, 'oatmeal raisin': 9, 'snickerdoodle': 10,  'dirt': 1 }
cookies = pd.Series(cookiesDict)
print(cookies)
print("rating of dirt cookies: ", cookies['dirt'])

#Dataframes is like a 2d array or specialized dictionary 
cookiesDF = pd.DataFrame(cookies, columns=['rating'])
print(cookiesDF)

#add a column to our dataframe 
cookiesDF['allergens'] = [True, True, True, True, False]
print(cookiesDF)

cookiesDF['Sweetness'] = { 'double chocolate': 10, 'chocolate chip': 9, 'oatmeal raisin': 7, 'snickerdoodle': 10,  'dirt': 1, 'birthday cake':1000}
print(cookiesDF)

data = pd.Series(['a','c','e'], index=[1,3,5])

#indexing 
print(data[3])

#slcing
print(data[3:5]) #not getting expected 

#instead use LOC to get a slice that uses explictit indecies 
#inclusive at index 5
print(data.loc[3:5])

#not as common, iLOC uses implicit indeices
print(data.iloc[0:1]) #doesnt include second