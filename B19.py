#Cho số tự nhiên n có 6 chữ số, hãy cho biết n có phải là số đảo ngược hay không (viết xuôi và ngược là như nhau, ví dụ 123321 là số đảo ngược). Tính tổng các chữ số chẵn của n
n=int(input('Nhập n: '))
chu_so=len(str(n))
so=0
tong=0
chuc=n//10
donvi=n%10
tram=n//100
nghin=(n//1000)
chuc_nghin=(n//10000)
tram_nghin=(n//100000)
if chu_so==6:
    if donvi==tram_nghin and chuc==chuc_nghin and tram==nghin:
        print(f'{n} là số đảo ngược')
    else:
        print(f'{n} ko là số đảo ngược')
    for i in range(1, 7):
        so=n%10
        n=n//10
        if so%2==0:
            tong+=so
    print(f'Tổng các chữ số chẵn là: {tong}')