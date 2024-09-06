h=int(input())
c=69
for x in range(h):
    print("-" * (h - x)+('%c' %(c+x))* (2*x + 1)+"-"*(h-x))
for y in range(h - 2, -1, -1):
    print("-" * (h - y)+"*" * (2*y + 1)+"-"*(h-y))