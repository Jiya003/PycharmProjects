n=input()
m=input()
ln=n.lower()
lm=m.lower()
v=1
u=1
for i in range (len(n)) :
    if i=="o":
        v=1
    else:
        v=0

for j in range (len(m)) :
    if j=="o":
        u=1

    else:
        u=0

if(v==1 and u==1):
    print("0")
else:
    print("1")