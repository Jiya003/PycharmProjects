import math
x=int(input())
x1=math.radians(x)
y=int(input())
y1=math.radians(y)
ans1=math.sin(x1)*math.cos(y1)

ans2=math.cos(x1)*math.sin(y1)

ans=ans1+ans2

print(format(ans,'.2f'))