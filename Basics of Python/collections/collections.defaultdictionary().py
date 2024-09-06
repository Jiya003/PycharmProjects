from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
l=[]
for i in range(1,n+1):
    d[input()].append(i)

for j in range(m):
    l.append(input())

for k in l:
    if k in d.keys():
        print(*d[k])
    else:
        print(-1)