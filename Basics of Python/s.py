s=input()
x=s[:].split(" ")
l=""
for i in x:
    s = s.replace(i, i.capitalize())
print(s)