import random

numbers = list(range(0,100))

list1 = []
list2 = []

for i in range(0,50):
    list1.append(random.choice(numbers))
    list2.append(random.choice(numbers))

print("This is list1 :")
print(list1)
print("")
print("This is list2 :")
print(list2)
print("")

list3 = []

for i in list1:
    if i in list2:
        list3.append(i)

print("This is the commons items between the two lists :")
print(list3)
print("")
