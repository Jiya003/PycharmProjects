#repr:Printable representation of string of the given object
import numpy as np
arr=np.array([[1,2,3,9,5],[9,5,9,5,9],[4,9,5,6,7]])
seq="9,5"
output=repr(arr).count(seq)
print(output)
