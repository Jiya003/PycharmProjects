choice=""
while(choice=="y"):
    try:
        num=int(input("Enter number:"))
    except TypeError:
        print("Please Enter the number")
        print("Do You want to continue?")
        print("Y for Yes N for No:")
        choice=input()


print("Your number is:",num)