num = int(input("Number -> "))

a = range(1, num + 1)

c = []

for b in a:
    if num % b == 0:
        c.append(b)

print(c)