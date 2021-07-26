import statistics
from datetime import datetime

now = datetime.now()

now_hour = now.hour
now_minute = now.minute
now_second = now.second

list1 = []

name = str(input("Enter your name: " ))
print("Hallo %s. Did you know it is now %02d:%02d:%02d. " % (name, now_hour, now_minute, now_second))
  
# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))
  
# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

median = statistics.median(list1)
print("The median of the list is: ", median)

mode = statistics.mode(list1)
print("The mode of the list is: ", mode)

mean = statistics.mean(list1)
print("The mean of the list is: ", mean)

print("Thank you %s. Feel free to try again" % (name) )