a = int(input())

flag = 1

for i in range(1, a+1):
    if ((int(i/8) % 2 == 0) | (i % 7 < 4) | ((i % 2 == 0) & (i % 4 != 0))):
        continue
    else:
        print(i)