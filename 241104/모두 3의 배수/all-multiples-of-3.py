a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
l = [a1, a2, a3, a4, a5]
flag = 1

for i in range(5):
    if l[i] % 3 == 0:
        continue
    else:
        flag = 0
        break

print(flag)