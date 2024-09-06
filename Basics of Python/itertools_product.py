from itertools import product
input_list1=list(map(int,input().split()))
input_list2=list(map(int,input().split()))
A=product(input_list1,input_list2)
print(*A)