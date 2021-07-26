from time import sleep
from datetime import datetime

now = datetime.now()

now_hour = now.hour
now_minute = now.minute
now_second = now.second

name = str(input("Enter your name: " ))
print("Hallo %s. Did you know it is now %02d:%02d:%02d. " % (name, now_hour, now_minute, now_second))

print("So what is your weight in kilograms?")
weight = int(input("Enter weight here: "))

print("What is your height in centimetres?")
height = int(input("Enter your height here: "))

print("")

height = (height/100) * (height/100)

BMI = (weight/height)

print("This is your BMI: ".format(height) + str(BMI))

sleep(2)

if int(BMI) in range(0, 19):
    print("%s you are underweight!" % (name))
elif int(BMI) in range(20, 25):
    print("%s you have healthy weight!" % (name))
elif int(BMI) in range(26, 30):
    print("%s you are overweight!" % (name))
elif int(BMI) in range(31, 40):
    print("%s you are obese!" % (name))

else: print("Just lose weight or grow taller!")
