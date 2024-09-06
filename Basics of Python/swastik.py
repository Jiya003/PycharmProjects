a=int(input('Enter a number:'))
for i in range (1,a):
    for j in range(1,a):
        if((j==1 and i<=a/2)and (j==a/2) and (i==a/2)and(i==1 and j>=a/2)and((i==a/2 and j==a )and i>a/2 ) and (i==a and j<=a/2)):
            print('*')
        else:
            print(" ")
    print(" ")
