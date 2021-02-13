'''
Make a program which will randomly create a character’s stats based on
several rules set by the user. Have it generate a class, gender,
strength/magic/dexterity points, and extra abilities or trades.
Have the program save it to a file which can then be printed out
so that it can be used in a game.
Extension: 
1. Make a mystical name generator.
   Perhaps randomise different name parts such as sha-ra-lam or big-lim-con
   to create names for each of your randomly generated characters.
'''
import random
GenderL = ["Male","Female","None"]
Class = ["Bird","Animal","Reptile","Amphebian","Carnovore","Omnivour","Harbivour"]
abilities = ["fire","smash","invisibility","punch"]
Ab = random.randint(0,3)
Abli = abilities[Ab]
Gen = random.randint(0,2)
G = GenderL[Gen]
Cla = random.randint(0,6)
C = Class[Cla]
low = int(input("Enter the lowerst strength level: "))
high = int(input("Enter the highest strength level: "))
strength = random.randint(low,high)
print("The gender of Pokemon is : ",G)
print("The class of Pokemon is : ",C)
print("The strength of Pokemon is : ",strength)
print("The pokenmon has the extra ability of : ",Abli)
