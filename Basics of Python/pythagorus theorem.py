import math
n=int(input())
m=int(input())
p=math.pow(n,2)
b=math.pow(m,2)
c=p+b#Hypotenus Calculation
x=math.sqrt(c)
#Squaring the Hypotenus
a=math.pow(x,3)
h=format(a, '.3f')#Formatting till 3 decimal places
print(h)