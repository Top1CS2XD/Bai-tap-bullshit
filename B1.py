#B1. Cho số tự nhiên n, hãy cho biết n tăng lên mấy lần để vừa lớn hơn 2k với k và n được nhập từ bàn phím
n = int(input('Nhập n: '))
k = int(input('Nhập k: '))
dem=0
while n<=2*k:
    n*=2
    dem+=1
print(dem)
