#Cho 2 số tự nhiên a và b, hãy in ra tỉ số của hai số a và b đồng thời với tỉ số rút gọn của chúng
a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
ucln=0
for i in range(1, min(a, b)+1):
    if (a%i==0) and (b%i==0):
        ucln=i
rg_a=a//ucln
rg_b=b//ucln
print(f'Tỉ số của {a} và {b} là: {a}/{b}')
print(f'Tỉ số rút gọn của {a} và {b} là: {rg_a}/{rg_b}')