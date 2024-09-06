num=int(input('Enter a Number:'))
sum=0
a=0
b=1
for i in range (0,num):#iteration
    print(sum)
    a=b
    b=sum
    sum=a+b

