#Chức năng
print('Chọn 1 chức năng:')
print('1.Cộng')
print('2.Trừ')
print('3.Nhân')
print('4.Chia')
chon = input('Chọn chức năng (1/2/3/4): ')
a=float(input('Nhập số thứ nhất: '))
b=float(input('Nhập số thứ hai: '))
#Xử lí blah blah blah
if chon == '1':
    print(f'Kết quả: {a} + {b} = {a+b}')
elif chon == '2':
    print(f'Kết quả: {a} - {b} = {a-b}')
elif chon == '3':
    print(f'Kết quả: {a} * {b} = {a*b}')
elif chon == '4':
    if b != 0:
        print(f'Kết quả: {a} / {b} = {a/b}')
    else:
        print('Lỗi: Không thể chia cho 0')
else:
    print('Chức năng không hợp lệ')