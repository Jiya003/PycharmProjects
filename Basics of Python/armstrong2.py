num = int(input("Enter a number: ")) #taking input from the user
no_of_digits = len(str(num))
sum1 = 0 #initialize sum
var1 = num
while var1 > 0:

    digit = var1 % 10
    sum1 = sum1 + digit ** no_of_digits
    var1 //= 10
# display the result
if num == sum1:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")