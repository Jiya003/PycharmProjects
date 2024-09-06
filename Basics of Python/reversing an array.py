import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    ar1=numpy.array(arr,float)
    ar2=numpy.flip(ar1)

    return ar2

arr = input().strip().split(' ')
result= arrays(arr)
print(result)