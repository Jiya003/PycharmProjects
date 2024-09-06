marks=int(input("Enter your Grade: "))
if(marks>=90):
    print("Excellent")
elif(marks<90 and marks>=70):
    print("Good")
elif(marks<70 and marks>=40):
    print("Average")
elif(marks<40 and marks>=0):
    print("You can do it")
else:
    print("Wrong Input")