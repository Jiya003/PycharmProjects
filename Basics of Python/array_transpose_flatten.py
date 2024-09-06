import numpy

n, m = map(int, input().split())
r = []
for i in range(n):
    row = list(map(int,input().split()))
    r.append(row)

arr = numpy.array(r)
print(numpy.transpose(arr))
print(arr.flatten())


