n=int(input())
rev=0
k=1
while n>0:
    rem=n%10
    k=k*rem
    n=n//10
print(k)