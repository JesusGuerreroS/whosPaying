#################################################
#simple script to show who's gonna play the bill
#################################################
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random = random.randint(0, (len(names) - 1))

print(names[random])