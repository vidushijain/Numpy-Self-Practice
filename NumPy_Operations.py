import numpy as np

list1 = [[1, 2, 3, 4],[3, -1, -1, 6], [5, 6, 7, 8]]
array_2D=np.array(list1)
print array_2D

print 'Mean'
print array_2D.min()

print 'Max'
print array_2D.max()

print 'Min'
print array_2D.min()

print 'Column wise minimum'
print np.amin(array_2D, axis=0)

print 'Row wise minimum'
print np.amin(array_2D, axis=1)

#np.apply_over_axis

print 'Cumulative Sum'
print np.cumsum(array_2D)


#If we done use copy, portion of array still points to parent array. Any changes in new reflects in parent array


array_2D_copy=array_2D.copy()
print 'Copy of Array'
print array_2D_copy

#Reshaping -> changing the arrangement of items so that shape of the array changes while maintaining the same number of dimensions.

#Flattening, however, will convert a multi-dimensional array to a flat 1d array. And not any other shape

print 'Reshape'
array_2D_reshape=array_2D.reshape(4,3)
print array_2D_reshape

#There are 2 popular ways to implement flattening. That is using the flatten() method and the other using the ravel() method.
#The difference between ravel and flatten is, the new array created using ravel is actually a reference to the parent array.
#  So, any changes to the new array will affect the parent as well. But is memory efficient since it does not create a copy.

print 'Lets Flatten'
print array_2D.flatten()

# Lower limit is 0 be default
print 'Range f 5'
print(np.arange(5))

# 0 to 9
print 'from 0-9'
print(np.arange(0, 10))

# 0 to 9 with step of 2
print 'With equal step of 2'
print(np.arange(0, 10, 2))

# 10 to 1, decreasing order
print 'Decreasing order'
print(np.arange(10, 0, -1))

print 'Limiting the number of elements'
print np.linspace(start=1, stop=50, num=10, dtype=int)

#np.logspace which rises in a logarithmic scale.
#In np.logspace, the given start value is actually base^start and ends with base^stop, with a default based value of 10.

# Limit the number of digits after the decimal to 2
np.set_printoptions(precision=2)

print 'Start at 10^1 and end at 10^50'
print np.logspace(start=1, stop=50, num=10, base=10)

print 'Shape with all zero'

print np.zeros([2,2])

print 'Shape with all ones'
print np.ones([2,2],dtype=str)

#np.tile will repeat a whole list or array n times. Whereas, np.repeat repeats each item n times.

a1=[1,2,3]
print 'List is',str(a1)

print 'Repeat list two time'
print np.tile(a1,2)

print 'Repeat each element of the list two times'
print np.repeat(a1,2)

a2d=[[1,2],[3,4]]
print np.array(a2d)

print 'Lets try repeating axis'
print np.repeat(a2d,2,axis=0)

