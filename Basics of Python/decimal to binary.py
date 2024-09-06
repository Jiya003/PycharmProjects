print("\t\t\t\t\tChild Nutrients Calculator\n")
print("""\tMy name is Divyanshi Maurya....I am here to calculate your
child's Health..:\n""")
name = input("\nEnter your Child's name :")
while True:
    age = int(input("\nEnter your child's age: "))
    if 0 <= age <= 8:
        break
    else:
        print("\nThe child's age must be between 0-8 years")
        continue

gender = input("\nEnter child's gender :")
height = int(input("\nEnter height (in inches):"))
weight = int(input("\nEnter weight (in pounds) :"))
print("\nThankyou for entering data.....\n")


food_calories = {"Milk": 100, "Egg": 155,  "Rice": 130,  "Lentils": 113, "Vegetable": 85,"Meat": 143 }

print("Please Enter the following Data carefully..:\n")
milk=int(input("Total daily consumption of in MILK in grams: "))
egg=int(input("Total daily consumption of in EGG in grams: "))
rice=int(input("Total daily consumption of in RICE in grams: "))
lentils=int(input("Total daily consumption of in LENTILS in grams: "))
veg=int(input("Total daily consumption of in VEGETABLES in grams: "))
meat=int(input("Total daily consumption of in MEAT in grams: "))

for i in food_calories.values():
    milk_cal=milk*i[0]
    egg_cal=egg*i[1]
    rice_cal=rice*i[2]
    lentils_cal=lentils*i[3]
    veg_cal=veg*i[4]
    meat_cal=meat*i[5]

total_calories=int(milk_cal+egg_cal+rice_cal+lentils_cal+veg_cal+meat_cal)

print("Total calorie consumption of the child is : ",total_calories)
if age>=0 and age <2:
    print("The minimum daily calorie requirement is 800 calorie.")
if age>=2 and age <4:
    print("The minimum daily calorie requirement is 1400 calorie.")
if age>=4 and age<=8:
    print("The minimum daily calorie requirement is 1800 calorie.")


#BMI Calculator
try:
    bmi = weight / (height ** 2) * 703
    print("The BMI of the child is :",bmi)
except ZeroDivisionError:
    print("Error: Height cannot be zero.")

if bmi < 16:
    print("Severely Underweight. Please increase the diet.")
elif 16 <= bmi < 18.5:
    print("Underweight. Please increase the diet")
elif 18.5 <= bmi < 25:
    print("Your child is Healthy")
elif 25 <= bmi < 30:
    print("Your child is Overweight")
elif bmi >= 30:
    print("Your child is Obese")
else:
    print("Wrong BMI value")
