p=int(input('Please Enter Your percentage:'))

if p<=25:
    print('Your Grade is D')
elif p>25 and p<=45:
    print('Your Grade is C')
elif p>45 and p<=50:
    print('Your Grade is B')
elif p>50 and p<=60:
    print('Your Grade is B+')
elif p>60 and p<=80:
    print('Your Grade is A')
elif p>80:
    print('Your Grade is A+')
else:
    print('Invalid Input')