#Tính tổng các số chia hết cho 4 và không chia hết cho 5 nhỏ hơn n
n=int(input('Nhập n: '))
tong=0
for i in range(n):
    if (i%4==0) and (i%5!=0):
        tong+=i
print(tong)