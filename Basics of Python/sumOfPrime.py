
last_number = int(input())
sum = 0
# Initializing the sum to 0
for number in range(2, last_number + 1):
# Using for loop starting from 2 as it is the first prime number.
    i = 2
    for i in range(2, number):
        if (int(number % i) == 0):
            i = number
            break;
#Only if the number is a prime number, continue to add it.
    if i is not number:
        sum = sum + number
print(sum)
print(15//2)
num=input().split(",")
w=num[0]
print(w)