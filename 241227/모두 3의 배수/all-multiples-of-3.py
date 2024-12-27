l = [None] * 5
flag = 1

for i in range(5):
    l[i] = int(input())    
    if l[i] % 3 != 0:
        flag = 0

print(flag)