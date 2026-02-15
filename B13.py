#Nhập vào số tự nhiên n có 2 chữ số, tính tổng tất cả các số chẳn lớn hơn n và có chữ số đứng trước chia hết cho chữ số phía sau
n=int(input('Nhập n: '))
tong=0
for i in range(n, 100):
    chuc=i//10
    donvi=i%10
    if (i%2==0) and (donvi!=0) and (chuc%donvi==0):
        tong+=i
print(tong)