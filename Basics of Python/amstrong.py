#Armstrong_Number
num=int(input("Enter a Value:"))
sum=0
temp=num


while temp>0:
    rem=temp%10#rem is the Remainder.
    sum=sum+(rem**3)#** is the exponential operator
    temp=temp//10#floor division(No Remainder is taken)

if num==sum:
    print("It is a Armstrong Number ",num)
else:
    print("It's not an Armstrong Number")


