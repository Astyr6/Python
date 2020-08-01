import this

num = int(input("Number -> "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []


for x in a:
    if x < num:
        b.append(x)

print(b)