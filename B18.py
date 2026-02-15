#Cho 2 số tự nhiên m và n, hãy cho biết số nào có nhiều chữ số hơn, in ra màn hình tất cả các số nguyên tố nhỏ hơn số vừa tìm được
m=int(input('Nhập m: '))
n=int(input('Nhập n: '))
r=len(str(m))
s=len(str(n))
if r>s:
    print(f'Số {m} có nhiều chữ số hơn số {n}')
    for i in range(2, m):
        dem_m=0
        for j in range(1, i+1):
            if i%j==0:
                dem_m+=1
        if dem_m==2:
            print(i, end=' ')
else:
    print(f'Số {n} có nhiều chữ số hơn số {m}')
    for i in range(2, n):
        dem_n=0
        for j in range(1, i+1):
            if i%j==0:
                dem_n+=1
        if dem_n==2:
            print(i, end=' ')