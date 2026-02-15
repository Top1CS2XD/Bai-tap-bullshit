#Viết chương trình tính tổng bình phương các số chẵn từ 1 đến n; với n được nhập từ bàn phím
n=int(input('Nhập n: '))
tong=0
for i in range(2,n+1,2):
    tong+=i**2
print(tong)