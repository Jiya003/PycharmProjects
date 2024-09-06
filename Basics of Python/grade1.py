#functions
def grade(marks):
    print("Your percentage is : ",marks)
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

#main function
eng=int(input("Enter your Eng marks: "))
mat=int(input("Enter your Maths marks: "))
comp=int(input("Enter your Computer marks: "))
hindi=int(input("Enter your Hindi marks: "))
sum=int(eng+mat+comp+hindi)
per=int((sum/400)*100)
grade(per)
