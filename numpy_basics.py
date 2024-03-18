# Package installation : we use pip to install python packages
# pip3 install numpy 

# import complete package
# import numpy as np
# np.array([1,2,3])

# import specific function from package
# from numpy import array
# array([1,2,3])

# calculating bmi using array in numpy as we can't perform ** or pow() on lists in numpy
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
np_bmi = np_weight / np_height ** 2
print(np_bmi)

# Numpy arrays only contain one type
# if we add multiple type data then it will converted to one
random = np.array([1, "one", True]) 
print(random) # all values converted to string

# If we use + operator with list, it will return concatenated list
# But with numpy array, it will return sum of both arrays
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2)
print(np.array(list1) + np.array(list2))

np.array([True, 1, 2]) + np.array([3, 4, False])

# numpy subsetting
ll = np.array([21,20,15,87,52,9])
print(ll[1])
print(ll > 50) # it returns boolean array, of values above and below 50
print(ll[ll > 50]) # this will return values that are greater than 50

# 2D numpy arrays
twoDarray = np.array([[1,2,3], [4,5,6]])
print(twoDarray)
print(type(twoDarray))
print(twoDarray.shape) # shape is attribute of ndarray array which gives us more info about array

# if we change one value of 2D array to string all the other values will also be changed to string
homegenous = np.array([[1,2,3], [4,"five",6]])
print(homegenous)

# subsetting in 2D array
print(twoDarray[0][1]) # array[row][col]
print(twoDarray[0, 1]) # same as above
print(twoDarray[:, 0:1])
print(twoDarray[1, :])