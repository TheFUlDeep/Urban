n = int(input("Значение первого поля "))

resault = ""

i = 1
while i < n:
    j = 1
    for j in range(i+1, 21 - i):
        if n % (i + j) == 0:
            resault = resault + str(i) + str(j)
    i += 1

print(resault)
