#Cho số n, hãy in ra màn hình tất cả các số nhỏ hơn n và có đúng 3 ước số
n=int(input('Nhập n: '))
dem=0
for i in range(1, n):
    for j in range(1, i+1):
        if i%j==0:
            dem+=1
    if dem==3:
        print(i)