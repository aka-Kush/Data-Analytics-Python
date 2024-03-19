# pandas is a data manipulation tool built over Numpy
# works with datafram i.e. tabular data
import pandas as pd

# this dataframe can be created yourseld using list (keys = col labels, values = data) but it is very complicated
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'country' : names, 'drives_right': dr, 'cars_per_cap': cpc}
# building dataframe from dictionary
cars = pd.DataFrame(my_dict)
print(cars)

# chanding row index
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels

# we usually import "comma seperated values" file .csv
brics = pd.read_csv("/home/kush/Desktop/DataAnalytics/python/data.csv") # give path to csv file to read
# print(brics)

# here row labels are seen as a seperate column
# we can fix this by telling read_csv that first col contains row indexes
brics = pd.read_csv("/home/kush/Desktop/DataAnalytics/python/data.csv", index_col= 0)
print(brics)

# selecting data
print(brics["country"])
print(type(brics["country"])) # it is a series data type which is 1D labelled array
# in order to get data in dataframe, we can do
print(brics[["country"]])
print(type(brics[["country"]])) # dataframe

# multiple cols
print(brics[["country", "capital"]])
# multiple rows
print(brics[1:4])

# Loc and iloc are two functions in Pandas that are used to slice a data set in a Pandas DataFrame
# loc is typically used for label indexing and can access multiple columns
# iloc is used for integer indexing
print(brics.loc[["IN"]]) # gives us info about label IN
print(brics.loc[["IN", "RU", "CH"]])

# we can also define which col to return
print(brics.loc[["IN", "RU", "CH"], ["country", "capital"]])
# all rows but specific columns
print(brics.loc[:, ["country", "capital"]])

print(brics.iloc[[1]])
print(brics.iloc[[1, 2, 3], [0,3]])
print(brics.iloc[:, [0,3]])