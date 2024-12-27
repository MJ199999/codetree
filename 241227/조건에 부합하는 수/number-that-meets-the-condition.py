i = int(input())

for a in range(1, i+1):
    if (a % 2 == 0) & (a % 4 != 0):
        continue
    elif ((a // 8) % 2 == 0):
        if (a // 8 != 0):
            continue
    elif (a % 7 < 4):
        continue
    else:
        print(a, end=" ")