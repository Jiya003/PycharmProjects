str=input()
l = len(str)
flag = 0
for i in range(l):
    flag = 0
    for j in range(l):
        if str[i] == str[j] and i != j:
            flag = 1
            break
    if flag == 0:
        print(i)
        break

if flag == 1:
    print("-1")