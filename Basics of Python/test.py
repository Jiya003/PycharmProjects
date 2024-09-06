import random
#A random function generates a random floating no. between interval of 0 and 1(0,1)
print(random.random())
#A randint function generates some random integers between the interval of any two integers a and b including a and b
print(random.randint(4,12))
#A uniform function generates any floating no. between a and b interval excluding a and b
print(random.uniform(6,9))
#A randrange function (start,end,skip) generates any random intergers from the range including start and end
print(random.randrange(4,16,4))
print(random.randrange(10,0,-1))
#A sample function genterates a sample between the range
print(random.sample(range(1,20),5))#List format
#A shuffle function:shuffles the list
l=['Divyanshi','Anil','Parul','Aparna']
random.shuffle(l)#return none if we done printing
print(l)
#A choice function we can get a paticular element from the list
p=random.choice(l)
print(p)
#wap that generates a random numbers between 1 and 6 simulates a dice
n=random.randint(1,6)
print(n)
if n==6:
    n2=random.randint(1,6)
    print(n2)
    if(n2==6):
        n3=random.randint(1,6)
        print(n3)
    else:
        print("Finish")
else:
    print("Finish")