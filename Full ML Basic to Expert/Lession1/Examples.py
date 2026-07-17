#Import type
import numpy as np;

print(np.__version__)

#array type
numbers = np.array([1,2,4,7,6,8]);
print(numbers)

print(type(numbers))

#Meaning

#nd
#↓
#n-dimensional
number = np.array([
                [1,2,4],
                [100,200,300]
                ]);
#Array Attributes
print(number.ndim)
print(number.shape)
print(number.dtype)
print(number.size)
