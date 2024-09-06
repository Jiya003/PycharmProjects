import math
n=float(input())
if n>=-1.0 and n<=1.0:
    ans=math.asin(n)
    print(format(ans,'.4f'))
else:
    print("Invalid")
