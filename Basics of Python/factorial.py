num=int(input("Enter Value"))
fact=1
for i in range(num,0,-1):#last value is not counted by the python
   fact=fact*i

print(fact)