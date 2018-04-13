import numpy as np


#Create Numpy array

list_1=[0, 1, 2, 3, 4]
array_1D = np.array(list_1)

print(type(array_1D))
print array_1D

#The key difference between an array and a list is, arrays are designed to handle vectorized operations while a python list is not
#That means, if you apply a function it is performed on every item in the array, rather than on the whole array object.

#Add 2 to each element

print "Adding 2 to each element"
print array_1D + 2

#once a numpy array is created, you cannot increase its size. To do so, you will have to create a new array. But such a behavior of extending the size is natural in a list.

#pass a list of lists to create a matrix like a 2d array

list_2 =[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
array_2D =np.array(list_2)
print 'Two dimensional Array'
print array_2D

#You may also specify the datatype by setting the dtype argument. Some of the most commonly used numpy dtypes are: 'float', 'int', 'bool', 'str' and 'object'.

array_2d_float = np.array(list_2, dtype='float')
print 'Array with floating elements'
print array_2d_float

print 'Converting to int using astype'

#print arr2d_f.astype('int')


#A numpy array must have all items to be of the same data type, unlike lists. This is another significant difference.
#However, if you are uncertain about what datatype your array will hold or if you want to hold characters and numbers in the same array, you can set the dtype as 'object'.
print array_2d_float

print 'Converting Back to List'
print array_2D.tolist()

print 'Lets try 3D array'
list_3= [[[10,11,12],[13,14,15]],[[1,2,3],[4,5,6]]]
array_3D=np.array(list_3)
print array_3D

print 'What type of array it is 1D/2D/3D'
print array_3D.ndim
print 'Size of array'
print array_3D.size
print 'Items present in each dimension'
print array_3D.shape


list_toTest = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]
array_2D_Check=np.array(list_toTest)

print 'Array is'
print array_2D_Check

print 'Size of array'
print array_2D_Check.size

print 'Shape of array'
print array_2D_Check.shape

print 'Dimension of array'
print array_2D_Check.ndim

print 'Datatype of array'
print array_2D_Check.dtype

print 'Extract some element'

print array_2D_Check[:2,1:3]


#Reverse the row and column positions

print 'Reverse the row and column positions'
print array_2D_Check[::-1,::-1]

#Missing values can be represented using np.nan object, while np.inf represents infinite

#print 'Insert a nan and an inf'
#array_2D_Check[1,1] = np.nan  # not a number
#array_2D_Check[1,2] = np.inf  # infinite

# Replace nan and inf with -1. Don't use arr2 == np.nan
#missing_bool = np.isnan(arr2) | np.isinf(arr2)
#arr2[missing_bool] = -1
#arr2

