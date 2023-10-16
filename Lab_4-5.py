import time as dt
#Create a Python file named lab_4-5.py
#Write a program that prompts one user for their first name, 
print("Hello user 1 good day today what is your name?")
dt.sleep(0.9)
person1 = input("input here:")
dt.sleep(0.9)
#then a second user for their first name. Using the format method, 
print(f"Thank you {person1} now please pass the computor to some one else.")
dt.sleep(0.9)
print("Hello user 2 good day today what is your name?")
dt.sleep(0.9)
person2 = input("input here:")
dt.sleep(0.9)
#output a string that follows this template.
print("Thank you")
dt.sleep(0.9)
print("Calculateing")
dt.sleep(0.9)
print(".")
dt.sleep(0.9)
print("..")
dt.sleep(0.9)
print("...")
dt.sleep(0.9)
#Hello, person1. My name is person2.
print("Hello, {0}. My name is {1}.".format(person1,person2))
dt.sleep(0.9)
print("Ha ha I have stolen your identitiy you lose.")
