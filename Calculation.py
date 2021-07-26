list1 = [77, 73, 84, 85, 79, 85, 85, 72]

#This is the first method
"""from collections import Counter

print("Highest score is: " , max(list1) )

def Average(list1):
    return sum(list1)/len(list1)
average = Average(list1)
print("Average of the list = ", round(average, 2))

data = Counter(list1)
data.most_common()
data.most_common(1)

print("Mode of the list is: ", data.most_common(1))"""

#This is the second method
import statistics
median = statistics.median(list1)
print("The median of the list is: ", median)

mode = statistics.mode(list1)
print("The mode of the list is: ", mode)

mean = statistics.mean(list1)
print("The mean of the list is: ", mean)