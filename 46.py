n=int(input('Nhập n: '))
tong=0
for i in range(1,n):
    if (i%4==0) and (i%5!=0):
        tong+=i
print(tong)