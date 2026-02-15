#Cho 2 số tự nhiên a và b, hãy cho biết tình trạng nguyên tố của a và b. Tính tổng tất cả các số nguyên tố trong phạm vi từ a đến b
a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
dem_a=0
dem_b=0
dem=0
tong=0
for i in range(1, b+1):
    if b%i==0:
        dem_b+=1
if dem_b==2:
    print(f'{b} là số ngto')
else:
    print(f'{b} ko là số ngto')
for i in range(1, a+1):
    if a%i==0:
        dem_a+=1
if dem_a==2:
    print(f'{a} là số ngto')
else:
    print(f'{a} ko là số ngto')
for i in range(a, b+1):
    for j in range(1, i+1):
        if i%j==0:
            dem+=1
    if dem==2:
        tong+=i
    dem=0
print(f'Tổng các số ngto từ {a} đến {b} là: {tong}')