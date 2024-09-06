import random
number1 = random.randint(0,9)
number2 = random.randint(0,9)
print(number1)
print(number2)
correct_answer = (number1 + number2)
input_answer = sum(map(int,input("Enter the value of number1 and Number2:").split(" ")))

if (correct_answer == input_answer):
    print("You can proceed to next question!")
elif(correct_answer != input_answer):
    print("Sorry, You have entered wrong answer!")
else:
    print("Loser")