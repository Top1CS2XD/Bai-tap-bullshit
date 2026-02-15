#Viết chương trình tính tổng nghịch đảo của n số nguyên đầu tiên
n=int(input('Nhập n: '))
tong=0
for i in range(1,n+1):
    tong+=1/i
print(tong)