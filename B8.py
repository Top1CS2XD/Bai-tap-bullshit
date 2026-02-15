#Nhập số từ bàn phím cho tới khi nhập số 28 thì dừng
n=int(input('Nhập số: '))
so=0
while n!=28:
    n=int(input('Nhập số: '))
    if n==28:
        print('Dừng')
        break