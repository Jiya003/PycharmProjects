#017-555-1212 is the correct format,

s=input()#Input a number
value=True#Assingning a condition

#Checking where Format can be false.
if(len(s)!=12):
    value=False
if(s[3]!='-' or s[7]!='-'):
    value=False
for i in range(12):#12 number digit
    if(i==3 or i==7):
        continue
    if(not(s[i].isdigit())):#checking whether all digits is a number or not.
        value=False

print(value)