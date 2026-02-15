n=int(input('Nhập n: '))
m=int(input('Nhập m: '))
for i in range(n, m+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")