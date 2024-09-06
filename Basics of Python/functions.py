a=abs(-5.5)
print(a)
b=abs(5.5)
print(b)

q=[1,2,3,4]
q.reverse()
print(q)

n=[0,1,1]
print(all(n))
n2=[1,1,1]
print(all(n2))

l1=[23,45,89]
print(max(l1))#maximum
print(min(l1))#minimum
print(sum(l1))#sum

#pow()
n3=pow(3,5)
print(n3)

#round function-helps us to round off the given integer

a3=round(4.4967563698,2)
print(a3)

a4=[4,6,2,9,1,0]
print(sorted(a4))
a4.sort()
print(a4)

#user-defined function
def myfunc():
    print('Hello shavi')
myfunc()

#passing multiple arguments
def func1(x,y):
    z=x+y
    print(z)
func1(3,4)

#returning a value-storing a value
def myfunc2(a,b):
    c=a+b
    return(c)
print(myfunc2(2,3))
print(2*myfunc2(2,3))

#calculator
def add(x,y):
    c=x+y
    print(c)

def sub(x,y):
    c=x-y
    print(c)

def multiply(x,y):
    c=x*y
    print(c)

def div(x,y):
    c=x/y
    print(c)

add(5,4)
sub(5,4)
multiply(5,4)
div(5,4)