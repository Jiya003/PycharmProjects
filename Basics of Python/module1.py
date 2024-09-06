#IMPLICIT TYPE CASTING[Indirect type conversion]
A=5.0#float
B=4#int
C=A+B#float+int=float[int converted into float]
print(C)
#EXPLICIT TYPE CASTING[Direct type conversion]
A=5.2#float
B=int(A)#int[float converted into int]
print(B)