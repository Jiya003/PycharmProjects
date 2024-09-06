import re
s=input()
vowels="aeiou".upper()
kevin=""
stuart=""
points1=0
points2=0
for i in range(len(s)):
    if s[i] in vowels:
        kevin=kevin+s[i]
    else:
        stuart=stuart+s[i]
print(kevin)
print(stuart)
start=0
start1=0
count=0
count1=0
pos = s.find(kevin, start)
pos1=s.find(stuart,start)
if pos != -1:
    start = pos + 1
    count += 1
else:
    break

if pos1!= -1:
    start1 = pos1+ 1
    count1 += 1
else:
    break

if(count<count1):
    print("Stuart",count)
elif(count>count1):
    print("Kevin",count1)
else:
    print("Draw")