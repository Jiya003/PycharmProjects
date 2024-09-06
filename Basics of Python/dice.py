import random
roll_again="yes"

while (roll_again=='yes' or roll_again=='Yes'):
    val=random.randint(1,6)
    print("You get in the dice:",val)
    roll_again = input("Do you want to roll the dice again? : Yes or No")


