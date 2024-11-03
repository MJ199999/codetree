n = int(input())
i = 1
while(True):
    if (i == 1):
        a = n
    a = a / i
    if (a <= 1):
        print(i)
        break
    i += 1