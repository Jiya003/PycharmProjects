# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
cols=namedtuple('cols',input().split())
s=0
for i in range(n):
    s=s+(int(cols(*input().split()).MARKS))

print(s/n)