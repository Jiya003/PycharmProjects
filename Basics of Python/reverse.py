num=int(input("Enter a Value:"))
rev=0
a=num
while num>0:
    ren=num%10
    rev=(rev*10)+ren#ren is Remainder
    num=num//10
print(rev)
if(a==rev):
    print("Pallindrome Number")
else:
    print("Not a Pallindrome Number")