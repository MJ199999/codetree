a, b = map(int, input().split())

flag = 0

for i in range(a, b+1):
    if (1920 % i == 0) & (2880 % i == 0):
        flag = 1
        break


if flag == 0:
    print(flag)
elif flag == 1:
    print(flag)