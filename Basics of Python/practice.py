#formatting strings
brand='Lenovo'
exchangeRate=1.23456789

message='The brand %s has a laptop of %d dollars and the exchange rate is %3.4f'%(brand,1000,exchangeRate)
msg2='hello {0:s}....kaisi ho B{1:d} wali rate hai tumhare rent ka {2:3.5f}'.format('Divyanshi', 528, 1.234567)
print(message)
print(msg2)

message1='{0} is easier than {1}'.format('python','java')
print(message1)
message2='{1} is easier than {0}'.format('python','java')
print(message2)
message3='{}'.format('Hello')

print(message3)
message4='{:5.7f} is greater than {:d}'.format(1.23456, 0)
print(message4)

#type casting:three in built functions int,float,string
a=5.34567728
print(int(a))#float to int
print(float(2))#int to float
print(float("2.019563"))#string to float
#str() converts anything into a string


#lists
#list from the front
userage=[20,21,22,23,24,25]
print(userage[0])
print(userage[1])
print(userage[2])
print(userage[3])
print(userage[4])
print(userage[5])
#list from the back
print(userage[-1])
print(userage[-2])
print(userage[-3])
print(userage[-4])
print(userage[-5])
print(userage[-6])

userage2=userage#assigning list to another variable
print(userage2)

print(userage[2:4:1])
'''The notation 2:4 is known as a slice. Whenever we use the slice notation
in Python, the item at the start index is always included, but the item at
the end is always excluded. '''
print(userage[0:5:2])#seperstor is 2

#function

def my_function():
    print("Hello from a function")

my_function()

#arguments in functions
def myfunction(fname):#fname is parameter(variable listed in the parentheses)
    print(fname+" book")

myfunction("mathematics")#arguments is the value sent to the function
myfunction("physics")

#practice
t=int(input())
m=t//60
s=t%60
print('m'+'s')
